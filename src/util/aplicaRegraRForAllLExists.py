from domain.NoSequente import NoSequente
from domain.NoArvore import NoArvore


def aplicaRegraRForAllLExists(F: NoSequente, noEst: NoArvore) -> NoSequente:
    posQuants = list(noEst.posNRJ)
    posQuants.append(noEst.posicao)
    t = len(posQuants)
    tam = len(F.Lit)
    i = 0
    auxF = []

    while i < tam:
        for k in range(t):
            if F.Lit[i].posicao == posQuants[k]:
                i += 2
                break
        else:
            auxF.append(F.Lit[i])
            i += 1

    F.Lit = auxF
    return F
