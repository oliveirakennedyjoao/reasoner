from domain.NoSequente import NoSequente
from domain.NoArvore import NoArvore
from domain.Literal import Literal

from util.buscaIndice import buscaIndice
from util.posicaoParenteses import posicaoParenteses


def aplicaRegraLAndROr(F: NoSequente, noEst: NoArvore) -> NoSequente:
    i = 0
    idx = buscaIndice(F, noEst.posicao)
    par = posicaoParenteses(F, idx)

    tam = len(F.Lit)
    auxF = []

    while i < tam:
        if i in par:
            i += 1
        elif F.Lit[i].posicao == noEst.posicao:
            auxF.append(Literal(',', noEst.posicao))
            i += 1
        else:
            auxF.append(F.Lit[i])
            i += 1

    F.Lit = auxF
    return F
