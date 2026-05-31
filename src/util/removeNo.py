from domain.NoArvore import NoArvore

from typing import List


def removeNo(no: NoArvore, lista: List[NoArvore]) -> List[NoArvore]:

    return list(filter(lambda noLista: noLista != no, lista))
