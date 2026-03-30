from util.parser import parse_to_literal
from lib.converteeminfixa import converteEmInFixa
from util.parser import parse_to_literal
from domain.Literal import Literal
import sys
import os

# Adiciona o diretório src ao path para permitir importações diretas
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def test_converteEmInFixa():
    entrada = "(((∃h.C)⊑CO)⊓(OL⊑(∃h.A)⊓(∀h.C))|=(OL(a)⊑CO(a)))"
    saida = "(((h∃C)⊑CO)⊓(OL⊑(h∃A)⊓(h∀C))|=(OL(a)⊑CO(a)))"

    entrada_parsed = parse_to_literal(entrada)
    result = converteEmInFixa(entrada_parsed)
    expected_result = parse_to_literal(saida)

    for i in range(len(result)):
        print(
            f"Índice {i}: '{result[i].rotulo}' (posição {result[i].posicao}) vs '{expected_result[i].rotulo}' (posição {expected_result[i].posicao})")

    assert result == expected_result


def test_parse_to_literal():
    entrada = "(((∃h.C)⊑CO)⊓(OL⊑(∃h.A)⊓(∀h.C))|=(OL(a)⊑CO(a)))"
    result = parse_to_literal(entrada)

    assert len(result) == len(entrada)


test_converteEmInFixa()
