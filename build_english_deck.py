#!/usr/bin/env python3
"""Build the English CSA GCR GitHub Pages deck from slides_data.json + packt-harness CSS."""
from __future__ import annotations

import json
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
CSS_PATH = os.path.join(ROOT, "_template.css.fragment")
DATA_PATH = os.path.join(ROOT, "slides_data.json")
OUT_PATH = os.path.join(ROOT, "slides.html")

EXTRA_CSS = r"""
    .section-slide {
      height: 100%;
      display: flex;
      flex-direction: column;
      justify-content: center;
      padding: 1.2rem 1.6rem;
      gap: 0.85rem;
    }
    .section-kicker {
      font-family: var(--font-code);
      font-size: 0.92rem;
      font-weight: 750;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--accent-dk);
      background: var(--accent-sf);
      border: 1px solid var(--accent);
      width: fit-content;
      padding: 0.28rem 0.70rem;
      border-radius: 999px;
    }
    .section-title {
      font-family: var(--font-display);
      font-size: 2.55rem;
      font-weight: 800;
      line-height: 1.12;
      letter-spacing: -0.02em;
      color: var(--ink);
      max-width: 18ch;
    }
    .section-sub {
      font-size: 1.15rem;
      color: var(--ink-muted);
      font-weight: 550;
      max-width: 42rem;
    }
    .triple-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 0.85rem;
      margin-top: 0.35rem;
    }
    .triple-card {
      background: var(--surface);
      border: 1.5px solid var(--rule);
      border-radius: 12px;
      padding: 1.05rem 1.15rem 1.20rem;
      display: flex;
      flex-direction: column;
      gap: 0.45rem;
      box-shadow: 0 4px 14px rgba(0,0,0,0.04);
      min-height: 0;
    }
    .triple-num {
      font-family: var(--font-code);
      font-size: 1.35rem;
      font-weight: 800;
      color: var(--accent-dk);
    }
    .triple-title {
      font-family: var(--font-display);
      font-size: 1.22rem;
      font-weight: 750;
      color: var(--ink);
      line-height: 1.22;
    }
    .triple-body {
      font-size: 0.98rem;
      line-height: 1.45;
      color: var(--ink);
    }
    .triple-lead {
      font-size: 1.05rem;
      color: var(--ink-muted);
      font-weight: 550;
      margin-bottom: 0.15rem;
    }
    .agenda-stack {
      display: flex;
      flex-direction: column;
      gap: 0.70rem;
    }
    .agenda-row {
      display: grid;
      grid-template-columns: 4.4rem 1fr;
      gap: 0.90rem;
      align-items: stretch;
      background: var(--surface);
      border: 1.5px solid var(--rule);
      border-radius: 12px;
      overflow: hidden;
      box-shadow: 0 3px 10px rgba(0,0,0,0.03);
    }
    .agenda-num {
      background: var(--accent-sf);
      color: var(--accent-dk);
      font-family: var(--font-code);
      font-weight: 800;
      font-size: 1.35rem;
      display: flex;
      align-items: center;
      justify-content: center;
      border-right: 1.5px solid var(--rule);
    }
    .agenda-copy {
      padding: 0.70rem 0.95rem 0.80rem 0;
    }
    .agenda-title {
      font-family: var(--font-display);
      font-weight: 750;
      font-size: 1.18rem;
      color: var(--ink);
      margin-bottom: 0.18rem;
    }
    .agenda-body {
      font-size: 0.95rem;
      line-height: 1.42;
      color: var(--ink);
    }
    .core-four-row {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 0.55rem;
      margin: 0.35rem 0 0.70rem;
    }
    .core-pill {
      background: var(--surface);
      border: 1.5px solid var(--rule);
      border-radius: 10px;
      padding: 0.70rem 0.75rem;
      box-shadow: 0 2px 8px rgba(0,0,0,0.03);
    }
    .core-pill-k {
      font-family: var(--font-code);
      font-size: 0.72rem;
      font-weight: 750;
      color: var(--accent-dk);
      letter-spacing: 0.04em;
      text-transform: uppercase;
    }
    .core-pill-t {
      font-family: var(--font-display);
      font-weight: 750;
      font-size: 1.05rem;
      color: var(--ink);
      margin: 0.12rem 0 0.10rem;
    }
    .core-pill-d {
      font-size: 0.80rem;
      color: var(--ink-muted);
      line-height: 1.30;
    }
    .ctrl-pills {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 0.40rem;
    }
    .ctrl-pill {
      background: var(--accent-sf);
      border: 1px solid var(--rule);
      border-radius: 8px;
      padding: 0.42rem 0.55rem;
      font-size: 0.82rem;
      font-weight: 650;
      color: var(--ink);
      text-align: center;
    }
    .thanks-wrap {
      height: 100%;
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 1.40rem;
      align-items: center;
    }
    .thanks-kicker {
      font-family: var(--font-code);
      font-weight: 750;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--accent-dk);
      font-size: 0.88rem;
    }
    .thanks-title {
      font-family: var(--font-display);
      font-size: 3.1rem;
      font-weight: 800;
      letter-spacing: -0.03em;
      line-height: 1.05;
      margin: 0.35rem 0 0.70rem;
    }
    .thanks-book {
      font-size: 1.08rem;
      line-height: 1.40;
      color: var(--ink);
      max-width: 28rem;
    }
    .thanks-link a {
      color: var(--accent-dk);
      font-weight: 700;
      font-family: var(--font-code);
      font-size: 0.95rem;
    }
    .thanks-cover {
      background: var(--surface);
      border: 1.5px solid var(--rule);
      border-radius: 14px;
      padding: 0.80rem;
      box-shadow: 0 8px 24px rgba(0,0,0,0.06);
      text-align: center;
    }
    .thanks-cover img {
      width: 100%;
      max-height: 52vh;
      object-fit: contain;
      border-radius: 8px;
    }
    @media (max-width: 980px) {
      .triple-grid, .core-four-row, .ctrl-pills, .thanks-wrap {
        grid-template-columns: 1fr 1fr;
      }
      .thanks-wrap { grid-template-columns: 1fr; }
    }
"""

