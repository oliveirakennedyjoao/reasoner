from domain.Literal import Literal
from domain.Elemento import Elemento
from util.isConstructor import isConstructor
from typing import List


def atribuiPosicao(matriz: List, Fp: List[Literal], indice: int = 0) -> int:
    """
    Atribui posições aos elementos da matriz com base nos literais da fórmula pós-fixa.

    Args:
        matriz: matriz de prova (lista aninhada de Elemento).
        Fp: fórmula em notação pós-fixa (lista de Literal).
        indice: posição atual em Fp (usado internamente nas chamadas recursivas).

    Returns:
        int: índice atualizado em Fp após processar esta sub-matriz.
        A matriz é modificada in-place (posicao de cada Elemento é preenchida).
    """
    for item in matriz:
        if not isinstance(item, Elemento):
            indice = atribuiPosicao(item, Fp, indice)
        else:
            achou = False
            while indice < len(Fp) and not achou:
                if not isConstructor(Fp[indice].rotulo):
                    if Fp[indice].rotulo == item.literal:
                        item.posicao = Fp[indice].posicao
                        achou = True
                    indice += 1
                else:
                    indice += 1
    return indice
