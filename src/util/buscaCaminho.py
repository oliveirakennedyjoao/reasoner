from domain.NoArvore import NoArvore


def buscaCaminho(no: NoArvore, posicao: int, caminho: list[NoArvore]):
    noNulo: NoArvore = NoArvore(None, -1, None, None)

    if no is None:
        caminho.append(noNulo)
        return caminho
    else:
        caminho.append(no)
        if no.posicao == posicao:
            return caminho
        else:
            caminho = buscaCaminho(no.filhoDireita, posicao, caminho)
            if (caminho[-1].posicao == -1):
                caminho.pop()
                caminho = buscaCaminho(no.filhoEsquerda, posicao, caminho)
                if (caminho[-1].posicao == -1):
                    caminho.pop()
                    caminho.pop()
                    caminho.append(noNulo)
                    return caminho
                else:
                    return caminho
            else:
                return caminho