JS = r"""
    const slidesData = SLIDES_JSON;
    const totalSlides = slidesData.length;
    let currentIdx = 0;
    let isGridMode = false;
    const selectEl = document.getElementById('slide-select');
    const bodyEl = document.getElementById('slide-body');

    slidesData.forEach((s, idx) => {
      const opt = document.createElement('option');
      opt.value = idx;
      opt.textContent = s.number + '. ' + (s.raw_lines[0] || 'Slide');
      selectEl.appendChild(opt);
    });
    const gotoInput = document.getElementById('goto-input');
    if (gotoInput) {
      gotoInput.max = String(totalSlides);
      gotoInput.title = 'Enter slide number (1-' + totalSlides + ')';
    }

    function esc(s) {
      return String(s)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;');
    }
    function rich(s) {
      return esc(s)
        .replace(/https:\/\/[^\s<]+/g, (m) => '<a href="' + m + '" target="_blank" rel="noopener noreferrer">' + m + '</a>')
        .replace(/`([^`]+)`/g, '<code>$1</code>');
    }
    function formatBullets(lines) {
      let html = '<ul class="main-bullets">';
      lines.forEach((line) => {
        const t = line.replace(/^[•\-\*]\s*/, '').trim();
        if (t) html += '<li class="bullet-group"><div class="primary-bullet">' + rich(t) + '</div></li>';
      });
      html += '</ul>';
      return html;
    }

    function renderTitle() {
      return `
        <div id="slide-content-wrap" class="slide-1-container">
          <div class="slide-1-hero-card">
            <div class="slide-1-hero-tagline">
              From Software Engineering to Harness Engineering
            </div>
            <div class="slide-1-hero-desc">
              Ontology defines intent. Governed order constrains action. Graph engineering is the multi-agent specialization under the harness umbrella &mdash; not a competing discipline.
            </div>
          </div>
          <div class="slide-1-instructor-card">
            <div class="slide-1-avatar-wrap">
              <img src="assets/images/ken-head-shot.png" alt="Ken Huang" class="slide-1-avatar-img" />
            </div>
            <div class="slide-1-instructor-info">
              <div class="slide-1-instructor-badge"><span>Keynote Speaker &middot; CSA GCR 2026</span></div>
              <div class="slide-1-instructor-name">Ken Huang, CISSP</div>
              <div class="slide-1-instructor-titles">
                <div class="slide-1-title-item">
                  <span class="title-icon">🏛️</span>
                  <span>Adjunct Professor, <span class="slide-1-title-highlight">University of San Francisco</span></span>
                </div>
                <div class="slide-1-title-item">
                  <span class="title-icon">🛡️</span>
                  <span>Vice President, <span class="slide-1-title-highlight">CSA Greater China Research Institute</span></span>
                </div>
                <div class="slide-1-title-item">
                  <span class="title-icon">🚀</span>
                  <span>CEO of <span class="slide-1-title-highlight">DistributedApps.ai</span></span>
                </div>
              </div>
            </div>
          </div>
          <div class="slide-1-pillars-row">
            <div class="slide-1-pillar-pill">
              <div class="slide-1-pillar-title">✍️ Prompt</div>
              <div class="slide-1-pillar-desc">Define the task, constraints, output, and stop</div>
            </div>
            <div class="slide-1-pillar-pill">
              <div class="slide-1-pillar-title">📚 Context</div>
              <div class="slide-1-pillar-desc">Give the right evidence, with provenance</div>
            </div>
            <div class="slide-1-pillar-pill">
              <div class="slide-1-pillar-title">🔁 Loop</div>
              <div class="slide-1-pillar-desc">Bound observe &rarr; plan &rarr; act &rarr; verify</div>
            </div>
            <div class="slide-1-pillar-pill">
              <div class="slide-1-pillar-title">🕸️ Graph</div>
              <div class="slide-1-pillar-desc">Govern multi-agent nodes, edges, and handoffs</div>
            </div>
          </div>
        </div>`;
    }

    function renderSpeaker(slide) {
      const rest = (slide.raw_lines || []).slice(1);
      return `
        <div id="slide-content-wrap" class="instructor-slide-grid">
          <div class="instructor-info-col">
            ${formatBullets(rest)}
          </div>
          <div class="author-books-card">
            <div class="author-books-header">
              <span>📚 AI Books &amp; Academic Publications (Springer · Cambridge · Wiley · Packt)</span>
              <a href="https://www.amazon.com/stores/author/B0D3J7L7GN" target="_blank" rel="noopener noreferrer">Amazon Author Page ➔</a>
            </div>
            <div class="books-gallery-grid">
              <a href="https://www.amazon.com/dp/3031900251" target="_blank" rel="noopener noreferrer" class="book-item-card" title="Agentic AI: Theories and Practices (Springer)">
                <img src="assets/images/books/springer_agentic_ai.jpg" alt="Agentic AI (Springer)" class="book-cover-img" />
                <div class="book-item-title">Agentic AI</div>
                <div class="book-publisher-tag">SPRINGER</div>
              </a>
              <a href="https://www.amazon.com/dp/3031448839" target="_blank" rel="noopener noreferrer" class="book-item-card" title="Beyond AI (Springer)">
                <img src="assets/images/books/springer_beyond_ai.jpg" alt="Beyond AI (Springer)" class="book-cover-img" />
                <div class="book-item-title">Beyond AI</div>
                <div class="book-publisher-tag">SPRINGER</div>
              </a>
              <a href="https://www.amazon.com/dp/3031542517" target="_blank" rel="noopener noreferrer" class="book-item-card" title="Generative AI Security (Springer)">
                <img src="assets/images/books/springer_generative_ai_security.jpg" alt="GenAI Security (Springer)" class="book-cover-img" />
                <div class="book-item-title">GenAI Security</div>
                <div class="book-publisher-tag">SPRINGER</div>
              </a>
              <a href="https://www.amazon.com/dp/3031901002" target="_blank" rel="noopener noreferrer" class="book-item-card" title="Securing AI Agents (Springer)">
                <img src="assets/images/books/springer_securing_ai_agents.jpg" alt="Securing AI Agents" class="book-cover-img" />
                <div class="book-item-title">Securing Agents</div>
                <div class="book-publisher-tag">SPRINGER</div>
              </a>
              <a href="https://www.amazon.com/dp/1009384467" target="_blank" rel="noopener noreferrer" class="book-item-card" title="Web3 (Cambridge)">
                <img src="assets/images/books/cambridge_web3.jpg" alt="Web3 (Cambridge UP)" class="book-cover-img" />
                <div class="book-item-title">Web3 &amp; Economy</div>
                <div class="book-publisher-tag">CAMBRIDGE</div>
              </a>
              <a href="https://www.amazon.com/dp/1394186524" target="_blank" rel="noopener noreferrer" class="book-item-card" title="Blockchain and Web3 (Wiley)">
                <img src="assets/images/books/wiley_blockchain_web3.jpg" alt="Blockchain & Web3 (Wiley)" class="book-cover-img" />
                <div class="book-item-title">Blockchain Web3</div>
                <div class="book-publisher-tag">WILEY</div>
              </a>
              <a href="https://www.amazon.com/dp/B0HF3F86YM" target="_blank" rel="noopener noreferrer" class="book-item-card" title="Harness Engineering">
                <img src="assets/images/books/harness_engineering.jpg" alt="Harness Engineering" class="book-cover-img" />
                <div class="book-item-title">Harness Eng.</div>
                <div class="book-publisher-tag">BEST SELLER</div>
              </a>
              <a href="https://www.amazon.com/dp/1807785017" target="_blank" rel="noopener noreferrer" class="book-item-card" title="OpenClaw AI in Production">
                <img src="assets/images/books/openclaw_ai_in_production.jpg" alt="OpenClaw AI in Production" class="book-cover-img" />
                <div class="book-item-title">OpenClaw AI</div>
                <div class="book-publisher-tag">PACKT</div>
              </a>
              <a href="https://www.amazon.com/dp/B0H8JW9XFN" target="_blank" rel="noopener noreferrer" class="book-item-card" title="Engineering Agentic AI with Claude">
                <img src="assets/images/books/engineering_agentic_ai_claude.jpg" alt="Engineering Agentic AI with Claude" class="book-cover-img" />
                <div class="book-item-title">Agentic Claude</div>
                <div class="book-publisher-tag">CLAUDE AI</div>
              </a>
              <a href="https://www.amazon.com/dp/1836207034" target="_blank" rel="noopener noreferrer" class="book-item-card" title="LLM Design Patterns">
                <img src="assets/images/books/llm_design_patterns.jpg" alt="LLM Design Patterns" class="book-cover-img" />
                <div class="book-item-title">LLM Patterns</div>
                <div class="book-publisher-tag">PACKT</div>
              </a>
              <a href="https://www.amazon.com/dp/B0H13XWS8W" target="_blank" rel="noopener noreferrer" class="book-item-card" title="Agentic AI Harness Pattern">
                <img src="assets/images/books/agentic_ai_harness_pattern.jpg" alt="Agentic AI Harness Pattern" class="book-cover-img" />
                <div class="book-item-title">AI Harness</div>
                <div class="book-publisher-tag">PATTERNS</div>
              </a>
              <a href="https://www.amazon.com/dp/B0DCBDGNTN" target="_blank" rel="noopener noreferrer" class="book-item-card" title="The Layperson's Handbook to Generative AI">
                <img src="assets/images/books/laypersons_handbook_genai.jpg" alt="Handbook to GenAI" class="book-cover-img" />
                <div class="book-item-title">GenAI Guide</div>
                <div class="book-publisher-tag">HANDBOOK</div>
              </a>
            </div>
          </div>
        </div>`;
    }

    function renderAgenda(slide) {
      const rows = (slide.agenda || []).map((row) => `
        <div class="agenda-row">
          <div class="agenda-num">${esc(row.num)}</div>
          <div class="agenda-copy">
            <div class="agenda-title">${esc(row.title)}</div>
            <div class="agenda-body">${rich(row.body)}</div>
          </div>
        </div>`).join('');
      return `<div id="slide-content-wrap"><div class="agenda-stack">${rows}</div></div>`;
    }

    function renderSection(slide) {
      return `
        <div id="slide-content-wrap" class="section-slide">
          <div class="section-kicker">${esc(slide.raw_lines[0] || '')}</div>
          <div class="section-title">${esc(slide.raw_lines[1] || '')}</div>
          <div class="section-sub">${esc(slide.raw_lines[2] || '')}</div>
          ${slide.kicker ? '<div class="triple-lead">' + esc(slide.kicker) + '</div>' : ''}
        </div>`;
    }

    function renderTriple(slide) {
      const cards = (slide.points || []).map((p) => `
        <div class="triple-card">
          <div class="triple-num">${esc(p.num)}</div>
          <div class="triple-title">${esc(p.title)}</div>
          <div class="triple-body">${rich(p.body)}</div>
        </div>`).join('');
      return `
        <div id="slide-content-wrap">
          <div class="triple-lead">${esc(slide.raw_lines[1] || '')}</div>
          <div class="triple-grid">${cards}</div>
        </div>`;
    }

    function renderComparison() {
      return `
        <div id="slide-content-wrap" class="thesis-slide-wrap">
          <div class="thesis-grid">
            <div class="thesis-card trad-card">
              <div class="thesis-card-header trad-header">
                <span class="thesis-icon">🏛️</span>
                <div>
                  <div class="thesis-title">Software Engineering</div>
                  <div class="thesis-subtitle">For specified, testable, repeatable behavior</div>
                </div>
                <span class="thesis-badge trad-badge">DETERMINISTIC</span>
              </div>
              <div class="thesis-card-body">
                <div class="thesis-point"><strong>What it includes:</strong> specs, design, and code; the test pyramid and CI/CD; release, ops, and SRE.</div>
                <div class="thesis-point"><strong>What it assumes:</strong> behavior is specified and testable. Logic encodes expected branches.</div>
                <div class="thesis-point"><strong>Engineering job:</strong> build software whose behavior is specified, tested, and repeatable.</div>
              </div>
            </div>
            <div class="thesis-card harn-card">
              <div class="thesis-card-header harn-header">
                <span class="thesis-icon">🛡️</span>
                <div>
                  <div class="thesis-title">Harness Engineering</div>
                  <div class="thesis-subtitle">Deterministic control for probabilistic agents</div>
                </div>
                <span class="thesis-badge harn-badge">AGENTIC AI</span>
              </div>
              <div class="thesis-card-body">
                <div class="core-four-row">
                  <div class="core-pill"><div class="core-pill-k">01</div><div class="core-pill-t">Prompt</div><div class="core-pill-d">Define the task</div></div>
                  <div class="core-pill"><div class="core-pill-k">02</div><div class="core-pill-t">Context</div><div class="core-pill-d">Provide evidence</div></div>
                  <div class="core-pill"><div class="core-pill-k">03</div><div class="core-pill-t">Loop</div><div class="core-pill-d">Bound execution</div></div>
                  <div class="core-pill"><div class="core-pill-k">04</div><div class="core-pill-t">Graph</div><div class="core-pill-d">Govern workflow</div></div>
                </div>
                <div class="thesis-point" style="margin-bottom:0.45rem;"><strong>Also part of the harness:</strong></div>
                <div class="ctrl-pills">
                  <div class="ctrl-pill">Automation</div>
                  <div class="ctrl-pill">Identity &amp; intent</div>
                  <div class="ctrl-pill">Memory</div>
                  <div class="ctrl-pill">Observability</div>
                  <div class="ctrl-pill">Runtime control</div>
                  <div class="ctrl-pill">Evaluation</div>
                  <div class="ctrl-pill">Scalability</div>
                  <div class="ctrl-pill">Token budget</div>
                </div>
                <div class="thesis-point" style="margin-top:0.55rem;">Extensions: skill · plug-in · MCP · hooks · CLI</div>
              </div>
            </div>
          </div>
        </div>`;
    }

    function renderThanks(slide) {
      return `
        <div id="slide-content-wrap" class="thanks-wrap">
          <div>
            <div class="thanks-kicker">CSA GCR 2026</div>
            <div class="thanks-title">Thank you</div>
            <div class="thanks-book">${esc(slide.raw_lines[1] || '')}</div>
            <div class="thanks-link" style="margin-top:0.85rem;">
              <a href="https://www.amazon.com/dp/B0HF3F86YM" target="_blank" rel="noopener noreferrer">amazon.com/dp/B0HF3F86YM ↗</a>
            </div>
            <div class="thanks-link" style="margin-top:0.35rem;">
              <a href="https://distributedapps.ai/" target="_blank" rel="noopener noreferrer">distributedapps.ai ↗</a>
              &nbsp;·&nbsp;
              <a href="https://kenhuangus.substack.com/" target="_blank" rel="noopener noreferrer">kenhuangus.substack.com ↗</a>
            </div>
          </div>
          <div class="thanks-cover">
            <a href="https://www.amazon.com/dp/B0HF3F86YM" target="_blank" rel="noopener noreferrer">
              <img src="assets/images/harness_engineering_book.png" alt="Harness Engineering book cover" />
            </a>
          </div>
        </div>`;
    }

    function renderSlide(idx) {
      if (idx < 0) idx = 0;
      if (idx >= slidesData.length) idx = slidesData.length - 1;
      currentIdx = idx;
      const slide = slidesData[idx];
      selectEl.value = idx;
      document.getElementById('slide-title').innerText = slide.raw_lines[0] || ('Slide ' + slide.number);
      document.getElementById('slide-num-badge').innerText = 'Slide ' + slide.number + ' of ' + slidesData.length;
      if (window.location.hash !== '#' + slide.number) {
        history.replaceState(null, '', '#' + slide.number);
      }
      document.getElementById('btn-prev').disabled = (idx === 0);
      document.getElementById('btn-next').disabled = (idx === slidesData.length - 1);

      let html = '';
      const t = slide.slide_type;
      if (t === 'title') html = renderTitle();
      else if (t === 'speaker') html = renderSpeaker(slide);
      else if (t === 'agenda') html = renderAgenda(slide);
      else if (t === 'section') html = renderSection(slide);
      else if (t === 'triple') html = renderTriple(slide);
      else if (t === 'comparison') html = renderComparison();
      else if (t === 'thanks') html = renderThanks(slide);
      else {
        html = '<div id="slide-content-wrap" class="slide-content-wrapper">' + formatBullets((slide.raw_lines || []).slice(1)) + '</div>';
      }
      bodyEl.innerHTML = html;

      bodyEl.style.setProperty('--fit-scale', '1.0');
      const wrapper = document.getElementById('slide-content-wrap') || bodyEl;
      const clientH = bodyEl.clientHeight;
      const targetH = clientH * 0.92;
      const tight = wrapper.querySelector('.slide-1-container, .instructor-slide-grid, .thesis-grid, .triple-grid, .agenda-stack, .thanks-wrap, .section-slide');
      const maxScale = tight ? 1.18 : 1.50;
      let scale = 1.0;
      let grow = 0;
      while (wrapper.offsetHeight < targetH && bodyEl.scrollHeight <= clientH && scale < maxScale && grow < 40) {
        scale += 0.05;
        bodyEl.style.setProperty('--fit-scale', scale.toFixed(2));
        grow++;
      }
      let shrink = 0;
      while ((bodyEl.scrollHeight > clientH || wrapper.offsetHeight > (clientH - 6)) && scale > 0.50 && shrink < 60) {
        scale -= 0.02;
        bodyEl.style.setProperty('--fit-scale', scale.toFixed(2));
        shrink++;
      }
      document.getElementById('progress-fill').style.width = (((idx + 1) / slidesData.length) * 100) + '%';
    }

    function renderGrid() {
      const grid = document.getElementById('grid-mode');
      grid.innerHTML = '';
      slidesData.forEach((slide, idx) => {
        const card = document.createElement('div');
        card.className = 'grid-slide-card';
        card.onclick = () => { isGridMode = true; toggleMode(); renderSlide(idx); };
        const title = slide.raw_lines[0] || ('Slide ' + slide.number);
        const body = (slide.raw_lines.slice(1, 3).join(' ') || '');
        card.innerHTML = '<div style="font-size:0.75rem;font-weight:800;margin-bottom:0.35rem;">SLIDE ' + slide.number + '</div>'
          + '<div class="grid-slide-title">' + esc(title) + '</div>'
          + '<div class="grid-slide-body">' + esc(body) + '</div>';
        grid.appendChild(card);
      });
    }
    function prevSlide() { renderSlide(currentIdx - 1); }
    function nextSlide() { renderSlide(currentIdx + 1); }
    function goToSlide(val) { renderSlide(parseInt(val, 10)); }
    function jumpToEnteredSlide() {
      const input = document.getElementById('goto-input');
      const val = parseInt(input.value, 10);
      if (!isNaN(val) && val >= 1 && val <= slidesData.length) {
        renderSlide(val - 1);
        input.value = '';
      } else {
        alert('Please enter a slide number between 1 and ' + slidesData.length + '.');
      }
    }
    function toggleMode() {
      isGridMode = !isGridMode;
      document.getElementById('presentation-mode').style.display = isGridMode ? 'none' : 'flex';
      document.getElementById('grid-mode').style.display = isGridMode ? 'grid' : 'none';
      document.getElementById('mode-text').innerText = isGridMode ? 'Presentation Mode' : 'Grid View';
      document.getElementById('mode-icon').innerText = isGridMode ? '📺' : '📜';
      if (isGridMode) renderGrid();
    }
    function toggleFullscreen() {
      if (!document.fullscreenElement) document.documentElement.requestFullscreen();
      else if (document.exitFullscreen) document.exitFullscreen();
    }
    document.addEventListener('keydown', (e) => {
      if (document.activeElement && document.activeElement.tagName === 'INPUT') return;
      if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') nextSlide();
      if (e.key === 'ArrowLeft' || e.key === 'PageUp') prevSlide();
      if (e.key === 'f' || e.key === 'F') toggleFullscreen();
      if (e.key === 'm' || e.key === 'M') toggleMode();
      if (e.key === 'g' || e.key === 'G') {
        e.preventDefault();
        const el = document.getElementById('goto-input');
        if (el) { el.focus(); el.select(); }
      }
    });
    window.addEventListener('resize', () => { if (!isGridMode) renderSlide(currentIdx); });
    function getInitialSlideIndex() {
      const hash = window.location.hash.replace('#', '');
      if (hash) {
        const num = parseInt(hash, 10);
        if (!isNaN(num)) {
          const found = slidesData.findIndex(s => s.number === num);
          if (found !== -1) return found;
        }
      }
      return 0;
    }
    window.addEventListener('hashchange', () => {
      const idx = getInitialSlideIndex();
      if (idx !== currentIdx) renderSlide(idx);
    });
    renderSlide(getInitialSlideIndex());
"""


