#!/usr/bin/env python3
"""High-contrast terracotta SVG diagrams for the Packt Graph Engineering deck."""

INK = "#141413"
MUTED = "#6B6B63"
ACCENT = "#D97757"
DK = "#BD5D3A"
SURFACE = "#FAF9F5"
TINT = "#F5E6DF"
WHITE = "#FFFFFF"
RULE = "#E3E0D6"
BLUE = "#1e40af"
BLUE_BG = "#EBF2FE"
GREEN = "#047857"
GREEN_BG = "#E6F7F0"


def _svg(slide_id: str, inner: str, h: int = 188) -> str:
    mid = f"arr-{slide_id}"
    return f'''<svg viewBox="0 0 800 {h}" class="slide-svg" role="img" aria-hidden="true">
  <defs>
    <marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="{DK}"/>
    </marker>
  </defs>
  {inner}
</svg>'''


def _box(x, y, w, h, title, sub="", fill=SURFACE, stroke=DK, title_size=14, sub_size=11):
    ty = y + (h / 2 + 5) if not sub else y + h / 2 - 6
    parts = [
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="{stroke}" stroke-width="2.4"/>',
        f'<text x="{x + w/2}" y="{ty}" fill="{INK}" font-family="Inter,system-ui,sans-serif" font-size="{title_size}" font-weight="800" text-anchor="middle">{title}</text>',
    ]
    if sub:
        parts.append(
            f'<text x="{x + w/2}" y="{ty + 18}" fill="{MUTED}" font-family="Inter,system-ui,sans-serif" font-size="{sub_size}" font-weight="600" text-anchor="middle">{sub}</text>'
        )
    return "\n  ".join(parts)


def _arrow(x1, y1, x2, y2, slide_id: str, label=""):
    mid = f"arr-{slide_id}"
    parts = [f'<path d="M {x1} {y1} L {x2} {y2}" stroke="{DK}" stroke-width="2.6" fill="none" marker-end="url(#{mid})"/>']
    if label:
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2 - 8
        parts.append(
            f'<text x="{mx}" y="{my}" fill="{DK}" font-family="Inter,system-ui,sans-serif" font-size="10" font-weight="800" text-anchor="middle">{label}</text>'
        )
    return "\n  ".join(parts)


def _label(x, y, text, size=12, fill=DK, anchor="middle", weight="800"):
    return f'<text x="{x}" y="{y}" fill="{fill}" font-family="Inter,system-ui,sans-serif" font-size="{size}" font-weight="{weight}" text-anchor="{anchor}">{text}</text>'


