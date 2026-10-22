# JD_poster

Poster for the paper *Jacobian Descent for Multi-Objective Optimization* (arXiv:2406.16232).
The paper sources are in the `SimplexLab/JD_paper` repo (cloned next to this one as `../JD_paper`);
figures in `images/` are copied from there and from `../JD_Presentation`.

## Stack

- LaTeX with the `tcbposter` library of `tcolorbox`, A0 portrait, 3 columns.
- `symbols.sty` holds the math macros (`\upgrad`, `\jac`, `\vx`, ...), shared with `JD_Presentation`.
- Code shown on the poster lives in `code/` and is included with `\lstinputlisting`
  (verbatim content cannot go directly inside a `\posterbox` argument).
- A box can only be placed relative to boxes defined *earlier* in the source.

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
