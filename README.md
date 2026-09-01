# Agentic AI Graph Engineering — Packt

English GitHub Pages edition of Ken Huang’s Packt graph engineering keynote.

**Live deck:** open `slides.html` (or the GitHub Pages URL after deploy).

## What this is

The source talk is the bilingual Google Slides deck
[Agentic AI Graph Engineering](https://docs.google.com/presentation/d/16UoKTeZEsF4ZGLOaSi_XjrtdbXMiXIUJ5IRTLp3ntDU/edit).
This site translates that deck into English and presents it in the same interactive template as
[the Packt Harness Engineering masterclass](https://kenhuangus.github.io/packt-harness/slides.html),
including the speaker introduction.

Thesis of the talk: software engineering specifies deterministic behavior; harness engineering is the surrounding control plane for probabilistic agents. Graph engineering is the multi-agent specialization under that umbrella.

## Files

| File | Role |
| --- | --- |
| `index.html` | Landing page (speaker, outline, link to the deck) |
| `slides.html` | 20-slide presentation (keyboard, Go-To, grid, fullscreen) |
| `slides_data.json` | English slide content |
| `build_english_deck.py` | Rebuilds `slides.html` from the JSON + Packt template CSS |
| `assets/images/` | Speaker photo, book covers, logos |

## Local preview

```bash
python -m http.server 8080
```

Then open `http://localhost:8080/slides.html`.

Rebuild after editing `slides_data.json`:

```bash
python build_english_deck.py
```

## Navigation

Arrow keys / Space / PageDown next · PageUp previous · `G` Go-To · `M` grid · `F` fullscreen.
