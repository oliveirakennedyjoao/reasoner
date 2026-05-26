import pytest
from lib.buscaConexao import buscaConexao
from domain.Elemento import Elemento
from domain.Conexao import Conexao


def build_matrix():
    """
    Matriz do exemplo da tese (p.58) com posições e conexões atribuídas.

    Entrada (conforme imagem):
      {1,h,0,4,5}, {2,C,0,6,2}, {3,CO,1,9,1}
      {4,OL,0,13,4}, {5,h,1,17,{3,5}}, {6,A,1,19,null}, {7,h,0,24,3}, {8,C,1,26,2}
      {9,OL(a),1,31,4}, {10,CO(a),0,33,1}
    """
    e1  = Elemento(1,  'h',      0, 4)
    e2  = Elemento(2,  'C',      0, 6)
    e3  = Elemento(3,  'CO',     1, 9)
    e4  = Elemento(4,  'OL',     0, 13)
    e5  = Elemento(5,  'h',      1, 17)
    e6  = Elemento(6,  'A',      1, 19)
    e7  = Elemento(7,  'h',      0, 24)
    e8  = Elemento(8,  'C',      1, 26)
    e9  = Elemento(9,  'OL(a)', 1, 31)
    e10 = Elemento(10, 'CO(a)', 0, 33)

    e1.conexoes  = [Conexao(1,  5, 5)]
    e2.conexoes  = [Conexao(2,  8, 2)]
    e3.conexoes  = [Conexao(10, 3, 1)]
    e4.conexoes  = [Conexao(4,  9, 4)]
    e5.conexoes  = [Conexao(7,  5, 3), Conexao(1, 5, 5)]
    e6.conexoes  = None
    e7.conexoes  = [Conexao(7,  5, 3)]
    e8.conexoes  = [Conexao(2,  8, 2)]
    e9.conexoes  = [Conexao(4,  9, 4)]
    e10.conexoes = [Conexao(10, 3, 1)]

    return [
        [e1, e2, e3],
        [e4, e5, e6, e7, e8],
        [e9, e10],
    ]


def run_busca():
    m = build_matrix()
    conexoes = [Conexao(0, 0, 0) for _ in range(5)]
    return buscaConexao(m, conexoes, 0)


@pytest.fixture
def resultado():
    return run_busca()


def test_retorna_5_conexoes(resultado):
    assert len(resultado) == 5


def test_resultado_ordenado_por_ordem(resultado):
    ordens = [c.ordem for c in resultado]
    assert ordens == sorted(ordens)


def test_conexao_ordem_1(resultado):
    c = next(c for c in resultado if c.ordem == 1)
    assert c.posicao1 == 33  # CO(a)
    assert c.posicao2 == 9   # CO


def test_conexao_ordem_2(resultado):
    c = next(c for c in resultado if c.ordem == 2)
    assert c.posicao1 == 6   # C
    assert c.posicao2 == 26  # C


def test_conexao_ordem_3(resultado):
    c = next(c for c in resultado if c.ordem == 3)
    assert c.posicao1 == 24  # h
    assert c.posicao2 == 17  # h


def test_conexao_ordem_4(resultado):
    c = next(c for c in resultado if c.ordem == 4)
    assert c.posicao1 == 13  # OL
    assert c.posicao2 == 31  # OL(a)


def test_conexao_ordem_5(resultado):
    c = next(c for c in resultado if c.ordem == 5)
    assert c.posicao1 == 4   # h
    assert c.posicao2 == 17  # h