def main() -> None:
    with open(CSS_PATH, "r", encoding="utf-8") as f:
        css = f.read()
    # Insert extra CSS before closing style
    if css.strip().endswith("</style>"):
        css = css.strip()[: -len("</style>")].rstrip() + "\n" + EXTRA_CSS + "\n  </style>"
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        slides = json.load(f)
    js = JS.replace("SLIDES_JSON", json.dumps(slides, ensure_ascii=False))

    html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Agentic AI Harness Engineering — CSA GCR 2026</title>
  <meta name="description" content="English keynote deck: from software engineering to harness engineering. Graph engineering is the multi-agent layer of the agent harness. Speaker: Ken Huang, CISSP.">
  <link rel="icon" type="image/svg+xml" href="favicon.svg">
  <link rel="icon" type="image/png" sizes="192x192" href="favicon.png">
  <link rel="apple-touch-icon" sizes="180x180" href="favicon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  __CSS__
</head>
<body>
  <header>
    <div class="header-left">
      <img src="assets/images/harness_app_icon.png" alt="Harness Engineering Logo" style="width:28px; height:28px; border-radius:6px; object-fit:cover; display:inline-block;" />
      <div class="brand-title">Harness Engineering · CSA GCR 2026</div>
    </div>
    <div class="controls">
      <a href="index.html" class="btn">🏠 Home Site</a>
      <button id="btn-grid" class="btn" onclick="toggleMode()"><span id="mode-icon">📜</span> <span id="mode-text">Grid View</span></button>
      <button id="btn-prev" class="btn" onclick="prevSlide()">❮ Prev</button>
      <select id="slide-select" class="slide-select" onchange="goToSlide(this.value)"></select>
      <div class="goto-group">
        <input type="number" id="goto-input" min="1" max="23" placeholder="#" class="goto-input" title="Enter slide number (1-23)" onkeydown="if(event.key==='Enter') jumpToEnteredSlide()">
        <button id="btn-goto" class="btn btn-goto" onclick="jumpToEnteredSlide()" title="Jump to entered slide number">Go ➔</button>
      </div>
      <button id="btn-next" class="btn" onclick="nextSlide()">Next ❯</button>
      <button id="btn-fullscreen" class="btn btn-primary" onclick="toggleFullscreen()">⛶ Fullscreen</button>
    </div>
  </header>
  <div class="progress-bar"><div id="progress-fill" class="progress-fill"></div></div>
  <main>
    <div id="presentation-mode" class="slide-viewport">
      <div class="slide-card">
        <div class="slide-header">
          <div class="slide-title-wrap">
            <div id="slide-title" class="slide-title">Slide Title</div>
          </div>
          <div id="slide-num-badge" class="slide-num-badge">Slide 1 / 23</div>
        </div>
        <div id="slide-body" class="slide-body"></div>
      </div>
    </div>
    <div id="grid-mode" class="grid-viewport" style="display:none;"></div>
  </main>
  <script>
__JS__
  </script>
</body>
</html>
"""
    html = html.replace("__CSS__", css).replace("__JS__", js)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", OUT_PATH, "bytes", os.path.getsize(OUT_PATH), "slides", len(slides))


if __name__ == "__main__":
    main()
