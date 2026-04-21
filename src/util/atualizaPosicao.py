from domain.Literal import Literal
from typing import List


def atualizaPosicao(F: List[Literal]) -> List[Literal]:
    index: int = 0
    j: int = None
    pos: List[Literal] = []

    for literal in F:
        if literal.rotulo is not '(' and literal.rotulo is not ')':
            index = index + 1
            j = 0
            while j < len(F):
                j = j + 1
                if pos[j] == literal.posicao:
                    pos[j] = index - 1
                    j = len(pos)

    return F
