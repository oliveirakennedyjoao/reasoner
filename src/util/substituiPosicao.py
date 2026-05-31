from domain.NoArvore import NoArvore

from typing import List


def substituiPosicao(no1: NoArvore, no2: NoArvore, sigmaFinal: List[List[int]]) -> List[List[int]]:
    par = [no1.posicao, no2.posicao]

    if len(sigmaFinal) != 0:
        for sigma in sigmaFinal:
            if sigma[0] == no2.posicao:
                par[1] = sigma[1]

    sigmaFinal.append(par)
    return sigmaFinal
