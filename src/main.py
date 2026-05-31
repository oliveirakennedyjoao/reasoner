from util.parser import parse_to_literal
from util.atualizaPosicao import atualizaPosicao
from util.imprimirArvore import imprimir_ast_completa

from lib.converteeminfixa import converteEmInFixa
from lib.converteemposfixa import converteEmPosFixa
from lib.constroiArvore import constroiArvore

from constants.constants import adapted_expected_Fin

import sys
import os

# Adiciona o diretório src ao path para permitir importações diretas
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def run():

    Fpos = converteEmPosFixa(adapted_expected_Fin)

    pos = [literal.posicao for literal in Fpos]
    pos = atualizaPosicao(adapted_expected_Fin, pos)

    index = [len(Fpos) - 1]
    inStr = 0
    inEnd = len(Fpos) - 1
    pol = 0
    arcos = [0, 0, 0, 0]
    posBetal = None
    posGDelta = None

    ast = constroiArvore(inStr, inEnd, Fpos, pol,
                         arcos, posBetal, posGDelta, pos, index)

    imprimir_ast_completa(ast, titulo="Árvore Sintática Completa - Adaptada",
                          mostrar_stats=True, mostrar_estrutura=True)


run()
