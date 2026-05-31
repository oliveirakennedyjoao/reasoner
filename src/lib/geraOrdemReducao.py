from domain.ConexaoNo import ConexaoNo
from domain.NoArvore import NoArvore

from util.buscaCaminho import buscaCaminho

from typing import List


def geraOrdemReducao(conexoes: List[ConexaoNo], noRaiz: NoArvore) -> List[NoArvore]:
    R = []
    P = []

    for conexao in conexoes:
        cn1 = buscaCaminho(noRaiz, conexao.posicao1, [])
        cn2 = buscaCaminho(noRaiz, conexao.posicao2, [])

        for z, cn in enumerate([cn1, cn2], start=1):
            continua = True
            conectar = False
            j = 0
            while continua:
                if cn[j].tipo == None:
                    P.append(cn[j])
                    continua = False

                    if z == 2:
                        conectar = True
                else:
                    if cn[j] not in R:
                        # executar algoritmo 7
                        j += 1
                    else:
                        j += 1
        if conectar:
            # executar algoritmo 8
            pass

    return P
