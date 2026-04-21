from domain.Literal import Literal


class Elemento:
    def __init__(self, id: int, literal: Literal, polaridade: int, posicao: int):
        self.id = id
        self.literal = literal
        self.polaridade = polaridade
        self.posicao = posicao
        self.conexoes = []
