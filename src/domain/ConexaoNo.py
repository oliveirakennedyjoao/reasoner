class ConexaoNo:
    def __init__(self, posicao1: int, posicao2: int, ordem: int):
        self.posicao1 = posicao1
        self.posicao2 = posicao2
        self.ordem = ordem

    def __str__(self):
        return f"ConexaoNo({self.posicao1}, {self.posicao2}, {self.ordem})"

    def __eq__(self, value):
        if isinstance(value, ConexaoNo):
            return self.posicao1 == value.posicao1 and self.posicao2 == value.posicao2 and self.ordem == value.ordem
        return False
