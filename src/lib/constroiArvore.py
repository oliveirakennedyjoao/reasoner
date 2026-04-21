from domain.NoArvore import NoArvore
from domain.Literal import Literal
from util.buscaTipoPol import busca_tipo_pol
from typing import List

"""
Resumo da função aqui.

Args:
    Fp (List[Literal]): Array que armazena os elementos de uma fórmula dispostos na notação pós-fixa.
    pol (int): Valor inteiro (0,1) que representa a polaridade do literal. O valor inicial de pol é 0.
    arcos (List): Array de tamanho 4 com os índices para dois ramos do tipo β e β'. Arcos é inicialmente vazio.
    posBetal (int): Variável que armazena a posição de um nó do tipo β', a fim de associá-la a nós folha.
    posGDelta (int): Variável que armazena a posição de um nó do tipo γ ou δ, a fim de associá-la a nós folha.
    inStr e inEnd (int): São duas variáveis inteiras que auxiliam na identificação dos nós que são folha. Seus valores iniciais são 0 e n-1, respectivamente, onde n é o número de elementos do array Fp.

Returns:
    NoArvore: Retorna a AST na forma de uma árvore de NoArvore.
"""


def constroiArvore(inSrt: int, inEnd: int, Fp: List[Literal], pol: int, arcos: List, posBetal: int, posGDelta: int) -> NoArvore:
    no: NoArvore
    trl = [None] * 3  # trl[0] = tipo, trl[1] = polNoDir, trl[2] = polNoEsq
    posBl = posBetal
    posGD = posGDelta
    construtores = ['|=', '⊑', '⊓', '⊔', '¬', '∃', '∀']
    index = 0

    if inSrt > inEnd:
        return None
    for index in range(len(Fp)):
        if Fp[index].rotulo in construtores:
            trl = busca_tipo_pol(Fp[index].rotulo, pol)
            if trl[0] == 'β':
                arcos[0] = arcos[0] + 1
                arcos[1] = arcos[1] + 1
                no = NoArvore(Fp[index].rotulo, Fp[index].posicao,
                              pol, trl[0], arcos[0], arcos[1])
            elif trl[0] == "β'":
                arcos[2] = arcos[2] + 1
                arcos[3] = arcos[2] + 1
                posBl = Fp[index].posicao
                no = NoArvore(Fp[index].rotulo, Fp[index].posicao,
                              pol, trl[0], arcos[2], arcos[3])
            elif trl[0] == 'γ' or trl[0] == 'δ':
                posGD = Fp[index].posicao
                no = NoArvore(Fp[index].rotulo, Fp[index].posicao,
                              pol, trl[0])
            else:
                no = NoArvore(Fp[index].rotulo, Fp[index].posicao,
                              pol, trl[0])
        else:
            no = NoArvore(Fp[index].rotulo, Fp[index].posicao,
                          pol, posBl, posGD)

        m = pos[index]
        index = index - 1

        if inSrt == inEnd:
            return no

        no.filhoDir = constroiArvore(
            m + 1, inEnd, Fp, trl[1], arcos, posBl, posGD)
        no.filhoEsq = constroiArvore(
            inSrt, m - 1, Fp, trl[2], arcos, posBl, posGD)

        return no
