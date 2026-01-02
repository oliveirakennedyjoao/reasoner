class Literal:
    def __init__(self, posicao: int, rotulo: bool = False):
        self.posicao = posicao
        self.rotulo = rotulo

    def __repr__(self):
        return f"¬{self.posicao}" if self.rotulo else self.posicao