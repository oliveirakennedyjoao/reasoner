from domain.Elemento import Elemento


def buscaPosicao(matriz, idElemento):
    posicaoElemento = None

    for element in matriz:
        if not isinstance(element, Elemento):
            buscaPosicao(element, idElemento)
        else:
            if element.id == idElemento:
                posicaoElemento = element.id
                break
    return posicaoElemento
