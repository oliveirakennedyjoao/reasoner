from constants.tiposEPolaridadesTable import tiposEPolaridades


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
