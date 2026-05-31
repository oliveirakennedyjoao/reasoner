from domain.NoArvore import NoArvore

from typing import List


def buscaNosTipo(tipo: str, lista: List[NoArvore]) -> List[NoArvore]:

    return list(filter(lambda no: no.tipo == tipo, lista))
