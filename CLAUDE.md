# JD_poster

Poster for the paper *Jacobian Descent for Multi-Objective Optimization* (arXiv:2406.16232).
The paper sources are in the `SimplexLab/JD_paper` repo (cloned next to this one as `../JD_paper`);
figures in `images/` are copied from there and from `../JD_Presentation`.

## Stack

- LaTeX with the `tcbposter` library of `tcolorbox`, 140 cm × 90 cm landscape, 4 columns
  (NeurIPS 2026 main conference format: https://neurips.cc/Conferences/2026/PosterInstructions).
- Styled after the NeurIPS poster template (`pptTemplate.pptx`): white background, plain section headers,
  colors from the NeurIPS logo (purple `#68448B` accent, charcoal `#323539` headers, slate `#344854` text).
- `symbols.sty` holds the math macros (`\upgrad`, `\jac`, `\vx`, ...), shared with `JD_Presentation`.
- Code shown on the poster lives in `code/` and is included with `\lstinputlisting`
  (verbatim content cannot go directly inside a `\posterbox` argument).
- A box can only be placed relative to boxes defined *earlier* in the source.
- Images must be vector (PDF/SVG) or very high resolution; check with `pdfimages -list main.pdf`.
  - `images/logos/torchjd.pdf` comes from `../TorchJD/docs/source/icons/TorchJD_text.svg` with black
    replaced by `#323539`, exported with `inkscape --export-text-to-path` (the wordmark needs the free
    "Louis George Cafe" font installed).
  - `images/logos/simplexlab.pdf` is the white SimplexLab logo with the triangle and the dot of the "i"
    recolored to `#529D68` (the green of the SimplexLab GitHub avatar) and the text to `#323539`.
  - `images/logos/neurips.pdf` comes from https://neurips.cc/static/core/img/NeurIPS-logo.svg.
  - `images/CQF_values.pdf` comes from `../TorchJD/tests/trajectories/` (see its CONTRIBUTING.md),
    plotted with `savefig.dpi: 600` in a `matplotlibrc` so the embedded heatmaps are high resolution.

## Workflow

After every change, compile and look at the result:

```bash
latexmk -pdf -interaction=nonstopmode main.tex
pdftoppm -png -r 25 -singlefile main.pdf preview      # whole poster
pdftoppm -png -r 50 -x X -y Y -W W -H H -singlefile main.pdf crop   # zoom on a region
```

Check that no box content overflows into the next box (overflow is silent in `tcbposter`),
and grep `main.log` for `^!` and `Overfull`.

Numbers on the poster must match the paper; check them against `../JD_paper/content/`.
