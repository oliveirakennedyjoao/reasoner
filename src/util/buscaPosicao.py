from domain.Elemento import Elemento


def buscaPosicao(matriz, idElemento):
    posicaoElemento = None

    for element in matriz:
        if not isinstance(element, Elemento):
            result = buscaPosicao(element, idElemento)
            if result is not None:
                return result
        else:
            if element.id == idElemento:
                posicaoElemento = element.posicao
                break
    return posicaoElemento
