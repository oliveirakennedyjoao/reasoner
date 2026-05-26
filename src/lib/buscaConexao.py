from domain.Conexao import Conexao
from domain.Elemento import Elemento
from util.constaConexao import constaConexao
from util.ordenaConexao import ordenaConexao
from util.buscaPosicao import buscaPosicao

"""
    Busca conexões entre elementos de uma matriz de conexões.

    Args:
        matriz: matriz de conexões (lista aninhada de Conexao).
    Returns:
        lista de conexões encontradas (lista de Conexao).
"""


def buscaConexao(matriz, conexoes: list[Conexao], indice: int, _raiz=None):
    is_top = _raiz is None
    if is_top:
        _raiz = matriz
    for element in matriz:
        if not isinstance(element, Elemento):
            indice = buscaConexao(element, conexoes, indice, _raiz)
        else:
            if element.conexoes is not None:
                for conexao in element.conexoes:
                    if not constaConexao(conexoes, conexao.ordem):
                        if element.id == conexao.idElemento1:
                            conexoes[indice].posicao1 = element.posicao
                            conexoes[indice].posicao2 = buscaPosicao(_raiz, conexao.idElemento2)
                        else:
                            conexoes[indice].posicao2 = element.posicao
                            conexoes[indice].posicao1 = buscaPosicao(_raiz, conexao.idElemento1)
                        conexoes[indice].ordem = conexao.ordem
                        indice += 1
    if is_top:
        return ordenaConexao(conexoes)
    return indice
