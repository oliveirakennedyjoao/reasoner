from src.constants.constants import expression, expected_F
from src.util.parser import parse_to_literal


def test_parse_to_literal():

    literals = parse_to_literal(expression)

    assert literals == expected_F
