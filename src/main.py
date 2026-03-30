from util.parser import parse_to_literal
from lib.converteeminfixa import converteEmInFixa
from domain.Literal import Literal
import sys
import os

# Adiciona o diretório src ao path para permitir importações diretas
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def test_converteEmInFixa():
    entrada = "(((∃h.C)⊑CO)⊓(OL⊑(∃h.A)⊓(∀h.C))|=(OL(a)⊑CO(a)))"
    saida = "(((h∃C)⊑CO)⊓(OL⊑(h∃A)⊓(h∀C))|=(OL(a)⊑CO(a)))"

    result = converteEmInFixa(entrada)

    assert result == saida


def test_parse_to_literal():
    entrada = "(((∃h.C)⊑CO)⊓(OL⊑(∃h.A)⊓(∀h.C))|=(OL(a)⊑CO(a)))"
    result = parse_to_literal(entrada)

    for i in range(len(result)):
        print(result[i].rotulo, result[i].posicao)

    assert len(result) == len(entrada)


test_parse_to_literal()
