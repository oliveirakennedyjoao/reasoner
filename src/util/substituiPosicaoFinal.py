from domain.NoArvore import NoArvore

from typing import List


def substituiPosicaoFinal(cn1: List[NoArvore], cn2: List[NoArvore], sigmaFinal: List[List[int]]):
    no1 = cn1.pop()
    no2 = cn2.pop()
    paiNo1 = cn1[-1]
    paiNo2 = cn2[-1]

    tam = sum(1 for p in no1.posSubst if p is not None)

    for i in range(tam):
        par = [no1.posSubst[i], no2.posSubst[i]]

        if par[0] != par[1]:
            if len(sigmaFinal) > 0:
                for sigma in sigmaFinal:
                    if sigma[0] == no1.posSubst[i]:
                        par[0] = sigma[1]
                    elif sigma[0] == no2.posSubst[i]:
                        par[1] = sigma[1]

        if par[0] != par[1]:
            if paiNo1.tipo in ["α", "α'"]:
                par[0] = par[1]
                par[1] = no1.posSubst[i]
                sigmaFinal.append(par)
            elif paiNo2.tipo in ["α", "α'"]:
                sigmaFinal.append(par)
            else:
                return None

    return sigmaFinal
