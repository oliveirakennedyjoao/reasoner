#!/usr/bin/env python3
"""
Visualizador web do pipeline do Reasoner.
Uso: python visualizer.py
Abre em: http://localhost:8080
"""

from lib.constroiArvore import constroiArvore
from lib.converteemposfixa import converteEmPosFixa
from lib.converteeminfixa import converteEmInFixa
from util.atualizaPosicao import atualizaPosicao
from util.parser import parse_to_literal
import json
import sys
import os
import traceback
import webbrowser
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

sys.path.insert(0, os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "src"))


FORMULA_EXEMPLO = "((((∃h.C)⊑CO)⊓(OL⊑((∃h.A)⊓(∀h.C))))|=(OL(a)⊑CO(a)))"


def literal_para_dict(lit):
    return {"rotulo": lit.rotulo, "posicao": lit.posicao}


def no_para_dict(no):
    if no is None:
        return None
    d = {
        "rotulo": no.rotulo,
        "posicao": no.posicao,
        "polaridade": no.polaridade,
        "tipo": no.tipo,
        "posSubst": no.posSubst,
    }
    esq = no_para_dict(no.filhoEsquerda) if no.filhoEsquerda else None
    dir_ = no_para_dict(no.filhoDireita) if no.filhoDireita else None
    if esq:
        d["filhoEsquerda"] = esq
    if dir_:
        d["filhoDireita"] = dir_
    return d


def executar_pipeline(formula: str):
    F = parse_to_literal(formula)
    Fin = converteEmInFixa(F)

    pos = [lit.posicao for lit in Fin]
    atualizaPosicao(Fin, pos)
    Fpos = converteEmPosFixa(Fin)

    ast = constroiArvore(Fpos, 0, [0, 0, 0, 0], 0, 0)

    return [
        {
            "titulo": "Etapa 1 — Parser / Tokenizer",
            "descricao": "Converte a string da fórmula em uma lista de Literals com índices de posição.",
            "entrada": {"formula": formula},
            "saida": {"F": [literal_para_dict(l) for l in F]},
        },
        {
            "titulo": "Etapa 2 — converteEmInFixa (Alg 1)",
            "descricao": "Move ∃/∀ para antes do ponto removendo o '.', produzindo a forma infixa Fin.",
            "entrada": {"F": [literal_para_dict(l) for l in F]},
            "saida": {"Fin": [literal_para_dict(l) for l in Fin]},
        },
        {
            "titulo": "Etapa 3 — converteEmPosFixa + atualizaPosicao (Alg 2 + 11)",
            "descricao": "Remove parênteses, converte para pós-fixo e recalcula os índices sem parênteses.",
            "entrada": {"Fin": [literal_para_dict(l) for l in Fin]},
            "saida": {"Fpos": [literal_para_dict(l) for l in Fpos]},
        },
        {
            "titulo": "Etapa 4 — constroiArvore (Alg 3)",
            "descricao": "Constrói a AST (árvore de fórmula) iterativamente a partir da fórmula pós-fixa.",
            "entrada": {"Fpos": [literal_para_dict(l) for l in Fpos]},
            "saida": {"ast": no_para_dict(ast)},
        },
    ]


