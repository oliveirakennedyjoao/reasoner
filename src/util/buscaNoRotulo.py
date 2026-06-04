from domain.NoArvore import NoArvore


def buscaNoRotulo(rotulo: str, caminho: list[NoArvore]) -> NoArvore:
    achou = False
    i = 0
    tam = len(caminho)

    while i <= tam - 2 and not achou:
        if caminho[i].rotulo == rotulo:
            achou = True
        else:
            i += 1
    return caminho[i]
