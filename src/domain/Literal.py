class Literal:
    # O método __init__ é o construtor da classe
    def __init__(self, rotulo, posicao):
        self.rotulo = rotulo    # Atributo de instância
        self.posicao = posicao  # Atributo de instância

    def __eq__(self, value):
        if isinstance(value, Literal):
            return self.rotulo == value.rotulo and self.posicao == value.posicao
        return False
