from src.util.tokenizer import tokenize
from src.constants.constants import expression, tokenized_expression

# expression == "(((∃h.C)⊑CO)⊓(OL⊑(∃h.A)⊓(∀h.C))|=(OL(a)⊑CO(a)))"


def test_tokenize():

    tokens = tokenize(expression)

    assert tokens == tokenized_expression
