from util.tokenizer import tokenize
from domain.Literal import Literal


def parse_to_literal(expression: str) -> list[Literal]:
    tokenized_expression = tokenize(expression)

    literals = []

    for i in range(len(tokenized_expression)):
        literals.append(Literal(tokenized_expression[i], i))

    return literals
