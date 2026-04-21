from domain.NoArvore import NoArvore
from domain.Literal import Literal
from util.buscaTipoPol import busca_tipo_pol
from typing import List

"""
Resumo da função aqui.

Args:
    - Fp (List[Literal]): Array que armazena os elementos de uma fórmula dispostos na notação pós-fixa.
    - pol (int): Valor inteiro (0,1) que representa a polaridade do literal. O valor inicial de pol é 0.
    - arcos (List): Array de tamanho 4 com os índices para dois ramos do tipo β e β'. Arcos é inicialmente vazio.
    - posBetal (int): Variável que armazena a posição de um nó do tipo β', a fim de associá-la a nós folha.
    - posGDelta (int): Variável que armazena a posição de um nó do tipo γ ou δ, a fim de associá-la a nós folha.
    - inStr e inEnd (int): São duas variáveis inteiras que auxiliam na identificação dos nós que são folha. Seus valores iniciais são 0 e n-1, respectivamente, onde n é o número de elementos do array Fp.

Returns:
    NoArvore: Retorna a AST na forma de uma árvore de NoArvore.
"""


def constroiArvore(Fp: List[Literal], pol: int, arcos: List, posBetal: int, posGDelta: int) -> NoArvore:
    pilha = []
    construtores = ['|=', '⊑', '⊓', '⊔', '¬', '∃', '∀']
    posBl = posBetal
    posGD = posGDelta

    for literal in Fp:
        if literal.rotulo in construtores:
            trl = busca_tipo_pol(literal.rotulo, pol)
            if trl.tipo == 'β':
                arcos[0] = arcos[0] + 1
                arcos[1] = arcos[1] + 1
                no = NoArvore(literal.rotulo, literal.posicao,
                              pol, trl.tipo, arcos[0], arcos[1])
            elif trl.tipo == "β'":
                arcos[2] = arcos[2] + 1
                arcos[3] = arcos[2] + 1
                posBl = literal.posicao
                no = NoArvore(literal.rotulo, literal.posicao,
                              pol, trl.tipo, arcos[2], arcos[3])
            elif trl.tipo == 'γ' or trl.tipo == 'δ':
                posGD = literal.posicao
                no = NoArvore(literal.rotulo, literal.posicao,
                              pol, trl.tipo)
            else:
                no = NoArvore(literal.rotulo, literal.posicao,
                              pol, trl.tipo)

            # Lógica da pilha: operadores consomem operandos
            if literal.rotulo in ['¬', '∃', '∀']:  # Operadores unários
                if pilha:
                    no.filhoEsquerda = pilha.pop()

            else:  # Operadores binários ['|=', '⊑', '⊓', '⊔']
                if len(pilha) >= 2:
                    no.filhoDireita = pilha.pop()  # Segundo operando (direita)
                    no.filhoEsquerda = pilha.pop()  # Primeiro operando (esquerda)
                elif len(pilha) == 1:
                    no.filhoEsquerda = pilha.pop()

            # Atualizar polaridades dos filhos
            if no.filhoEsquerda and hasattr(trl, 'polNoEsq') and trl.polNoEsq is not None:
                # Polaridade do filho esquerdo
                no.filhoEsquerda.polaridade = trl.polNoEsq
            if no.filhoDireita and hasattr(trl, 'polNoDir') and trl.polNoDir is not None:
                # Polaridade do filho direito
                no.filhoDireita.polaridade = trl.polNoDir

            pilha.append(no)
        else:
            # Folhas (variáveis, constantes) - usar posBl e posGD atualizados
            no = NoArvore(literal.rotulo, literal.posicao, pol, posBl, posGD)
            pilha.append(no)

    return pilha[0] if pilha else None
