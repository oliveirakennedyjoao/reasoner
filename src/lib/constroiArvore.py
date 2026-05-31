from constants.constructors import construtores

from domain.NoArvore import NoArvore
from domain.Literal import Literal
from util.buscaTipoPol import busca_tipo_pol
from typing import List

"""
Resumo da função aqui.

Args:
    - Fp (List[Literal]): Array que armazena os elementos de uma fórmula dispostos na notação pós-fixa.
    - pol (int): Valor inteiro (0,1) que representa a polaridade do literal. O valor inicial de pol é 0.
    - arcos (List): Array de tamanho 4 com os índices para dois ramos do tipo β e β'. Arcos é inicialmente vazio.
    - posBetal (int): Variável que armazena a posição de um nó do tipo β', a fim de associá-la a nós folha.
    - posGDelta (int): Variável que armazena a posição de um nó do tipo γ ou δ, a fim de associá-la a nós folha.

Returns:
    NoArvore: Retorna a AST na forma de uma árvore de NoArvore.
"""

# pos é resultado da funcao atribuiPosicao, vai estar declarado no main.
# index é global.
# inStr é 0
# inEnd é o tamanho do array Fp - 1


def constroiArvore(inStr: int, inEnd: int, Fp: List[Literal], pol: int, arcos: List, posBetal: int, posGDelta: int, pos, index) -> NoArvore:
    noRaiz: NoArvore
    trl = None
    posBl = posBetal
    posGd = posGDelta

    if inStr > inEnd:
        return None

    if Fp[index[0]].rotulo in construtores:
        trl = busca_tipo_pol(Fp[index[0]].rotulo, pol)

        if trl.tipo == "β":
            arcos[0] = arcos[0] + 1
            arcos[1] = arcos[0] + 1
            noRaiz = NoArvore(Fp[index[0]].rotulo,
                              Fp[index[0]].posicao,
                              pol,
                              trl.tipo, arcos[0], arcos[1])

        elif trl.tipo == "β'":
            arcos[2] = arcos[2] + 1
            arcos[3] = arcos[2] + 1
            posBl = Fp[index[0]].posicao
            noRaiz = NoArvore(Fp[index[0]].rotulo,
                              Fp[index[0]].posicao,
                              pol, trl.tipo, arcos[2], arcos[3])

        elif trl.tipo == "γ" or trl.tipo == "δ":
            posGd = Fp[index[0]].posicao
            noRaiz = NoArvore(Fp[index[0]].rotulo,
                              Fp[index[0]].posicao,
                              pol, trl.tipo, None, None)
        else:
            noRaiz = NoArvore(Fp[index[0]].rotulo,
                              Fp[index[0]].posicao,
                              pol, trl.tipo, None, None)
    else:
        noRaiz = NoArvore(Fp[index[0]].rotulo,
                          Fp[index[0]].posicao,
                          pol, None, posBl, posGd)
    m = pos[index[0]]
    index[0] = index[0] - 1

    if inStr == inEnd:
        return noRaiz

    if trl is not None and (trl.tipo == "γ" or trl.tipo == "δ"):
        noRaiz.filhoDireita = constroiArvore(
            m + 1, inEnd, Fp, trl.polNoDir, arcos, None, posGd, pos, index)
        noRaiz.filhoEsquerda = constroiArvore(
            inStr, m - 1, Fp, trl.polNoEsq, arcos, posBl, posGd, pos, index)
    else:
        noRaiz.filhoDireita = constroiArvore(
            m + 1, inEnd, Fp, trl.polNoDir, arcos, posBl, posGd, pos, index)
        noRaiz.filhoEsquerda = constroiArvore(
            inStr, m - 1, Fp, trl.polNoEsq, arcos, posBl, posGd, pos, index)

    return noRaiz
