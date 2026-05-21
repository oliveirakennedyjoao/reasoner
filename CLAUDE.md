# Reasoner — Contexto do Projeto

## O que é este projeto

Implementação em Python do método de conversão descrito na tese de doutorado:

> **"Conversão de Provas em Lógica de Descrições ALC Geradas pelo Método de Conexões para Sequentes"**
> Eunice Palmeira da Silva — UFPE, 2017
> PDF: `/Users/jk/Documents/Mestrado/TESE Eunice Palmeira da Silva.pdf`

O sistema converte provas em ALC geradas pelo **Método de Conexões não-clausal** para provas no **Cálculo de Sequentes para ALC**.

---

## Pipeline (4 etapas)

```
Fórmula ALC (string)
      ↓ [parser/tokenizer]
   F[]  (array de Literal)
      ↓ Alg 1: converteEmInFixa
   Fin[] (infixo — ∃/∀ movidos antes do ponto)
      ↓ Alg 2: converteEmPosFixa
   Fp[]  (pós-fixo — parênteses removidos)
      ↓ Alg 11: atualizaPosicao (recalcula índices sem parênteses)
      ↓ Alg 3: constroiArvore
   AST   (árvore de fórmula — NoArvore)
      ↓ Alg 4: atribuiPosicao
   Matriz com posições atribuídas
      ↓ Etapa 3: análise de conexões + ordem de redução ◁
   Estrutura parcial da prova em sequentes
      ↓ Etapa 4: aplicação das regras dos sequentes
   Prova completa em sequentes
```

---

## Modelos de domínio

### Literal (`src/domain/Literal.py`)
Representa um símbolo da fórmula.
- `rotulo`: símbolo (ex: "∃", "OL", "⊑")
- `posicao`: índice que identifica o símbolo na fórmula

### NoArvore (`src/domain/NoArvore.py`)
Nó da árvore de fórmula (AST).
- `rotulo`, `posicao`, `polaridade` (0 ou 1)
- `tipo`: α, α', β, β', γ, δ (ou 'folha')
- `posSubst[2]`: posições associadas para substituição (posBl, posGD)
- `filhoEsquerda`, `filhoDireita`

### Elemento (`src/domain/Elemento.py`)
Literal na matriz de prova do Método de Conexões.
- `id`, `literal`, `polaridade`, `posicao`
- `conexoes[]`: lista de Conexao

### Conexao (`src/domain/Conexao.py`)
Par de literais complementares na matriz.
- `idElemento1`, `idElemento2`, `ordem`

---

## Tipos de nó e polaridades (Tabela 6/13 da tese)

| Tipo | Construtor | Pol | PolFilhoEsq | PolFilhoDir |
|------|-----------|-----|-------------|-------------|
| α    | ⊓         | 1   | 1           | 1           |
| α    | ⊔         | 0   | 0           | 0           |
| α    | ¬         | 1   | 0           | —           |
| α    | ¬         | 0   | 1           | —           |
| α'   | ⊑         | 0   | 1           | 0           |
| α'   | \|=       | 0   | 1           | 0           |
| β'   | ⊑         | 1   | 0           | 1           |
| β    | ⊓         | 0   | 0           | 0           |
| β    | ⊔         | 1   | 1           | 1           |
| δ    | ∀         | 0   | 1           | 0           |
| δ    | ∃         | 1   | 1           | 1           |
| γ    | ∀         | 1   | 0           | 1           |
| γ    | ∃         | 0   | 0           | 0           |

**α/α'**: não causam ramificação.
**β/β'**: causam ramificação em dois sub-ramos independentes. Nós β' são ⊑¹, fundamentais para subsunção.
**γ/δ**: regras de quantificadores. δ tem restrição de autovariável (deve ser reduzido antes de γ).

---

## Regras de sequentes correspondentes (Tabelas 7 e 8 da tese)

**Sem negação precedente (Tabela 7):**
- α: ⊓¹→l⊓, ⊔⁰→r⊔
- β: ⊓⁰→r⊓, ⊔¹→l⊔
- δ: ∀⁰→r∀, ∃¹→l∃
- β': ⊑¹ → regra de corte com dois sub-sequentes
- α'/γ/∃⁰/∀¹: sem regra direta (∅)

**Com negação precedente (Tabela 8):**
- ¬¹→r¬¬, ¬⁰→l¬¬
- ⊓¹→r¬⊓, ⊔⁰→l¬⊔
- ⊓⁰→l¬⊓, ⊔¹→r¬⊔
- ∀⁰→l¬∀, ∃¹→r¬∃

---

## Algoritmos principais (Cap. 6 da tese)

| Alg | Função | Arquivo | Status |
|-----|--------|---------|--------|
| 1   | `converteEmInFixa(F[])` | `lib/converteeminfixa.py` | ✅ |
| 2   | `converteEmPosFixa(Fin[])` | `lib/converteemposfixa.py` | ✅ |
| 3   | `constroiArvore(...)` | `lib/constroiArvoreAdaptado.py` | ✅ (adaptado: iterativo em vez de recursivo) |
| 4   | `atribuiPosicao(matriz[], Fp[], indice)` | `lib/atribuiPosicao.py` | ✅ |
| 11  | `atualizaPosicao(F[])` | `util/atualizaPosicao.py` | ✅ |
| 5-10 | Etapas 3 e 4 (análise de conexões + construção da prova) | — | ❌ não implementado |

### Algoritmos auxiliares (Apêndice C da tese)

| Alg | Função | Notas |
|-----|--------|-------|
| 12  | `constaConexao(C[], ordem)` | verifica se conexão existe |
| 13  | `buscaPosicao(matriz[], idelemento)` | busca posição por ID |
| 14  | `ordenaConexao(C[])` | selection sort de conexões |
| 15  | `buscaCaminho(no, pos, caminho)` | caminho raiz→nó (backtracking) |
| 16  | `substituiPosicao(no1, no2, σ)` | substitui posições σδ/σβ' |
| 17  | `constaNo(no, lista)` | nó está em lista? |
| 18  | `buscaNosTipo(tipo, lista)` | filtra nós por tipo |
| 19  | `removeNo(no, lista)` | remove nó de lista |
| 20  | `checaReflexividade(◁)` | verifica se ordem de redução é reflexiva |
| 21  | `substituiPosicaoFinal(cn1, cn2, σFinal)` | substitui posições σFinal |
| 22-27 | `aplicaRegra*` | aplicam regras de sequentes sobre F |
| 34  | `buscaRegraSequentes(noArv, noEst)` | consulta tabelas 7/8 |
| 35  | `constaNoRotulo(rotulo, caminho)` | há nó com dado rótulo no caminho? |
| 36  | `buscaNoRotulo(rotulo, caminho)` | retorna nó com dado rótulo no caminho |

---

## Fórmula de exemplo usada nos testes

F1 (tese, p.58):
```
((((∃h.C)⊑CO)⊓(OL⊑((∃h.A)⊓(∀h.C))))|=(OL(a)⊑CO(a)))
```

Operadores ALC usados: `∃` (existencial), `∀` (universal), `⊑` (subsunção), `⊓` (interseção), `⊔` (união), `¬` (negação), `|=` (entailment/sequente).

---

## Convenções do projeto

- Python 3.14, sem dependências externas além do stdlib
- Testes com pytest em `tests/`
- Constantes e dados de teste em `src/constants/`
- Código em português (nomes de variáveis e funções seguem a tese)
- `constroiArvoreAdaptado.py` é a versão iterativa (via pilha) do Alg 3, que na tese é recursivo — esta adaptação é intencional
