from uuid import uuid4

from fastapi import HTTPException

from controllers.ConexaoFirestore import ConexaoFirestore
from models.SolicitacaoEmpresaModel import SolicitacaoEmpresaModel


class SolicitacaoEmpresaController(ConexaoFirestore):

    def __init__(self):
        self.db = ConexaoFirestore.conect(self)

    def setSolicitacao(self, dados: SolicitacaoEmpresaModel):
        return self._criarSolicitacao(dados, 'Pendente')

    def setSolicitacaoAprovada(self, dados: SolicitacaoEmpresaModel):
        return self._criarSolicitacao(dados, 'Aprovado')

    def _criarSolicitacao(self, dados: SolicitacaoEmpresaModel, status: str):
        try:
            key_doc = uuid4().hex
            dados.id = key_doc
            dados.status = status
            docs = self.db.collection('solicitacoes_empresa').document(key_doc)

            docs.set(dados.toMaps())
            solicitacao = self.db.collection('solicitacoes_empresa').document(key_doc).get().to_dict()
            return {'msg': 'Solicitacao criada com sucesso!', 'solicitacao': solicitacao}
        except Exception as e:
            raise e

    def getSolicitacoes(self):
        try:
            docs = self.db.collection('solicitacoes_empresa').stream()
            solicitacoes = [doc.to_dict() for doc in docs]
            if solicitacoes:
                return {'msg': 'Sucesso ao listar!', 'total de solicitacoes': len(solicitacoes), 'solicitacoes': solicitacoes}
            else:
                return {'msg': 'Sem solicitacoes!'}
        except Exception as e:
            return {'msg': f'Houve um erro! {e}'}

    def getSolicitacoesPublicas(self):
        try:
            docs = self.db.collection('solicitacoes_empresa').stream()
            solicitacoes = []

            for doc in docs:
                data = doc.to_dict()
                if data.get('status') != 'Aprovado':
                    continue

                solicitacoes.append({
                    'id': data.get('id'),
                    'empresa': data.get('empresa'),
                    'descricao_problema': data.get('descricao_problema'),
                    'expectativa': data.get('expectativa'),
                    'prazo': data.get('prazo'),
                })

            if solicitacoes:
                return {'msg': 'Sucesso ao listar!', 'total de solicitacoes': len(solicitacoes), 'solicitacoes': solicitacoes}
            else:
                return {'msg': 'Sem solicitacoes!'}
        except Exception as e:
            return {'msg': f'Houve um erro! {e}'}

    def aprovarSolicitacao(self, id: str):
        try:
            doc_ref = self.db.collection('solicitacoes_empresa').document(id)
            doc = doc_ref.get()

            if not doc.exists:
                raise HTTPException(status_code=404, detail="Solicitacao nao encontrada")

            doc_ref.update({'status': 'Aprovado'})
            solicitacao = doc_ref.get().to_dict()
            return {'msg': 'Solicitacao aprovada com sucesso!', 'solicitacao': solicitacao}
        except Exception as e:
            raise e

    def recusarSolicitacao(self, id: str):
        try:
            doc_ref = self.db.collection('solicitacoes_empresa').document(id)
            doc = doc_ref.get()

            if not doc.exists:
                raise HTTPException(status_code=404, detail="Solicitacao nao encontrada")

            solicitacao = doc.to_dict()
            doc_ref.delete()
            return {'msg': 'Solicitacao recusada e excluida com sucesso!', 'solicitacao': solicitacao}
        except Exception as e:
            raise e
