try:
    from ..domain.Literal import Literal
except ImportError:
    from domain.Literal import Literal
from typing import List


def converteEmPosFixa(Fin: List[Literal]) -> List[Literal]:
    pilha = []
    Fpos = []
    construtores = ['|=', '⊑', '⊓', '⊔', '¬', '∃', '∀']

    for literal in Fin:
        if literal.rotulo == '(':
            pilha.append(literal)
        elif literal.rotulo not in construtores and literal.rotulo != ')':
            print(
                f"Adicionando '{literal.rotulo}' (posição {literal.posicao}) à Fpos")
            Fpos.append(literal)
        elif literal.rotulo in construtores:
            pilha.append(literal)
        elif literal.rotulo == ')':
            while (pilha and pilha[-1].rotulo != '('):
                if (pilha[-1].rotulo in construtores):
                    Fpos.append(pilha.pop())
            pilha.pop()

    return Fpos