# Packt Harness slide 3 — Traditional SE vs Harness Engineering
THESIS_SVG = r'''<svg viewBox="0 0 880 140" class="slide-svg" role="img" aria-hidden="true">
  <defs>
    <marker id="thesis-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#BD5D3A"/>
    </marker>
  </defs>
  <g transform="translate(10, 5)">
    <rect x="0" y="0" width="395" height="128" rx="10" fill="#FAF9F5" stroke="#2563eb" stroke-width="2"/>
    <rect x="0" y="0" width="395" height="28" rx="10" fill="#EBF2FE" stroke="#2563eb" stroke-width="2"/>
    <text x="197" y="19" fill="#1e40af" font-family="Inter" font-size="12" font-weight="800" text-anchor="middle">TRADITIONAL SOFTWARE ENGINEERING</text>
    <text x="197" y="46" fill="#141413" font-family="Inter" font-size="10.5" font-weight="700" text-anchor="middle">Deterministic IT Systems: Explicit Logic &amp; Repeatable Outputs</text>
    <g transform="translate(12, 56)">
      <rect x="0" y="0" width="180" height="36" rx="5" fill="#FFFFFF" stroke="#E3E0D6"/>
      <text x="90" y="15" fill="#1e3a8a" font-family="Inter" font-size="9" font-weight="750" text-anchor="middle">SDLC · Agile · Architecture</text>
      <text x="90" y="28" fill="#6B6B63" font-family="Inter" font-size="8.5" text-anchor="middle">DevOps · CI/CD · Pyramids</text>
      <rect x="190" y="0" width="180" height="36" rx="5" fill="#FFFFFF" stroke="#E3E0D6"/>
      <text x="280" y="15" fill="#1e3a8a" font-family="Inter" font-size="9" font-weight="750" text-anchor="middle">SRE &amp; Secure-SDLC</text>
      <text x="280" y="28" fill="#6B6B63" font-family="Inter" font-size="8.5" text-anchor="middle">AppSec · SAST/DAST</text>
    </g>
    <rect x="12" y="98" width="370" height="22" rx="4" fill="#EBF2FE" stroke="#bfdbfe"/>
    <text x="197" y="113" fill="#1e40af" font-family="JetBrains Mono" font-size="9.5" font-weight="700" text-anchor="middle">Formula: f(x) → y  [Strict Input-Output Repeatability]</text>
  </g>
  <g transform="translate(410, 54)">
    <path d="M 0 15 L 56 15" stroke="#BD5D3A" stroke-width="2.5" stroke-dasharray="4 3" marker-end="url(#thesis-arrow)"/>
    <rect x="4" y="3" width="48" height="24" rx="4" fill="#F5E6DF" stroke="#BD5D3A" stroke-width="1.2"/>
    <text x="28" y="15" fill="#BD5D3A" font-family="Inter" font-size="7.5" font-weight="850" text-anchor="middle">PARADIGM</text>
    <text x="28" y="23" fill="#BD5D3A" font-family="Inter" font-size="6.8" font-weight="800" text-anchor="middle">SHIFT</text>
  </g>
  <g transform="translate(475, 5)">
    <rect x="0" y="0" width="395" height="128" rx="10" fill="#FAF9F5" stroke="#059669" stroke-width="2"/>
    <rect x="0" y="0" width="395" height="28" rx="10" fill="#E6F7F0" stroke="#059669" stroke-width="2"/>
    <text x="197" y="19" fill="#047857" font-family="Inter" font-size="12" font-weight="800" text-anchor="middle">HARNESS ENGINEERING FOR AGENTIC AI</text>
    <text x="197" y="46" fill="#141413" font-family="Inter" font-size="10.5" font-weight="700" text-anchor="middle">Non-Deterministic Systems: Model + Emergent Behavior</text>
    <g transform="translate(12, 56)">
      <rect x="0" y="0" width="180" height="36" rx="5" fill="#FFFFFF" stroke="#E3E0D6"/>
      <text x="90" y="15" fill="#BD5D3A" font-family="Inter" font-size="9" font-weight="750" text-anchor="middle">Probabilistic Core</text>
      <text x="90" y="28" fill="#6B6B63" font-family="Inter" font-size="8.5" text-anchor="middle">Model · Prompts · Context · Tools</text>
      <rect x="190" y="0" width="180" height="36" rx="5" fill="#FFFFFF" stroke="#059669" stroke-width="1.2"/>
      <text x="280" y="15" fill="#047857" font-family="Inter" font-size="9" font-weight="750" text-anchor="middle">Deterministic Control Harness</text>
      <text x="280" y="28" fill="#6B6B63" font-family="Inter" font-size="8.5" text-anchor="middle">Memory · Sandbox · Hooks · TDA</text>
    </g>
    <rect x="12" y="98" width="370" height="22" rx="4" fill="#E6F7F0" stroke="#a7f3d0"/>
    <text x="197" y="113" fill="#047857" font-family="Inter" font-size="9.5" font-weight="800" text-anchor="middle">Goal: Reliable · Observable · Secure · Governable · Manageable</text>
  </g>
</svg>'''


HARNESS_STACK_SVG = _svg("s4", f'''
  {_box(150, 8, 500, 62, "Harness Engineering", "deterministic control plane for agentic systems", fill=GREEN_BG, stroke=GREEN, title_size=20, sub_size=13)}
  <path d="M 400 70 L 400 88" stroke="{DK}" stroke-width="2.6"/>
  <path d="M 90 88 L 710 88" stroke="{DK}" stroke-width="2.4"/>
  {_arrow(90, 88, 90, 108, "s4")}
  {_arrow(246, 88, 246, 108, "s4")}
  {_arrow(400, 88, 400, 108, "s4")}
  {_arrow(556, 88, 556, 108, "s4")}
  {_arrow(710, 88, 710, 108, "s4")}
  {_box(20, 110, 140, 78, "Prompt", "engineering")}
  {_box(176, 110, 140, 78, "Context", "engineering")}
  {_box(330, 110, 140, 78, "Loop", "engineering")}
  {_box(486, 110, 140, 78, "Graph", "engineering", fill=TINT)}
  {_box(640, 110, 140, 78, "Memory", "engineering")}
''', 196)


