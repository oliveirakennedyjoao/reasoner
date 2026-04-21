from domain.Literal import Literal
from typing import List

"""
    Atualiza as posições dos literais em uma fórmula disposta na notação infixa.
    Args:
    - Fin (List[Literal]): Array que armazena os elementos de uma fórmula dispostos na notação infixa.
    - pos (List[int]): Array que armazena as posições dos literais. Inicialmente vazio.

    Returns:
        List[int]: Retorna o array de posições atualizado.
"""


def atualizaPosicao(Fin: List[Literal], pos: List[int]) -> List[int]:
    index: int = 0

    for literal in Fin:
        # print(f"Literal: {literal.rotulo}, Posição: {literal.posicao}")
        if literal.rotulo != '(' and literal.rotulo != ')':
            index = index + 1
            j = 0
            while j < len(pos):
                j = j + 1
                if pos[j] == literal.posicao:
                    pos[j] = index - 1
                    j = len(pos)

    return pos
