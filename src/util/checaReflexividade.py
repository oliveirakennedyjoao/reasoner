from domain.NoArvore import NoArvore

from typing import List


def checaReflexividade(ordemReducao: List[NoArvore]) -> bool:
    resp = 0
    tamanho = len(ordemReducao)
    for i in range(tamanho):
        for j in range(i + 1, tamanho):
            if isinstance(ordemReducao[i], list) or isinstance(ordemReducao[j], list):
                continue
            if ordemReducao[i].posicao == ordemReducao[j].posicao:
                resp = 1

    return resp > 0
