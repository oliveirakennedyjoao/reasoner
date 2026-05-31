from src.constants.constants import expected_Fpos, expected_Fin
from lib.constroiArvore import constroiArvore
from src.domain.ConexaoNo import ConexaoNo
from src.lib.geraOrdemReducao import geraOrdemReducao
from src.util.atualizaPosicao import atualizaPosicao


def extraiPosicoes(resultado, pos_map):
    posicoes = set()
    for item in resultado:
        if isinstance(item, list):
            posicoes.add(frozenset(pos_map[no.posicao] for no in item))
        else:
            posicoes.add(pos_map[item.posicao])
    return posicoes


def test_geraOrdemReducao():

    pos = [literal.posicao for literal in expected_Fpos]
    pos = atualizaPosicao(expected_Fin, pos)
    n = len(expected_Fpos)
    index = [n - 1]

    raiz = constroiArvore(0, n - 1, expected_Fpos, 0,
                          [0, 0, 0, 0], 0, None, pos, index)
    conexoes = [
        ConexaoNo(33, 9, 1),
        ConexaoNo(6, 26, 2),
        ConexaoNo(24, 17, 3),
        ConexaoNo(13, 31, 4),
        ConexaoNo(4, 17, 5),
    ]
    pos_map = {expected_Fpos[i].posicao: pos[i] for i in range(n)}
    resultado = geraOrdemReducao(conexoes, raiz)
    esperado = {17, 15, 11, 3, frozenset({18, 4}), 7, 5, 9, frozenset({
        2, 14}), frozenset({6, 16})}
    assert extraiPosicoes(resultado, pos_map) == esperado
