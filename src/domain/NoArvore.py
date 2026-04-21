class NoArvore:
    def __init__(self, rotulo, posicao, polaridade, tipo, posBl=None, posGD=None):
        self.rotulo = rotulo
        self.posicao = posicao
        self.polaridade = polaridade
        self.tipo = tipo
        self.posSubst = [posBl, posGD]
        self.filhoDireita = None
        self.filhoEsquerda = None
