from typing import Optional


class Elemento:
    def __init__(self, id: int, literal: str, polaridade: int, posicao: Optional[int] = None):
        self.id = id
        self.literal = literal
        self.polaridade = polaridade
        self.posicao = posicao
        self.conexoes = []
