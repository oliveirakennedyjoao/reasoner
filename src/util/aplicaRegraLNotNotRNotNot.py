from domain.NoSequente import NoSequente
from domain.NoArvore import NoArvore

from util.buscaCaminho import buscaCaminho
from util.buscaNoRotulo import buscaNoRotulo


def aplicaRegraLNotNotRNotNot(F: NoSequente, noEst: NoArvore, noArvore: NoArvore) -> NoSequente:
    cn1 = buscaCaminho(noArvore, noEst.posicao, [])
    noNeg = buscaNoRotulo("¬", cn1)

    tam = len(F.Lit)
    auxF = []

    for i in range(tam):
        # Corrigido - tese diz "=="
        if F.Lit[i].posicao != noNeg.posicao and F.Lit[i].posicao != noEst.posicao:
            auxF.append(F.Lit[i])
    F.Lit = auxF
    return F
