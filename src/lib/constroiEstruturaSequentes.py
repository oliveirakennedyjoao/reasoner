from domain.NoArvore import NoArvore

from typing import List


def constroiEstruturaSequentes(ordemReducao: List, idx: list) -> NoArvore | list | None:
    if idx[0] >= len(ordemReducao):
        return None

    i = idx[0]
    idx[0] += 1

    if isinstance(ordemReducao[i], list):
        return ordemReducao[i]
    else:
        noEst: NoArvore = ordemReducao[i]
        noEst.filhoDireita = constroiEstruturaSequentes(ordemReducao, idx)
        if noEst.tipo in ["β", "β'"]:
            noEst.filhoEsquerda = constroiEstruturaSequentes(ordemReducao, idx)
        return noEst
