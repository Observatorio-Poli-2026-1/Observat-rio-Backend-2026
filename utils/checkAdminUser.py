from firebase_admin import auth as admin_auth, firestore
from fastapi import HTTPException, Request
from controllers.keyAdmin import initialize_firebase
import logging

logger = logging.getLogger(__name__)

try:
    initialize_firebase()
except Exception:
    pass


def get_token_from_request(request: Request):
    auth_header = request.headers.get('Authorization')
    if auth_header and auth_header.startswith('Bearer '):
        return auth_header.split(' ')[1]

    return request.query_params.get('id_token')


def check_if_admin(request: Request):
    id_token = get_token_from_request(request)

    if not id_token:
        raise HTTPException(status_code=401, detail="Token nao fornecido.")

    try:
        decoded_token = admin_auth.verify_id_token(id_token, clock_skew_seconds=60)

        if decoded_token.get('admin', False):
            return decoded_token

        user_id = decoded_token.get('uid')
        if user_id:
            user_doc = firestore.client().collection('users').document(user_id).get()
            user_data = user_doc.to_dict() if user_doc.exists else {}

            if user_data.get('is_admin', False):
                return decoded_token

        raise HTTPException(status_code=403, detail="Acesso proibido: Apenas administradores.")
    except HTTPException:
        raise
    except Exception as e:
        logger.info(f"!!! ERRO ADMIN VERIFY: {e}")
        raise HTTPException(status_code=401, detail=f"Sessao invalida: {str(e)}")


def check_if_login(request: Request):
    id_token = get_token_from_request(request)

    if not id_token:
        logger.info("!!! ERRO: Token nao encontrado no request.")
        raise HTTPException(status_code=401, detail="Token nao fornecido.")

    try:
        decoded_token = admin_auth.verify_id_token(id_token, clock_skew_seconds=60)
        return decoded_token
    except ValueError as e:
        logger.info(f"!!! ERRO CONFIG FIREBASE: {e}")
        try:
            initialize_firebase()
            return admin_auth.verify_id_token(id_token, clock_skew_seconds=60)
        except Exception as e2:
            logger.info(f"!!! ERRO RE-INIT: {e2}")
            raise HTTPException(status_code=500, detail=f"Erro interno de autenticacao: {str(e2)}")
    except Exception as e:
        logger.info(f"!!! ERRO LOGIN VERIFY: {e}")
        raise HTTPException(status_code=401, detail=f"Token invalido: {str(e)}")