SVG_MAP = {
    "1": _svg("s1", f'''
  {_label(400, 20, "A multi-agent graph inside the harness — not a replacement for it", 14)}
  <rect x="24" y="32" width="752" height="148" rx="14" fill="{WHITE}" stroke="{DK}" stroke-width="2.6"/>
  {_label(48, 54, "HARNESS", 11, MUTED, "start")}
  {_box(48, 66, 148, 58, "Planner", "one loop")}
  {_arrow(196, 95, 230, 95, "s1", "typed")}
  {_box(238, 66, 160, 58, "Implementer", "one loop", fill=TINT)}
  {_arrow(398, 95, 432, 95, "s1", "typed")}
  {_box(440, 66, 148, 58, "Reviewer", "one loop")}
  {_arrow(588, 95, 622, 95, "s1")}
  {_box(630, 66, 124, 58, "Done", "", fill=GREEN_BG, stroke=GREEN)}
  {_box(238, 136, 200, 34, "human / fallback", "", fill=TINT, title_size=12)}
  <path d="M 514 124 L 514 153 L 438 153" stroke="{DK}" stroke-width="2.2" fill="none" marker-end="url(#arr-s1)"/>
''', 188),

    "2": _svg("s2", f'''
  {_box(20, 28, 180, 70, "Author", "Harness · MAESTRO")}
  {_arrow(200, 63, 238, 63, "s2")}
  {_box(240, 28, 180, 70, "Professor", "Univ. of San Francisco")}
  {_arrow(420, 63, 458, 63, "s2")}
  {_box(460, 28, 150, 70, "OWASP", "AIVSS · LLM Top 10")}
  {_arrow(610, 63, 648, 63, "s2")}
  {_box(650, 28, 130, 70, "CSA", "AI Safety WGs")}
  {_label(400, 128, "One speaker  ·  books, standards, and production harnesses", 13, MUTED)}
''', 140),

    "3": THESIS_SVG,

    "4": HARNESS_STACK_SVG,

    "5": _svg("s6", f'''
  {_box(20, 40, 200, 108, "01  Ontology", "entities · relations · rules")}
  {_arrow(230, 94, 268, 94, "s6")}
  {_box(276, 40, 230, 108, "02  Intent", "goal · object · success")}
  {_arrow(516, 94, 554, 94, "s6")}
  {_box(562, 40, 218, 108, "03  Harness check", "action vs intent + policy", fill=TINT)}
  {_label(400, 28, "No ontology  →  no authorized action", 13, DK)}
''', 170),

    "6": _svg("s7", f'''
  {_label(196, 24, "ONE AGENT LOOP", 13, MUTED)}
  {_label(608, 24, "MULTI-AGENT GRAPH", 13, DK)}
  <rect x="16" y="36" width="352" height="136" rx="12" fill="{WHITE}" stroke="{RULE}" stroke-width="2.2"/>
  {_box(32, 56, 100, 96, "Prompt", "task")}
  {_box(142, 56, 100, 96, "Context", "evidence")}
  {_box(252, 56, 100, 96, "Loop", "bounds")}
  {_arrow(378, 104, 420, 104, "s7", "fan-out")}
  <rect x="428" y="36" width="356" height="136" rx="12" fill="{TINT}" stroke="{DK}" stroke-width="2.4"/>
  {_box(444, 56, 104, 96, "Plan", "node")}
  {_box(556, 56, 104, 96, "Impl.", "node")}
  {_box(668, 56, 100, 96, "Review", "node")}
''', 184),

    "7": _svg("s8", f'''
  {_box(16, 36, 300, 120, "Trusted instructions", "goal · constraints · output · stop", fill=GREEN_BG, stroke=GREEN)}
  {_box(332, 70, 136, 52, "TRUST BOUNDARY", "", fill=TINT, title_size=11)}
  {_box(484, 36, 300, 120, "Untrusted data", "tickets · retrieval · user text", fill=WHITE)}
''', 176),

    "8": _svg("s9", f'''
  {_box(16, 36, 150, 120, "Corpus", "too much", fill=WHITE, stroke=RULE)}
  {_arrow(176, 96, 214, 96, "s9", "select")}
  {_box(222, 36, 250, 120, "This decision only", "source · freshness · scope", fill=TINT)}
  {_arrow(482, 96, 520, 96, "s9")}
  {_box(528, 36, 256, 120, "Context window", "policy outranks retrieval", fill=GREEN_BG, stroke=GREEN)}
''', 176),

    "9": _svg("s10", f'''
  {_box(40, 18, 160, 70, "Observe", "")}
  {_arrow(210, 53, 248, 53, "s10")}
  {_box(256, 18, 160, 70, "Plan", "")}
  {_arrow(426, 53, 464, 53, "s10")}
  {_box(472, 18, 140, 70, "Act", "")}
  {_arrow(622, 53, 660, 53, "s10")}
  {_box(668, 18, 112, 70, "Verify", "", fill=TINT)}
  <path d="M 724 88 L 724 118 L 120 118 L 120 88" stroke="{DK}" stroke-width="2.4" fill="none" marker-end="url(#arr-s10)"/>
  {_label(400, 168, "Bounds: steps · time · cost · retries   —   no progress → STOP", 13)}
''', 180),

    "10": _svg("s11", f'''
  {_box(28, 12, 132, 72, "Plan", "one job", fill=WHITE)}
  {_arrow(160, 48, 196, 48, "s11", "typed")}
  {_box(204, 12, 148, 72, "Implement", "one job")}
  {_arrow(352, 48, 388, 48, "s11", "typed")}
  {_box(396, 12, 132, 72, "Review", "one job", fill=TINT)}
  {_arrow(528, 48, 564, 48, "s11")}
  {_box(572, 12, 200, 72, "Done / merge", "", fill=GREEN_BG, stroke=GREEN, title_size=14)}
  <path d="M 462 84 L 462 118 L 204 118" stroke="{DK}" stroke-width="2.4" fill="none" marker-end="url(#arr-s11)"/>
  {_box(48, 96, 150, 40, "exception owner", "", fill=TINT, title_size=12)}
  {_label(400, 168, "Archetypes: sequential  ·  parallel  ·  reviewer  ·  conditional", 13)}
''', 180),

    "11": _svg("s12", f'''
  {_box(300, 62, 200, 64, "Agent run", "probabilistic core", fill=WHITE)}
  {_box(20, 16, 150, 48, "Automation", "", title_size=13)}
  {_box(210, 16, 150, 48, "Identity", "", title_size=13)}
  {_box(440, 16, 150, 48, "Memory", "", title_size=13)}
  {_box(630, 16, 150, 48, "Observability", "", title_size=13)}
  {_box(20, 124, 150, 48, "Runtime", "", title_size=13)}
  {_box(210, 124, 150, 48, "Evaluation", "", title_size=13)}
  {_box(440, 124, 150, 48, "Scalability", "", title_size=13)}
  {_box(630, 124, 150, 48, "Token budget", "", title_size=13)}
''', 184),

    "12": _svg("s13", f'''
  {_box(16, 36, 130, 100, "Start", "harness")}
  {_arrow(156, 86, 188, 86, "s13")}
  {_box(196, 36, 140, 100, "Sandbox", "isolated runtime")}
  {_arrow(346, 86, 378, 86, "s13")}
  {_box(386, 36, 150, 100, "Allowlist", "approved tools")}
  {_arrow(546, 86, 578, 86, "s13")}
  {_box(586, 36, 198, 100, "Stop", "human set the boundary", fill=TINT)}
''', 168),

    "13": _svg("s14", f'''
  {_box(16, 40, 150, 108, "Principal", "who acts")}
  {_arrow(176, 94, 208, 94, "s14")}
  {_box(216, 40, 140, 108, "Task ID", "this run")}
  {_arrow(366, 94, 398, 94, "s14")}
  {_box(406, 40, 170, 108, "Short credential", "time-boxed")}
  {_arrow(586, 94, 618, 94, "s14")}
  {_box(626, 40, 158, 108, "Tool auth", "vs stated intent", fill=TINT)}
''', 172),

    "14": _svg("s15", f'''
  {_box(20, 36, 230, 116, "Write", "named purpose + scope", fill=WHITE)}
  {_arrow(260, 94, 298, 94, "s15")}
  {_box(306, 36, 230, 116, "Isolate", "user · task · retention")}
  {_arrow(546, 94, 584, 94, "s15")}
  {_box(592, 36, 188, 116, "Roll back", "poison = incident", fill=TINT)}
''', 172),

    "15": _svg("s16", f'''
  {_box(20, 36, 210, 116, "Decision", "why this action")}
  {_arrow(240, 94, 278, 94, "s16", "trace")}
  {_box(286, 36, 220, 116, "Tool call", "what ran")}
  {_arrow(516, 94, 554, 94, "s16", "trace")}
  {_box(562, 36, 218, 116, "Artifact", "reconstruct high-risk", fill=TINT)}
''', 172),

    "16": _svg("s17", f'''
  <rect x="40" y="70" width="720" height="28" rx="8" fill="{TINT}" stroke="{DK}" stroke-width="2.2"/>
  {_label(400, 89, "LIVE RUN  —  still interruptible", 14, INK)}
  {_box(40, 16, 160, 42, "Pause", "", title_size=14)}
  {_box(240, 16, 160, 42, "Stop", "", title_size=14)}
  {_box(440, 16, 160, 42, "Change policy", "", title_size=14)}
  {_box(640, 16, 120, 42, "Checkpoint", "", title_size=13, fill=TINT)}
  {_box(200, 118, 400, 50, "No interrupt path  =  unsupervised execution", "", fill=WHITE, title_size=14)}
''', 180),

    "17": _svg("s18", f'''
  {_box(20, 40, 220, 112, "Change", "prompt · tool · model")}
  {_arrow(250, 96, 292, 96, "s18")}
  {_box(300, 28, 200, 136, "EVAL GATE", "success AND boundary", fill=TINT, title_size=16)}
  {_arrow(510, 70, 558, 70, "s18")}
  {_box(566, 20, 210, 70, "Release", "full autonomy", fill=GREEN_BG, stroke=GREEN)}
  {_arrow(510, 122, 558, 122, "s18")}
  {_box(566, 102, 210, 62, "Block / reduce", "failed evaluation", fill=WHITE)}
''', 180),

    "18": _svg("s19", f'''
  {_box(16, 40, 180, 112, "Admit", "backpressure first")}
  {_arrow(206, 96, 244, 96, "s19")}
  {_box(252, 16, 150, 70, "Tenant A", "isolated")}
  {_box(252, 98, 150, 70, "Tenant B", "isolated")}
  {_arrow(412, 96, 450, 96, "s19")}
  {_box(458, 40, 322, 112, "Idempotent retry", "scale must not multiply harm", fill=TINT)}
''', 176),

    "19": _svg("s20", f'''
  {_label(400, 28, "Token + tool-output budget per node and per graph", 14)}
  <rect x="60" y="52" width="680" height="44" rx="10" fill="{WHITE}" stroke="{DK}" stroke-width="2.4"/>
  <rect x="64" y="56" width="470" height="36" rx="8" fill="{TINT}"/>
  {_label(300, 80, "consumed", 13, DK)}
  {_label(700, 80, "CAP", 13, DK)}
  {_box(220, 116, 360, 52, "Hit the ceiling → STOP and report", "never continue silently", fill=TINT, title_size=15, sub_size=12)}
''', 180),

    "20": _svg("s21", f'''
  {_box(16, 28, 128, 56, "skill", "")}
  {_box(16, 100, 128, 56, "plugin", "")}
  {_box(656, 28, 128, 56, "MCP", "")}
  {_box(656, 100, 128, 56, "hooks", "")}
  {_box(328, 136, 144, 36, "CLI", "", title_size=13)}
  {_arrow(144, 56, 288, 84, "s21")}
  {_arrow(144, 128, 288, 104, "s21")}
  {_arrow(656, 56, 512, 84, "s21")}
  {_arrow(656, 128, 512, 104, "s21")}
  {_arrow(400, 136, 400, 128, "s21")}
  {_box(296, 40, 208, 88, "This node", "scoped tools only", fill=TINT)}
''', 180),

    "21": _svg("s22", f'''
  {_box(16, 40, 230, 116, "Inventory + approve", "every skill, tool, server")}
  {_arrow(256, 98, 294, 98, "s22")}
  {_box(302, 40, 230, 116, "Least privilege", "typed · scoped creds")}
  {_arrow(542, 98, 580, 98, "s22")}
  {_box(588, 40, 196, 116, "Validate / revoke", "fail policy → out", fill=TINT)}
''', 172),

    "22": _svg("s23", f'''
  {_label(400, 44, "Fan-out only when one loop is not enough.", 18)}
  {_label(400, 80, "A graph without a harness is a retry loop with more processes.", 14, MUTED)}
  {_box(120, 108, 560, 52, "typed edges  ·  scoped credentials  ·  exception owners", "", fill=TINT, title_size=14)}
''', 172),
}
