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

Returns:
    NoArvore: Retorna a AST na forma de uma árvore de NoArvore.
"""


def constroiArvore(Fp: List[Literal], pol: int, arcos: List, posBetal: int, posGDelta: int) -> NoArvore:
    pilha = []
    construtores = ['|=', '⊑', '⊓', '⊔', '¬', '∃', '∀']
    posBl = posBetal
    posGD = posGDelta

    print(f"🔍 Iniciando construção com {len(Fp)} elementos")

    for i, literal in enumerate(Fp):
        print(f"[{i}] Processando: {literal.rotulo}")
        if literal.rotulo in construtores:
            print(f"   → É construtor! Pilha atual: {len(pilha)} elementos")

            trl = busca_tipo_pol(literal.rotulo, pol)
            print(f"   → Tipo encontrado: {trl.tipo}")

            if trl.tipo == 'β':
                arcos[0] = arcos[0] + 1
                arcos[1] = arcos[1] + 1
                no = NoArvore(literal.rotulo, literal.posicao,
                              pol, trl.tipo, posBl, posGD)
            elif trl.tipo == "β'":
                arcos[2] = arcos[2] + 1
                arcos[3] = arcos[2] + 1
                posBl = literal.posicao
                no = NoArvore(literal.rotulo, literal.posicao,
                              pol, trl.tipo, posBl, posGD)
            elif trl.tipo == 'γ' or trl.tipo == 'δ':
                posGD = literal.posicao
                no = NoArvore(literal.rotulo, literal.posicao,
                              pol, trl.tipo, posBl, posGD)
            else:
                no = NoArvore(literal.rotulo, literal.posicao,
                              pol, trl.tipo, posBl, posGD)

            # Lógica da pilha: operadores consomem operandos
            if literal.rotulo in ['¬', '∃', '∀']:  # Operadores unários
                if pilha:
                    no.filhoEsquerda = pilha.pop()
                    print(f"   → Operador unário: 1 filho adicionado")
                else:
                    print(f"   → Operador unário: nenhum filho na pilha")

            else:  # Operadores binários ['|=', '⊑', '⊓', '⊔']
                if len(pilha) >= 2:
                    no.filhoDireita = pilha.pop()  # Segundo operando (direita)
                    no.filhoEsquerda = pilha.pop()  # Primeiro operando (esquerda)
                    print(f"   → Operador binário: 2 filhos adicionados")
                elif len(pilha) == 1:
                    no.filhoEsquerda = pilha.pop()
                    print(f"   → Operador binário: apenas 1 filho disponível")
                else:
                    print(f"   → Operador binário: nenhum filho na pilha")

            # Atualizar polaridades dos filhos
            if no.filhoEsquerda and hasattr(trl, 'polNoEsq') and trl.polNoEsq is not None:
                no.filhoEsquerda.polaridade = trl.polNoEsq
                print(f"   → Polaridade filho esq: {trl.polNoEsq}")
            if no.filhoDireita and hasattr(trl, 'polNoDir') and trl.polNoDir is not None:
                no.filhoDireita.polaridade = trl.polNoDir
                print(f"   → Polaridade filho dir: {trl.polNoDir}")

            pilha.append(no)
            print(f"   → Operador processado. Pilha: {len(pilha)} elementos")
        else:
            # Folhas (variáveis, constantes) - usar posBl e posGD atualizados
            print(f"   → É folha! Adicionando à pilha")
            no = NoArvore(literal.rotulo, literal.posicao,
                          pol, 'folha', posBl, posGD)
            pilha.append(no)
            print(f"   → Folha adicionada. Pilha: {len(pilha)} elementos")

    print(f"🎯 Construção finalizada. Pilha final: {len(pilha)} elementos")

    # Debug: mostrar elementos restantes na pilha
    if len(pilha) > 1:
        print("⚠️  ATENÇÃO: Pilha tem mais de 1 elemento! Elementos restantes:")
        for i, elemento in enumerate(pilha):
            print(f"   [{i}] {elemento.rotulo} (pos: {elemento.posicao})")
        print("   → Retornando último elemento (topo da pilha) como raiz")

    # Retorna o TOPO da pilha (último elemento)
    return pilha[-1] if pilha else None
