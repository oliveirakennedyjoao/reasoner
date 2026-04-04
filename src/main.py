from util.parser import parse_to_literal
from lib.converteeminfixa import converteEmInFixa
from lib.converteemposfixa import converteEmPosFixa
from constants.constants import adapted_expected_Fin, adapted_expected_Fpos
import sys
import os

# Adiciona o diretório src ao path para permitir importações diretas
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def run():

    Fpos = converteEmPosFixa(adapted_expected_Fin)

    print(Fpos == adapted_expected_Fpos)


run()
