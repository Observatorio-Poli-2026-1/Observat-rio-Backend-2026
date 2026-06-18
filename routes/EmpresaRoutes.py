from fastapi import APIRouter, Depends
from controllers.SolicitacaoEmpresaController import SolicitacaoEmpresaController
from models.SolicitacaoEmpresaModel import SolicitacaoEmpresaModel
from utils.checkAdminUser import check_if_admin

router = APIRouter()

@router.post("/solicitacoes_empresa/")
def criar_solicitacao(dados: SolicitacaoEmpresaModel):
    return SolicitacaoEmpresaController().setSolicitacao(dados)

@router.get("/solicitacoes_empresa_publicas/")
def listar_solicitacoes_publicas():
    return SolicitacaoEmpresaController().getSolicitacoesPublicas()

@router.get("/solicitacoes_empresa/", dependencies=[Depends(check_if_admin)])
def listar_solicitacoes():
    return SolicitacaoEmpresaController().getSolicitacoes()

@router.delete("/solicitacoes_empresa/{id}/", dependencies=[Depends(check_if_admin)])
def deletar_solicitacao(id: str):
    return SolicitacaoEmpresaController().deleteSolicitacao(id)
