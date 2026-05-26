class Conexao:
    def __init__(self, idElemento1: int, idElemento2: int, ordem: int):
        self.idElemento1 = idElemento1
        self.idElemento2 = idElemento2
        self.ordem = ordem

    def __str__(
        self): return f"Conexao({self.idElemento1}, {self.idElemento2}, {self.ordem})"

    def __eq__(self, value):
        if isinstance(value, Conexao):
            return self.idElemento1 == value.idElemento1 and self.idElemento2 == value.idElemento2 and self.ordem == value.ordem
        return False
