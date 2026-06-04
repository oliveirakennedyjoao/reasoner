from domain.NoSequente import NoSequente
from domain.NoArvore import NoArvore

from constants import regras as REGRAS

from util.aplicaRegraLAndROr import aplicaRegraLAndROr
from util.aplicaRegraRNotAndLNotOr import aplicaRegraRNotAndLNotOr
from util.aplicaRegraLNotNotRNotNot import aplicaRegraLNotNotRNotNot
from util.aplicaRegraLOrRAnd import aplicaRegraLOrRAnd

from typing import List, Literal


def constroiSequentes(F: NoSequente, noArvore: NoArvore, noEst: NoArvore | list, lado: Literal['D', 'E', ''], regra: str | int, index: int, S: list) -> NoSequente | None:
    if index > 0:
        if regra in [REGRAS.L_AND, REGRAS.R_OR]:
            F = aplicaRegraLAndROr(F,  noEst)
        elif regra in [REGRAS.R_NOT_AND, REGRAS.L_NOT_OR]:
            F = aplicaRegraRNotAndLNotOr(F, noEst, noArvore)
        elif regra in [REGRAS.L_NOT_NOT, REGRAS.R_NOT_NOT]:
            F = aplicaRegraLNotNotRNotNot(F, noEst, noArvore)
        elif regra in [REGRAS.L_OR, REGRAS.R_AND, REGRAS.L_NOT_AND, REGRAS.R_NOT_OR]:
            F = aplicaRegraLOrRAnd(F, noEst, lado)
        elif regra in [REGRAS.R_FORALL, REGRAS.L_EXISTS, REGRAS.L_NOT_FORALL, REGRAS.R_NOT_EXISTS]:
            F = aplicaRegraRForAllLExists(F, noEst)
        elif regra == REGRAS.CUT:
            if isinstance(noEst, list):
                F = aplicaRegraCut(F, noEst, lado, S)
                return F
            else:
                j = 0
                while len(S) > 0:
                    F.Lit[j] = S.pop()
                    j += 1
    if isinstance(noEst, list):
        return None
    else:
        regra = buscaRegraSequentes(noArvore, noEst)
        while regra == 0:
            regra = buscaRegraSequentes(noArvore, noEst.filhoDireita)

    if noEst.tipo == "β'":
        if isinstance(noEst.filhoDireita, list):
            F.direita = constroiSequentes(
                F, noArvore, noEst.filhoDireita, 'D', regra, 1, S)
            F.esquerda = constroiSequentes(
                F, noArvore, noEst.filhoEsquerda, 'E', regra, 1, S)
        else:
            F.esquerda = constroiSequentes(
                F, noArvore, noEst.filhoEsquerda, 'E', regra, 1, S)
            F.direita = constroiSequentes(
                F, noArvore, noEst.filhoDireita, 'D', regra, 1, S)
    else:
        F.direita = constroiSequentes(
            F, noArvore, noEst.filhoDireita, 'D', regra, 1, S)

    if noEst.tipo == "β":
        F.esquerda = constroiSequentes(
            F, noArvore, noEst.filhoEsquerda, 'E', regra, 1, S)
    return F
