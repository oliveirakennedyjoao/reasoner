from domain.NoArvore import NoArvore

"""
    Verifica se um nó é um predicado, ou seja, se ele tem exatamente uma posição de substituição.
    Código adaptado.
"""


def ehPredicado(no: NoArvore) -> bool:

    return sum(1 for p in no.posSubst if p is not None) == 1
