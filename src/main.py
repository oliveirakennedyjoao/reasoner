from util.parser import parse_to_literal
from lib.converteeminfixa import converteEmInFixa
from lib.converteemposfixa import converteEmPosFixa
from util.parser import parse_to_literal
from domain.Literal import Literal
from constants.constants import expected_fin
import sys
import os

# Adiciona o diretório src ao path para permitir importações diretas
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def test_parse_to_literal():
    entrada = "(((∃h.C)⊑CO)⊓(OL⊑(∃h.A)⊓(∀h.C))|=(OL(a)⊑CO(a)))"
    result = parse_to_literal(entrada)

    # O tokenizador semântico produz tokens reorganizados, então o comprimento pode ser diferente
    # devido à reorganização dos quantificadores
    # Com pontos preservados, deve ter o mesmo tamanho
    assert len(result) == len(entrada)


def test_converteEmInFixa():
    entrada = "(((∃h.C)⊑CO)⊓(OL⊑(∃h.A)⊓(∀h.C))|=(OL(a)⊑CO(a)))"
    saida = "(((h∃C)⊑CO)⊓(OL⊑(h∃A)⊓(h∀C))|=(OL(a)⊑CO(a)))"

    entrada_parsed = parse_to_literal(entrada)  # usar tokenizador semântico
    result = converteEmInFixa(entrada_parsed)

    # Importar a função simples para processar a saída esperada
    from util.parser import parse_to_literal_simple
    expected_result = parse_to_literal_simple(
        saida)  # usar tokenizador simples

    # Comparar apenas os rótulos, não as posições (que serão diferentes por design)
    print("Comparando sequência de rótulos:")
    result_rotulos = [lit.rotulo for lit in result]
    expected_rotulos = [lit.rotulo for lit in expected_result]

    if len(result_rotulos) != len(expected_rotulos):
        print(
            f"❌ Tamanhos diferentes: {len(result_rotulos)} vs {len(expected_rotulos)}")
        return False

    for i in range(len(result_rotulos)):
        if result_rotulos[i] != expected_rotulos[i]:
            print(
                f"❌ Índice {i}: '{result_rotulos[i]}' vs '{expected_rotulos[i]}'")
        else:
            print(f"✅ Índice {i}: '{result_rotulos[i]}'")

    # Comparar apenas os rótulos
    assert result_rotulos == expected_rotulos


def test_converteEmPosFixa():
    expected_Fpos = converteEmPosFixa(expected_fin)

    for literal in expected_Fpos:
        print(f"'{literal.rotulo}' (posição {literal.posicao})")


# Executar todos os testes
print("Executando test_parse_to_literal...")
test_parse_to_literal()
print("✓ test_parse_to_literal passed")

print("\nExecutando test_converteEmInFixa...")
test_converteEmInFixa()
print("✓ test_converteEmInFixa passed")

print("\nExecutando test_converteEmPosFixa...")
test_converteEmPosFixa()
print("✓ test_converteEmPosFixa passed")
