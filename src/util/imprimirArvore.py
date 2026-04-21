from domain.NoArvore import NoArvore
from typing import Dict


def print_arvore(no: NoArvore, nivel: int = 0, prefixo: str = ""):
    """
    Imprime a árvore de forma hierárquica e legível

    Args:
        no (NoArvore): Nó raiz da árvore a ser impressa
        nivel (int): Nível de indentação (para uso interno)
        prefixo (str): Prefixo adicional (para uso interno)
    """
    if no is None:
        return

    # Indentação baseada no nível
    indent = "  " * nivel

    # Informações do nó
    info_no = f"{prefixo}{indent}├─ {no.rotulo}"

    # Adicionar informações extras se disponíveis
    detalhes = []
    if hasattr(no, 'posicao'):
        detalhes.append(f"pos: {no.posicao}")
    if hasattr(no, 'polaridade') and no.polaridade is not None:
        detalhes.append(f"pol: {no.polaridade}")
    if hasattr(no, 'tipo') and no.tipo is not None:
        detalhes.append(f"tipo: {no.tipo}")

    if detalhes:
        info_no += f" ({', '.join(detalhes)})"

    print(info_no)

    # Imprimir filhos recursivamente
    if hasattr(no, 'filhoEsquerda') and no.filhoEsquerda:
        print(f"{indent}  ├─ Esquerda:")
        print_arvore(no.filhoEsquerda, nivel + 2, "")

    if hasattr(no, 'filhoDireita') and no.filhoDireita:
        print(f"{indent}  └─ Direita:")
        print_arvore(no.filhoDireita, nivel + 2, "")


def calcular_estatisticas_arvore(no: NoArvore) -> Dict[str, int]:
    """
    Calcula estatísticas da árvore

    Args:
        no (NoArvore): Nó raiz da árvore

    Returns:
        Dict[str, int]: Dicionário com estatísticas (nos, folhas, altura)
    """
    if no is None:
        return {"nos": 0, "folhas": 0, "altura": 0}

    def calcular_stats(no: NoArvore, altura_atual: int = 0):
        if no is None:
            return {"nos": 0, "folhas": 0, "altura": altura_atual}

        # Verificar se é folha
        eh_folha = (not hasattr(no, 'filhoEsquerda') or no.filhoEsquerda is None) and \
                   (not hasattr(no, 'filhoDireita') or no.filhoDireita is None)

        stats = {
            "nos": 1,
            "folhas": 1 if eh_folha else 0,
            "altura": altura_atual
        }

        # Recursão para filhos
        if hasattr(no, 'filhoEsquerda') and no.filhoEsquerda:
            stats_esq = calcular_stats(no.filhoEsquerda, altura_atual + 1)
            stats["nos"] += stats_esq["nos"]
            stats["folhas"] += stats_esq["folhas"]
            stats["altura"] = max(stats["altura"], stats_esq["altura"])

        if hasattr(no, 'filhoDireita') and no.filhoDireita:
            stats_dir = calcular_stats(no.filhoDireita, altura_atual + 1)
            stats["nos"] += stats_dir["nos"]
            stats["folhas"] += stats_dir["folhas"]
            stats["altura"] = max(stats["altura"], stats_dir["altura"])

        return stats

    return calcular_stats(no)


def imprimir_ast_completa(ast: NoArvore, titulo: str = "Árvore Sintática",
                          mostrar_stats: bool = True, mostrar_estrutura: bool = True):
    """
    Função principal para imprimir uma AST completa com todas as informações

    Args:
        ast (NoArvore): A árvore a ser impressa
        titulo (str): Título da seção
        mostrar_stats (bool): Se deve mostrar estatísticas
        mostrar_estrutura (bool): Se deve mostrar a estrutura hierárquica
    """
    if ast is None:
        print(f"❌ {titulo}: AST é None (vazia)")
        return

    print(f"\n=== {titulo.upper()} ===")

    if mostrar_stats:
        # Imprimir estatísticas da árvore
        print("\n📊 Estatísticas da árvore:")
        stats = calcular_estatisticas_arvore(ast)
        print(f"   • Total de nós: {stats['nos']}")
        print(f"   • Nós folha: {stats['folhas']}")
        print(f"   • Altura: {stats['altura']}")

    if mostrar_estrutura:
        # Imprimir estrutura da árvore
        print("\n🌳 Estrutura da AST:")
        print("┌─ RAIZ")
        print_arvore(ast, 1)
        print("└─ FIM DA ÁRVORE")

    print(f"\n=== {titulo.upper()} - CONCLUÍDO ===\n")


def imprimir_ast_simples(ast: NoArvore, titulo: str = "AST"):
    """
    Versão simplificada para impressão rápida da AST

    Args:
        ast (NoArvore): A árvore a ser impressa
        titulo (str): Título da impressão
    """
    if ast is None:
        print(f"{titulo}: None")
        return

    print(f"\n{titulo}:")
    print_arvore(ast)
    print()
