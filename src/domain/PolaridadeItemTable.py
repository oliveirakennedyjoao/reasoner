

class PolaridadeItemTable:
    def __init__(self, tipo: {"α" | "α'" | "β" | "β'" | "γ" | "δ"}, conectivo: {"⊓" | "⊔" | "¬" | "⊑" | "|=" | "∀" | "∃"}, polaridade: {0 | 1}, polNoEsq: {0 | 1 | None}, polNoDir: {0 | 1 | None}):
        self.tipo = tipo
        self.conectivo = conectivo
        self.polaridade = polaridade
        self.polNoEsq = polNoEsq
        self.polNoDir = polNoDir
