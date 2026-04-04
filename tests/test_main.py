from src.lib.converteeminfixa import converteEmInFixa
from src.domain.Literal import Literal
from src.util.parser import parse_to_literal
from src.constants.constants import expression, expected_Fin, expected_Fpos
from src.util.tokenizer import tokenize
from src.lib.converteemposfixa import converteEmPosFixa


def test_converteEmInFixa():
    F = parse_to_literal(expression)
    result = converteEmInFixa(F)

    assert result == expected_Fin


def test_converteEmPosFixa():
    result = converteEmPosFixa(expected_Fin)

    print(len(result))
    print(len(expected_Fpos))

    for i in range(len(result)):
        print(
            f"result[{i}]: {result[i].rotulo} (posicao: {result[i].posicao})")
        print(
            f"expected_Fpos[{i}]: {expected_Fpos[i].rotulo} (posicao: {expected_Fpos[i].posicao})")

    assert result == expected_Fpos
