from domain.Literal import Literal

from typing import List


class NoSequente:
    def __init__(self, Lit: List[Literal], direita: 'NoSequente | None' = None, esquerda: 'NoSequente | None' = None):
        self.Lit = Lit
        self.direita = direita
        self.esquerda = esquerda
