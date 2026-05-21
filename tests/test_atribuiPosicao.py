from src.constants.constants import expected_Fpos
from src.constants.matrix import build_matrix
from src.lib.atribuiPosicao import atribuiPosicao


def test_sub_matriz_1():
    m = build_matrix()
    atribuiPosicao(m, expected_Fpos)
    assert m[0][0].posicao == 4   # h
    assert m[0][1].posicao == 6   # C
    assert m[0][2].posicao == 9   # CO


def test_sub_matriz_2():
    m = build_matrix()
    atribuiPosicao(m, expected_Fpos)
    assert m[1][0].posicao == 13  # OL
    assert m[1][1].posicao == 17  # h
    assert m[1][2].posicao == 19  # A
    assert m[1][3].posicao == 24  # h
    assert m[1][4].posicao == 26  # C


def test_sub_matriz_3():
    m = build_matrix()
    atribuiPosicao(m, expected_Fpos)
    assert m[2][0].posicao == 31  # OL(a)
    assert m[2][1].posicao == 33  # CO(a)


def test_todos_elementos_recebem_posicao():
    m = build_matrix()
    atribuiPosicao(m, expected_Fpos)
    for sub in m:
        for elem in sub:
            assert elem.posicao is not None
