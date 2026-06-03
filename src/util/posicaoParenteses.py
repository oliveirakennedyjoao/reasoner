from domain.NoSequente import NoSequente


def posicaoParenteses(F: NoSequente, idx: int) -> list:
    achou = False
    tam = len(F.Lit)
    i = idx - 1
    par = []

    while i >= 0 and not achou:
        if F.Lit[i].rotulo == '(':
            achou = True
            par.append(i)
        i -= 1

    achou = False
    i = idx + 1

    while i < tam and not achou:
        if F.Lit[i].rotulo == ')':
            achou = True
            par.append(i)
        i += 1

    return par
