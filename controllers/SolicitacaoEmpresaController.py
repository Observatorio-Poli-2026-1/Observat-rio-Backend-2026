from uuid import uuid4

from controllers.ConexaoFirestore import ConexaoFirestore
from models.SolicitacaoEmpresaModel import SolicitacaoEmpresaModel


class SolicitacaoEmpresaController(ConexaoFirestore):

    def __init__(self):
        self.db = ConexaoFirestore.conect(self)

    def setSolicitacao(self, dados: SolicitacaoEmpresaModel):
        try:
            key_doc = uuid4().hex
            dados.id = key_doc
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
