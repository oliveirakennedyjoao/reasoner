try:
    from ..domain.Literal import Literal
except ImportError:
    from domain.Literal import Literal

try:
    from .tokenizer import tokenize
except ImportError:
    from tokenizer import tokenize


def parse_to_literal(expression: str) -> list[Literal]:
    tokenized_expression = tokenize(expression)

    literals = []

    for i in range(len(tokenized_expression)):
        print(
            f"Creating Literal with rotulo='{tokenized_expression[i]}' and posicao={i}")
        literals.append(Literal(tokenized_expression[i], i))

    return literals
