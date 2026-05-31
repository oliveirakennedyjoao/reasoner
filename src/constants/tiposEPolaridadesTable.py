from domain.PolaridadeItemTable import PolaridadeItemTable

from typing import List

tiposEPolaridades: List[PolaridadeItemTable] = [
    PolaridadeItemTable(tipo="α", conectivo="⊓",
                        polaridade=1, polNoEsq=1, polNoDir=1),
    PolaridadeItemTable(tipo="α", conectivo="⊔",
                        polaridade=0, polNoEsq=1, polNoDir=0),
    PolaridadeItemTable(tipo="α", conectivo="¬",
                        polaridade=1, polNoEsq=None, polNoDir=0),
    PolaridadeItemTable(tipo="α", conectivo="¬",
                        polaridade=0, polNoEsq=None, polNoDir=1),
    PolaridadeItemTable(tipo="α'", conectivo="⊑",
                        polaridade=0, polNoEsq=1, polNoDir=0),
    PolaridadeItemTable(tipo="α'", conectivo="|=",
                        polaridade=0, polNoEsq=1, polNoDir=0),
    PolaridadeItemTable(tipo="β'", conectivo="⊑",
                        polaridade=1, polNoEsq=0, polNoDir=1),
    PolaridadeItemTable(tipo="β", conectivo="⊓",
                        polaridade=0, polNoEsq=0, polNoDir=0),
    PolaridadeItemTable(tipo="β", conectivo="⊔",
                        polaridade=1, polNoEsq=1, polNoDir=1),
    PolaridadeItemTable(tipo="δ", conectivo="∀",
                        polaridade=0, polNoEsq=1, polNoDir=0),
    PolaridadeItemTable(tipo="δ", conectivo="∃",
                        polaridade=1, polNoEsq=1, polNoDir=1),
    PolaridadeItemTable(tipo="γ", conectivo="∀",
                        polaridade=1, polNoEsq=0, polNoDir=1),
    PolaridadeItemTable(tipo="γ", conectivo="∃",
                        polaridade=0, polNoEsq=0, polNoDir=0)
]
