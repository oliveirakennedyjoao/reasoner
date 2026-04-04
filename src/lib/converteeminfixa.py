try:
    from ..domain.Literal import Literal
except ImportError:
    from domain.Literal import Literal

from typing import List


def converteEmInFixa(f: List[Literal]) -> List[Literal]:
    Fin = []
    quant = None
    i = 0

    for i in range(len(f)):
        if (f[i].rotulo != "∃" and f[i].rotulo != "∀" and f[i].rotulo != "."):
            Fin.append(f[i])
        elif (f[i].rotulo == "∃" or f[i].rotulo == "∀"):
            quant = f[i]
        elif (f[i].rotulo == "."):
            Fin.append(quant)

    return Fin
