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


def buscaConexao(matriz, conexoes: list[Conexao], indice: int):
    for element in matriz:
        if isinstance(element, Elemento):
            buscaConexao(element, conexoes, indice)
        else:
            if element.conexoes is not None:
                for conexao in element.conexoes:
                    if not constaConexao(conexoes, conexao.ordem):
                        if (element.id == conexao.idElemento1):
                            # revisar essa parte
                            # aqui deveria ser a posição do elemento, não o id (revisar isso depois)
                            conexoes[indice].posicao1 = element.id
                            conexoes[indice].posicao2 = buscaPosicao(
                                conexao.idElemento2)
                        else:
                            # aqui deveria ser a posição do elemento, não o id (revisar isso depois)
                            conexoes[indice].posicao2 = element.id
                            conexoes[indice].posicao1 = buscaPosicao(
                                conexao.idElemento1)
                        conexoes[indice].ordem = conexao.ordem
                        indice += 1
    return ordenaConexao(conexoes)
