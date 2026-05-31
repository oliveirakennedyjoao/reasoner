from domain.ConexaoNo import ConexaoNo
from domain.NoArvore import NoArvore

from util.buscaCaminho import buscaCaminho
from util.buscaNosTipo import buscaNosTipo
from util.substituiPosicao import substituiPosicao
from util.removeNo import removeNo
from util.constaNo import constaNo
from util.substituiPosicaoFinal import substituiPosicaoFinal
from util.checaReflexividade import checaReflexividade
from util.ehPredicado import ehPredicado

from typing import List


def geraOrdemReducao(conexoes: List[ConexaoNo], noRaiz: NoArvore) -> List:
    R = []
    P = []
    ordemReducao = []
    alphaL = []
    delta = []
    sigmaFinal = []

    for conexao in conexoes:
        cn1 = buscaCaminho(noRaiz, conexao.posicao1, [])
        cn2 = buscaCaminho(noRaiz, conexao.posicao2, [])

        for z, cn in enumerate([cn1, cn2], start=1):
            continua = True
            conectar = False
            j = 0
            while continua:
                if cn[j].tipo == None:
                    P.append(cn[j])
                    continua = False

                    if z == 2:
                        conectar = True
                else:
                    if cn[j] not in R:
                        ##
                        # algoritmo 7
                        ##
                        if cn[j].tipo in ["α", "α'", "β"]:
                            R.append(cn[j])
                            ordemReducao.append(cn[j])
                            if cn[j].tipo == "α'":
                                alphaL.append(cn[j])
                        elif cn[j].tipo == "δ":
                            delta.append(cn[j])
                            R.append(cn[j])
                            ordemReducao.append(cn[j])
                            nosGamma = buscaNosTipo("γ", P)
                            if len(nosGamma) > 0:
                                for noGamma in nosGamma:
                                    sigmaDelta = substituiPosicao(
                                        noGamma, delta[-1], sigmaFinal)
                                    R.append(noGamma)
                                    P = removeNo(noGamma, P)
                                    sigmaFinal = sigmaDelta
                        elif cn[j].tipo == "β'":
                            if len(alphaL) > 0:
                                sigmaBeta = substituiPosicao(
                                    cn[j], alphaL[-1], sigmaFinal)
                                R.append(cn[j])
                                ordemReducao.append(cn[j])
                                sigmaFinal = sigmaBeta
                            else:
                                for no in cn[j:]:
                                    if not constaNo(no, P):
                                        P.append(no)
                                continua = False
                        elif cn[j].tipo == "γ":
                            if len(delta) > 0:
                                sigmaGamma = substituiPosicao(
                                    cn[j], delta[-1], sigmaFinal)
                                R.append(cn[j])
                                sigmaFinal = sigmaGamma
                            else:
                                for no in cn[j:]:
                                    if not constaNo(no, P):
                                        P.append(no)
                                continua = False
                        j += 1
                    else:
                        j += 1
        if conectar:
            # executar algoritmo 8
            # adaptado (folha1 e folha2), pois substituirPosicaoFinal modifica cn1 e cn2 realizando um pop
            folha1 = cn1[-1]
            folha2 = cn2[-1]
            temp = substituiPosicaoFinal(cn1, cn2, sigmaFinal)
            if temp is not None:
                sigmaFinal = temp
                isReflexiva = checaReflexividade(ordemReducao)

                if not isReflexiva:
                    parLit = [folha1, folha2]
                    achou = False
                    for pl in parLit:
                        if pl in R:
                            achou = True
                            P.pop()
                        else:
                            R.append(P.pop())
                    if achou == False and ehPredicado(parLit[0]):
                        ordemReducao.append(parLit)
                else:
                    return None
            else:
                return None

    return ordemReducao