HTML = r"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Reasoner — Visualizador de Pipeline</title>
<script src="https://cdn.jsdelivr.net/npm/d3@7/dist/d3.min.js"></script>
<style>
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
  background: #0d1117;
  color: #e2e8f0;
  min-height: 100vh;
}
header {
  background: #161b27;
  border-bottom: 1px solid #21293a;
  padding: 1.25rem 2rem;
  display: flex;
  align-items: center;
  gap: 1.5rem;
}
header h1 { font-size: 1.2rem; font-weight: 700; color: #a78bfa; letter-spacing: -0.02em; }
header p { color: #4b5563; font-size: 0.82rem; margin-top: 0.2rem; }
.main { max-width: 1400px; margin: 0 auto; padding: 2rem; }

/* Input section */
.input-card {
  background: #161b27;
  border: 1px solid #21293a;
  border-radius: 10px;
  padding: 1.25rem 1.5rem;
  margin-bottom: 2rem;
}
.input-row { display: flex; gap: 0.75rem; align-items: flex-end; }
label { display: block; color: #6b7280; font-size: 0.75rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.5rem; }
input[type=text] {
  flex: 1;
  background: #0d1117;
  border: 1px solid #2d3748;
  border-radius: 7px;
  padding: 0.65rem 1rem;
  color: #e2e8f0;
  font-size: 0.95rem;
  font-family: 'Cascadia Code', 'Fira Code', monospace;
  outline: none;
  transition: border-color 0.15s;
}
input[type=text]:focus { border-color: #7c3aed; }
button {
  background: #7c3aed;
  color: #fff;
  border: none;
  border-radius: 7px;
  padding: 0.65rem 1.5rem;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  white-space: nowrap;
  transition: background 0.15s;
}
button:hover:not(:disabled) { background: #6d28d9; }
button:disabled { background: #2d3748; color: #4b5563; cursor: not-allowed; }

/* Error */
.error-box {
  background: #2d0f0f;
  border: 1px solid #7f1d1d;
  border-radius: 8px;
  padding: 1rem 1.25rem;
  color: #fca5a5;
  font-family: monospace;
  font-size: 0.82rem;
  white-space: pre-wrap;
  margin-bottom: 1.5rem;
}

/* Steps */
.steps { display: flex; flex-direction: column; gap: 1.25rem; }
.step {
  background: #161b27;
  border: 1px solid #21293a;
  border-radius: 10px;
  overflow: hidden;
}
.step-header {
  padding: 0.9rem 1.5rem;
  border-bottom: 1px solid #21293a;
  display: flex;
  align-items: baseline;
  gap: 0.75rem;
}
.step-num {
  background: #7c3aed;
  color: #fff;
  border-radius: 5px;
  padding: 0.15rem 0.5rem;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  flex-shrink: 0;
}
.step-title { font-weight: 600; font-size: 0.95rem; color: #e2e8f0; }
.step-desc { color: #4b5563; font-size: 0.82rem; }
.step-body { display: grid; grid-template-columns: 1fr 1fr; }
.panel {
  padding: 1.1rem 1.5rem;
  min-height: 5rem;
}
.panel:first-child { border-right: 1px solid #21293a; }
.panel-label {
  font-size: 0.7rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: #374151;
  margin-bottom: 0.75rem;
}

/* Literal chips */
.chips { display: flex; flex-wrap: wrap; gap: 0.35rem; }
.chip {
  display: inline-flex;
  align-items: baseline;
  gap: 0.15rem;
  background: #0d1117;
  border: 1px solid #2d3748;
  border-radius: 4px;
  padding: 0.15rem 0.45rem;
  font-family: monospace;
  font-size: 0.82rem;
  color: #a78bfa;
}
.chip .idx { color: #374151; font-size: 0.68rem; }
.chip.constructor { color: #60a5fa; border-color: #1e3a5f; background: #0f1d2e; }
.chip.paren { color: #374151; border-color: #1f2937; }
.formula-raw {
  font-family: monospace;
  font-size: 0.9rem;
  color: #34d399;
  word-break: break-all;
  line-height: 1.7;
}

/* AST Tree */
.tree { font-family: 'Cascadia Code', 'Fira Code', monospace; font-size: 0.82rem; line-height: 1.6; }
details.tnode { margin-left: 1rem; }
details.tnode > summary {
  cursor: pointer;
  list-style: none;
  display: flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.1rem 0;
  user-select: none;
}
details.tnode > summary::-webkit-details-marker { display: none; }
.toggle-icon { color: #374151; font-size: 0.6rem; transition: transform 0.12s; }
details[open] > summary .toggle-icon { transform: rotate(90deg); }
.leaf-node {
  margin-left: calc(1rem + 0.4rem + 0.6rem);
  padding: 0.1rem 0;
  display: flex;
  align-items: center;
  gap: 0.4rem;
  color: #94a3b8;
}
.leaf-dot { color: #374151; font-size: 0.55rem; }
.n-rotulo { color: #e2e8f0; font-weight: 600; }
.n-pos { color: #374151; }
.n-pol { font-size: 0.75rem; font-weight: 700; }
.pol-1 { color: #34d399; }
.pol-0 { color: #f87171; }
.badge {
  border-radius: 3px;
  padding: 0.05rem 0.3rem;
  font-size: 0.68rem;
  font-weight: 700;
}
.b-alpha  { background: #1e3a5f; color: #60a5fa; }
.b-alpha2 { background: #1a2e4a; color: #7dd3fc; }
.b-beta   { background: #2e1f5f; color: #c084fc; }
.b-beta2  { background: #271a4a; color: #d8b4fe; }
.b-gamma  { background: #1a3323; color: #4ade80; }
.b-delta  { background: #33250f; color: #fb923c; }
.b-folha  { background: #1f2937; color: #6b7280; }

.placeholder { color: #2d3748; font-size: 0.85rem; font-style: italic; }
.loading { color: #4b5563; font-size: 0.85rem; padding: 1rem 0; }
.ast-d3-container { width: 100%; height: 420px; overflow: hidden; cursor: grab; background: #0a0e17; border-radius: 6px; }
.ast-d3-container:active { cursor: grabbing; }
.tree-hint { color: #374151; font-size: 0.7rem; text-align: center; margin-top: 0.35rem; letter-spacing: 0.03em; }
</style>
</head>
<body>
<header>
  <div>
    <h1>Reasoner — Visualizador de Pipeline</h1>
    <p>Conversão ALC (Método de Conexões → Cálculo de Sequentes) · Tese Eunice Palmeira da Silva, UFPE 2017</p>
  </div>
</header>
<div class="main">
  <div class="input-card">
    <div class="input-row">
      <div style="flex:1">
        <label>Fórmula ALC</label>
        <input type="text" id="formula" value="((((∃h.C)⊑CO)⊓(OL⊑((∃h.A)⊓(∀h.C))))|=(OL(a)⊑CO(a)))">
      </div>
      <div>
        <label>&nbsp;</label>
        <button id="btn" onclick="runPipeline()">Executar</button>
      </div>
    </div>
  </div>
  <div id="error-box"></div>
  <div id="steps" class="steps"></div>
</div>

<script>
const CONSTRUTORES = new Set(['|=','⊑','⊓','⊔','¬','∃','∀']);
const PARENS = new Set(['(',')']);

function tipoBadge(tipo) {
  if (!tipo) return '';
  const map = {
    'α': ['b-alpha', 'α'], "α'": ['b-alpha2', "α'"],
    'β': ['b-beta', 'β'], "β'": ['b-beta2', "β'"],
    'γ': ['b-gamma', 'γ'], 'δ': ['b-delta', 'δ'],
    'folha': ['b-folha', '◆'],
  };
  const [cls, label] = map[tipo] || ['b-folha', tipo];
  return `<span class="badge ${cls}">${label}</span>`;
}

function chipClass(rotulo) {
  if (PARENS.has(rotulo)) return 'chip paren';
  if (CONSTRUTORES.has(rotulo)) return 'chip constructor';
  return 'chip';
}

function renderChips(literals) {
  if (!literals || literals.length === 0) return '<span class="placeholder">—</span>';
  return '<div class="chips">' + literals.map(l =>
    `<span class="${chipClass(l.rotulo)}">${esc(l.rotulo)}<span class="idx">${l.posicao}</span></span>`
  ).join('') + '</div>';
}

function renderNo(no, depth = 0) {
  if (!no) return '';
  const rotulo = esc(no.rotulo);
  const pos = `<span class="n-pos">[${no.posicao}]</span>`;
  const pol = no.polaridade !== null
    ? `<span class="n-pol ${no.polaridade === 1 ? 'pol-1' : 'pol-0'}">${no.polaridade === 1 ? '¹' : '⁰'}</span>`
    : '';
  const badge = tipoBadge(no.tipo);
  const label = `<span class="toggle-icon">▶</span><span class="n-rotulo">${rotulo}</span>${pos}${pol}${badge}`;

  const hasChildren = no.filhoEsquerda || no.filhoDireita;
  if (!hasChildren) {
    return `<div class="leaf-node"><span class="leaf-dot">●</span>${label}</div>`;
  }

  const open = depth < 2 ? ' open' : '';
  let children = '';
  if (no.filhoEsquerda) children += renderNo(no.filhoEsquerda, depth + 1);
  if (no.filhoDireita)  children += renderNo(no.filhoDireita, depth + 1);
  return `<details class="tnode"${open}><summary>${label}</summary>${children}</details>`;
}

function renderEntrada(entrada) {
  if (entrada.formula !== undefined) {
    return `<div class="formula-raw">${esc(entrada.formula)}</div>`;
  }
  const key = Object.keys(entrada)[0];
  return renderChips(entrada[key]);
}

function renderSaida(saida, stepIdx) {
  const key = Object.keys(saida)[0];
  const val = saida[key];
  if (key === 'ast') {
    if (!val) return '<span class="placeholder">AST vazia</span>';
    return `<div id="ast-tree-${stepIdx}" class="ast-d3-container"></div>
<div class="tree-hint">scroll para zoom · arrastar para mover</div>`;
  }
  return renderChips(val);
}

const TIPO_COLOR = {
  'α': '#60a5fa', "α'": '#7dd3fc',
  'β': '#c084fc', "β'": '#d8b4fe',
  'γ': '#4ade80', 'δ': '#fb923c',
  'folha': '#4b5563'
};

function toHierarchy(no) {
  const n = { rotulo: no.rotulo, posicao: no.posicao, polaridade: no.polaridade, tipo: no.tipo };
  const kids = [];
  if (no.filhoEsquerda) kids.push(toHierarchy(no.filhoEsquerda));
  if (no.filhoDireita)  kids.push(toHierarchy(no.filhoDireita));
  if (kids.length) n.children = kids;
  return n;
}

function drawASTTree(containerId, data) {
  const container = document.getElementById(containerId);
  if (!container || !data) return;

  const W = container.clientWidth || 600;
  const H = 420;
  const R = 20, dx = 76, dy = 70;

  const root = d3.hierarchy(toHierarchy(data));
  d3.tree().nodeSize([dx, dy])(root);

  let x0 = Infinity, x1 = -Infinity;
  root.each(d => { x0 = Math.min(x0, d.x); x1 = Math.max(x1, d.x); });

  const treeW = x1 - x0 + dx;
  const treeH = root.height * dy + R * 3;
  const k = Math.min((W - 40) / treeW, (H - 40) / treeH, 1.5);
  const tx = W / 2 - ((x0 + x1) / 2) * k;
  const ty = R * k + 16;

  const svg = d3.select(container).append('svg')
    .attr('width', W).attr('height', H)
    .style('display', 'block');

  const g = svg.append('g');

  const zoom = d3.zoom().scaleExtent([0.15, 4])
    .on('zoom', e => g.attr('transform', e.transform));

  svg.call(zoom)
     .call(zoom.transform, d3.zoomIdentity.translate(tx, ty).scale(k));

  g.append('g')
    .attr('fill', 'none').attr('stroke', '#2d3748').attr('stroke-width', 1.5)
    .selectAll('path').data(root.links()).join('path')
    .attr('d', d3.linkVertical().x(d => d.x).y(d => d.y));

  const node = g.append('g').selectAll('g').data(root.descendants()).join('g')
    .attr('transform', d => `translate(${d.x},${d.y})`);

  node.append('circle')
    .attr('r', R).attr('fill', '#161b27')
    .attr('stroke', d => TIPO_COLOR[d.data.tipo] || '#374151')
    .attr('stroke-width', 2);

  node.append('text')
    .attr('text-anchor', 'middle').attr('dominant-baseline', 'central')
    .attr('fill', '#e2e8f0').attr('font-size', '12px').attr('font-weight', '600')
    .attr('font-family', 'monospace')
    .text(d => d.data.rotulo);

  node.append('text')
    .attr('text-anchor', 'middle').attr('y', R + 11)
    .attr('fill', '#4b5563').attr('font-size', '9px').attr('font-family', 'monospace')
    .text(d => `[${d.data.posicao}]`);

  node.filter(d => d.data.polaridade != null)
    .append('text')
    .attr('text-anchor', 'middle').attr('y', -R - 5)
    .attr('font-size', '10px').attr('font-weight', 'bold').attr('font-family', 'monospace')
    .attr('fill', d => d.data.polaridade === 1 ? '#34d399' : '#f87171')
    .text(d => d.data.polaridade === 1 ? '¹' : '⁰');
}

function renderSteps(steps) {
  const container = document.getElementById('steps');
  container.innerHTML = steps.map((s, i) => `
    <div class="step">
      <div class="step-header">
        <span class="step-num">ETAPA ${i+1}</span>
        <div>
          <div class="step-title">${esc(s.titulo.replace(/^Etapa \d+ — /, ''))}</div>
          <div class="step-desc">${esc(s.descricao)}</div>
        </div>
      </div>
      <div class="step-body">
        <div class="panel">
          <div class="panel-label">Entrada</div>
          ${renderEntrada(s.entrada)}
        </div>
        <div class="panel">
          <div class="panel-label">Saída</div>
          ${renderSaida(s.saida, i)}
        </div>
      </div>
    </div>
  `).join('');
  steps.forEach((s, i) => {
    if (s.saida.ast) requestAnimationFrame(() => drawASTTree(`ast-tree-${i}`, s.saida.ast));
  });
}

function showError(msg) {
  document.getElementById('error-box').innerHTML =
    `<div class="error-box">${esc(msg)}</div>`;
}

function esc(s) {
  return String(s)
    .replace(/&/g,'&amp;')
    .replace(/</g,'&lt;')
    .replace(/>/g,'&gt;');
}

async function runPipeline() {
  const formula = document.getElementById('formula').value.trim();
  const btn = document.getElementById('btn');
  if (!formula) return;

  btn.disabled = true;
  btn.textContent = 'Processando…';
  document.getElementById('error-box').innerHTML = '';
  document.getElementById('steps').innerHTML = '<p class="loading">Executando pipeline…</p>';

  try {
    const resp = await fetch('/run', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ formula }),
    });
    const data = await resp.json();
    if (!resp.ok) {
      showError(data.erro || 'Erro desconhecido');
      document.getElementById('steps').innerHTML = '';
    } else {
      renderSteps(data.etapas);
    }
  } catch (e) {
    showError(e.message);
    document.getElementById('steps').innerHTML = '';
  } finally {
    btn.disabled = false;
    btn.textContent = 'Executar';
  }
}

// Run automatically on load
window.addEventListener('DOMContentLoaded', runPipeline);
</script>
</body>
</html>
"""


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        pass  # silencia logs do servidor

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(HTML.encode("utf-8"))

    def do_POST(self):
        if self.path != "/run":
            self.send_response(404)
            self.end_headers()
            return

        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length)

        try:
            payload = json.loads(body)
            formula = payload.get("formula", "").strip()
            if not formula:
                raise ValueError("Fórmula vazia.")
            etapas = executar_pipeline(formula)
            resposta = json.dumps({"etapas": etapas}, ensure_ascii=False)
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(resposta.encode("utf-8"))
        except Exception as e:
            erro = traceback.format_exc()
            resposta = json.dumps(
                {"erro": str(e), "traceback": erro}, ensure_ascii=False)
            self.send_response(500)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(resposta.encode("utf-8"))


def main():
    porta = 8080
    servidor = HTTPServer(("localhost", porta), Handler)
    url = f"http://localhost:{porta}"
    print(f"Reasoner Visualizer  →  {url}")
    print("Ctrl+C para encerrar.")
    threading.Timer(0.5, lambda: webbrowser.open(url)).start()
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        print("\nEncerrado.")


if __name__ == "__main__":
    main()
