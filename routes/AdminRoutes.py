from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from controllers.UserController import UserController
from utils.checkAdminUser import check_if_admin

router = APIRouter()
user_controller = UserController()

class AdminClaimPayload(BaseModel):
    email: EmailStr

@router.post("/set-admin/", summary="Conceder permissão de administrador a um usuário", dependencies=[Depends(check_if_admin)])
def set_admin_claim(payload: AdminClaimPayload):
    """
    Endpoint para atribuir permissões de administrador a um usuário existente.
    **Atenção:** Este é um endpoint sensível e está protegido por verificação de admin.
    """
    try:
        result = user_controller.set_admin_claim(payload.email)
        return result
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno do servidor: {e}")
