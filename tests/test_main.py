from src.lib.converteeminfixa import converteEmInFixa
from src.domain.Literal import Literal
from src.util.parser import parse_to_literal
from src.constants.constants import expression, expected_Fin
from src.util.tokenizer import tokenize
from src.lib.converteemposfixa import converteEmPosFixa


def test_converteEmInFixa():
    F = parse_to_literal(expression)
    result = converteEmInFixa(F)

    assert result == expected_Fin
