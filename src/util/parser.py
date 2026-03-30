try:
    from ..domain.Literal import Literal
except ImportError:
    from domain.Literal import Literal


def parse_to_literal(expression: str) -> list[Literal]:
    literals = []

    print("Parsing expression:", expression)

    for i in range(len(expression)):
        literals.append(Literal(expression[i], i))

    return literals
