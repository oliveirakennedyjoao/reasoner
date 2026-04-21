from util.parser import parse_to_literal
from util.atualizaPosicao import atualizaPosicao
from util.imprimirArvore import imprimir_ast_completa
from lib.converteeminfixa import converteEmInFixa
from lib.converteemposfixa import converteEmPosFixa
from lib.constroiArvoreAdaptado import constroiArvore
from constants.constants import adapted_expected_Fin, adapted_expected_Fpos
import sys
import os

# Adiciona o diretório src ao path para permitir importações diretas
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def run():

    pos = [literal.posicao for literal in adapted_expected_Fin]

    pos = atualizaPosicao(adapted_expected_Fin, pos)
    Fpos = converteEmPosFixa(adapted_expected_Fin)

    # 🔍 DEBUG: Ver o que está sendo processado
    print("=== DEBUG: FÓRMULA PÓS-FIXA ===")
    for i, literal in enumerate(Fpos):
        print(f"[{i}] {literal.rotulo} (pos: {literal.posicao})")
    print(f"Total: {len(Fpos)} elementos\n")

    ast = constroiArvore(Fpos, 0, [0, 0, 0, 0], 0, 0)

    imprimir_ast_completa(ast, titulo="Árvore Sintática Completa - Adaptada",
                          mostrar_stats=True, mostrar_estrutura=True)


run()
