from fastapi import APIRouter, Depends
from controllers.SolicitacaoEmpresaController import SolicitacaoEmpresaController
from models.SolicitacaoEmpresaModel import SolicitacaoEmpresaModel
from utils.checkAdminUser import check_if_admin

router = APIRouter()

@router.post("/solicitacoes_empresa/")
def criar_solicitacao(dados: SolicitacaoEmpresaModel):
    return SolicitacaoEmpresaController().setSolicitacao(dados)

@router.post("/admin/solicitacoes_empresa/", dependencies=[Depends(check_if_admin)])
def criar_solicitacao_admin(dados: SolicitacaoEmpresaModel):
    return SolicitacaoEmpresaController().setSolicitacaoAprovada(dados)

@router.get("/solicitacoes_empresa_publicas/")
def listar_solicitacoes_publicas():
    return SolicitacaoEmpresaController().getSolicitacoesPublicas()

@router.get("/solicitacoes_empresa/", dependencies=[Depends(check_if_admin)])
def listar_solicitacoes():
    return SolicitacaoEmpresaController().getSolicitacoes()

@router.put("/solicitacoes_empresa/{id}/aprovar", dependencies=[Depends(check_if_admin)])
def aprovar_solicitacao(id: str):
    return SolicitacaoEmpresaController().aprovarSolicitacao(id)

@router.put("/solicitacoes_empresa/{id}/desaprovar", dependencies=[Depends(check_if_admin)])
def desaprovar_solicitacao(id: str):
    return SolicitacaoEmpresaController().desaprovarSolicitacao(id)

@router.delete("/solicitacoes_empresa/{id}/recusar", dependencies=[Depends(check_if_admin)])
def recusar_solicitacao(id: str):
    return SolicitacaoEmpresaController().recusarSolicitacao(id)
