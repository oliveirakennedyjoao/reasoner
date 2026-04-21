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

"""
Função que recebe o rótulo e polaridade de um nó (conectivo) e retorna o tipo do nó e a polaridade de seus filhos.

Args:
    conectivo (str): Rótulo do nó (conectivo).
    polaridade (int): Polaridade do nó (0 ou 1).

Returns:
    PolaridadeItemTable: Objeto contendo o tipo do nó e a polaridade de seus filhos.
"""


def busca_tipo_pol(conectivo, polaridade):
    for item in tiposEPolaridades:
        if item.conectivo == conectivo and item.polaridade == polaridade:
            return item
    return None
