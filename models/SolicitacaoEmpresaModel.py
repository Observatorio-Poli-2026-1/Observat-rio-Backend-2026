from typing import Optional
from pydantic import BaseModel

class SolicitacaoEmpresaModel(BaseModel):
    id: str
    empresa: str
    contato_email: str
    telefone: Optional[str] = ''
    descricao_problema: str
    expectativa: Optional[str] = ''
    prazo: Optional[str] = ''
    status: Optional[str] = 'Pendente'

    def toMaps(self):
        return {
            'id': self.id,
            'empresa': self.empresa,
            'contato_email': self.contato_email,
            'telefone': self.telefone,
            'descricao_problema': self.descricao_problema,
            'expectativa': self.expectativa,
            'prazo': self.prazo,
            'status': self.status,
        }
