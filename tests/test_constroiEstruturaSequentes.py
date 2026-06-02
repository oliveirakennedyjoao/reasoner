import pytest

from domain.NoArvore import NoArvore
from lib.constroiEstruturaSequentes import constroiEstruturaSequentes


def build_ordem_reducao():
    """
    Exemplo 63 da tese (Algoritmo 9):
      ◁ = { 29, 32, 11, 8, {33,9}, 14, 21, 16, {6,26}, {13,31} }
    """
    n29 = NoArvore('|=',    29, 0, "α'")
    n32 = NoArvore('⊑',    32, 0, "α'")
    n11 = NoArvore('⊓',    11, 1, 'α')
    n8 = NoArvore('⊑',     8, 1, "β'")
    n14 = NoArvore('⊑',    14, 1, "β'")
    n21 = NoArvore('⊓',    21, 1, 'α')
    n16 = NoArvore('∃',    16, 1, 'δ')

    n33 = NoArvore('CO(a)', 33, 0, None)
    n9 = NoArvore('CO',     9, 1, None)
    n6 = NoArvore('C',      6, 0, None)
    n26 = NoArvore('C',     26, 1, None)
    n13 = NoArvore('OL',    13, 0, None)
    n31 = NoArvore('OL(a)', 31, 1, None)

    return [n29, n32, n11, n8, [n33, n9], n14, n21, n16, [n6, n26], [n13, n31]]


@pytest.fixture
def resultado():
    return constroiEstruturaSequentes(build_ordem_reducao(), [0])


def test_raiz_e_no29(resultado):
    assert resultado.posicao == 29


def test_cadeia_linear_ate_no8(resultado):
    assert resultado.filhoDireita.posicao == 32
    assert resultado.filhoDireita.filhoDireita.posicao == 11
    assert resultado.filhoDireita.filhoDireita.filhoDireita.posicao == 8


def test_beta_linha_8_ramo_direito_e_folha(resultado):
    no8 = resultado.filhoDireita.filhoDireita.filhoDireita
    assert isinstance(no8.filhoDireita, list)
    assert {n.posicao for n in no8.filhoDireita} == {33, 9}


def test_beta_linha_8_ramo_esquerdo_e_no14(resultado):
    no8 = resultado.filhoDireita.filhoDireita.filhoDireita
    assert no8.filhoEsquerda.posicao == 14


def test_beta_linha_14_ramo_direito_e_no21(resultado):
    no8 = resultado.filhoDireita.filhoDireita.filhoDireita
    assert no8.filhoEsquerda.filhoDireita.posicao == 21


def test_beta_linha_14_ramo_esquerdo_e_folha(resultado):
    no8 = resultado.filhoDireita.filhoDireita.filhoDireita
    no14 = no8.filhoEsquerda
    assert isinstance(no14.filhoEsquerda, list)
    assert {n.posicao for n in no14.filhoEsquerda} == {13, 31}


def test_no21_leva_a_no16(resultado):
    no8 = resultado.filhoDireita.filhoDireita.filhoDireita
    no21 = no8.filhoEsquerda.filhoDireita
    assert no21.filhoDireita.posicao == 16


def test_no16_leva_a_folha_6_26(resultado):
    no8 = resultado.filhoDireita.filhoDireita.filhoDireita
    no16 = no8.filhoEsquerda.filhoDireita.filhoDireita
    assert isinstance(no16.filhoDireita, list)
    assert {n.posicao for n in no16.filhoDireita} == {6, 26}


def test_guard_lista_vazia():
    assert constroiEstruturaSequentes([], [0]) is None


def test_primeiro_elemento_folha():
    n1 = NoArvore('A', 1, 0, None)
    n2 = NoArvore('B', 2, 1, None)
    resultado = constroiEstruturaSequentes([[n1, n2]], [0])
    assert isinstance(resultado, list)
    assert {n.posicao for n in resultado} == {1, 2}
