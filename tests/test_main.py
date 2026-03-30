from src.lib.converteeminfixa import converteEmInFixa
from src.domain.Literal import Literal
from src.util.parser import parse_to_literal


def test_parse_to_literal():
    entrada = "(((∃h.C)⊑CO)⊓(OL⊑(∃h.A)⊓(∀h.C))|=(OL(a)⊑CO(a)))"
    result = parse_to_literal(entrada)

    print("Testing parse_to_literal with input:", entrada)

    for i in range(len(result)):
        print(result[i].rotulo, result[i].posicao)

    print("Finished testing parse_to_literal with output:",
          [(lit.rotulo, lit.posicao) for lit in result])

    assert len(result) == len(entrada)


def test_converteEmInFixa():
    entrada = "(((∃h.C)⊑CO)⊓(OL⊑(∃h.A)⊓(∀h.C))|=(OL(a)⊑CO(a)))"
    saida = "(((h∃C)⊑CO)⊓(OL⊑(h∃A)⊓(h∀C))|=(OL(a)⊑CO(a)))"

    result = converteEmInFixa(entrada)

    assert result == saida
