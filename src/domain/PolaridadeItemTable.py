{tipo: "α", conectivo: "⊓", polaridade: 1, polNoEsq: 1, polNoDir: 1},
{tipo: "α", conectivo: "⊔", polaridade: 0, polNoEsq: 1, polNoDir: 0},
{tipo: "α", conectivo: "¬", polaridade: 1, polNoEsq: None, polNoDir: 0},
{tipo: "α", conectivo: "¬", polaridade: 0, polNoEsq: None, polNoDir: 1},
{tipo: "α'", conectivo: "⊑", polaridade: 0, polNoEsq: 1, polNoDir: 0},
{tipo: "α'", conectivo: "|=", polaridade: 0, polNoEsq: 1, polNoDir: 0},
{tipo: "β'", conectivo: "⊑", polaridade: 1, polNoEsq: 0, polNoDir: 1},
{tipo: "β", conectivo: "⊓", polaridade: 0, polNoEsq: 0, polNoDir: 0},
{tipo: "β", conectivo: "⊔", polaridade: 1, polNoEsq: 1, polNoDir: 1},
{tipo: "δ", conectivo: "∀", polaridade: 0, polNoEsq: 1, polNoDir: 0},
{tipo: "δ", conectivo: "∃", polaridade: 1, polNoEsq: 1, polNoDir: 1},
{tipo: "γ", conectivo: "∀", polaridade: 1, polNoEsq: 0, polNoDir: 1},
{tipo: "γ", conectivo: "∃", polaridade: 0, polNoEsq: 0, polNoDir: 0}


class PolaridadeItemTable:
    def __init__(self, tipo: {"α" | "α'" | "β" | "β'" | "γ" | "δ"}, conectivo: {"⊓" | "⊔" | "¬" | "⊑" | "|=" | "∀" | "∃"}, polaridade: {0 | 1}, polNoEsq: {0 | 1 | None}, polNoDir: {0 | 1 | None}):
        self.tipo = tipo
        self.conectivo = conectivo
        self.polaridade = polaridade
        self.polNoEsq = polNoEsq
        self.polNoDir = polNoDir
