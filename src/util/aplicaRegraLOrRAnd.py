from domain.NoSequente import NoSequente
from domain.NoArvore import NoArvore

from util.buscaIndice import buscaIndice
from util.posicaoParenteses import posicaoParenteses

from typing import Literal


def aplicaRegraLOrRAnd(F: NoSequente, noEst: NoArvore, lado: Literal['D', 'E', '']) -> NoSequente:
    i = 0
    idx = buscaIndice(F, noEst.posicao)
    par = posicaoParenteses(F, idx)

    if lado == 'D':
        tam = len(F.Lit)
        auxF = []

        while i < tam:
            if i >= par[0] and i <= idx or i == par[1]:
                i += 1
            else:
                auxF.append(F.Lit[i])
                i += 1

    if lado == 'E':
        tam = len(F.Lit)
        auxF = []

        while i < tam:
            if i >= idx and i <= par[1] or i == par[0]:
                i += 1
            else:
                auxF.append(F.Lit[i])
                i += 1
    F.Lit = auxF
    return F
