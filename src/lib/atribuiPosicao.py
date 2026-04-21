from domain.Literal import Literal
from domain.Elemento import Elemento
from util.isConstructor import isConstructor
from typing import List

"""
    Atribui posições aos elementos da matriz com base nos literais fornecidos.
    Args:
        - matriz (List[List[Elemento]]): Matriz de elementos que precisam ter suas posições atribuídas.
        - Fp (List[Literal]): Lista de literais que contêm as posições a serem atribuídas.
        - indice (int): Índice inicial para percorrer a lista de literais.
    Returns:
        - List[List[Elemento]]: Matriz atualizada com as posições atribuídas.

"""


def atribuiPosicao(matriz: List[List[Elemento]], Fp: List[Literal], indice: int):
    achou = False

    for i, lista_de_elementos in enumerate(matriz):
        if isinstance(lista_de_elementos, Elemento):
            atribuiPosicao(lista_de_elementos, Fp, indice)
        else:
            while (indice < len(Fp) or achou is True):
                if (isConstructor(Fp[indice].rotulo) is False):
                    if (Fp[indice].rotulo == matriz[i].literal):
                        matriz[i].posicao = Fp[indice].posicao
                        achou = True
                        indice += 1
                    else:
                        indice += 1
                else:
                    indice += 1

    return matriz
