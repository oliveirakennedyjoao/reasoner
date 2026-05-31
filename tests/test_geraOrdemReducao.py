from src.constants.constants import expected_Fpos
from src.lib.constroiArvoreAdaptado import constroiArvore
from src.domain.ConexaoNo import ConexaoNo
from src.lib.geraOrdemReducao import geraOrdemReducao


def extraiPosicoes(resultado):
    posicoes = []
    for item in resultado:
        if isinstance(item, list):
            posicoes.append(frozenset(no.posicao for no in item))
        else:
            posicoes.append(item.posicao)
    return posicoes


def test_geraOrdemReducao():
    raiz = constroiArvore(expected_Fpos, 0, [0, 0, 0, 0], 0, 0)
    conexoes = [
        ConexaoNo(33, 9, 1),
        ConexaoNo(6, 26, 2),
        ConexaoNo(24, 17, 3),
        ConexaoNo(13, 31, 4),
        ConexaoNo(4, 17, 5),
    ]
    resultado = geraOrdemReducao(conexoes, raiz)
    esperado = [17, 15, 11, 3, frozenset({18, 4}), 7, 5, 9, frozenset({
        2, 14}), frozenset({6, 16})]
    assert extraiPosicoes(resultado) == esperado
