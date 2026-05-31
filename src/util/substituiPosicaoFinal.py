from domain.NoArvore import NoArvore

from typing import List


def substituiPosicaoFinal(cn1: List[NoArvore], cn2: List[NoArvore], sigmaFinal: List[List[int]]):
    no1 = cn1.pop()
    no2 = cn2.pop()
    paiNo1 = cn1[-1]
    paiNo2 = cn2[-1]

    no1_vals = [p for p in no1.posSubst if p is not None]
    no2_vals = [p for p in no2.posSubst if p is not None]
    tam = len(no1_vals)

    for i in range(tam):
        par = [no1_vals[i], no2_vals[i] if i < len(no2_vals) else None]

        if par[0] != par[1]:
            if len(sigmaFinal) > 0:
                alterado = True
                while alterado:
                    alterado = False
                    for sigma in sigmaFinal:
                        if sigma[0] == par[0] and par[0] != sigma[1]:
                            par[0] = sigma[1]
                            alterado = True
                        elif sigma[0] == par[1] and par[1] != sigma[1]:
                            par[1] = sigma[1]
                            alterado = True

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
