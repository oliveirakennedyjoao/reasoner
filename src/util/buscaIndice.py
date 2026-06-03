from domain.NoSequente import NoSequente


def buscaIndice(F: NoSequente, posicao: int) -> int:
    achou = False
    i = 0
    idx = -1
    while i < len(F.Lit) and not achou:
        if F.Lit[i].posicao == posicao:
            achou = True
            idx = i
        i += 1
    return idx
