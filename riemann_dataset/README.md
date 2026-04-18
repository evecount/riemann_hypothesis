# Seven Perspectives on the Riemann Hypothesis

**A Unified Computational Exploration with 10,000 Zeros**

Jian Zhou — *Research in Number Theory* (submitted 2026-03-20)

## Abstract

We explore the Riemann Hypothesis through seven structurally interconnected numerical perspectives, computed from 10,000 non-trivial zeros of ζ(s):

1. **Unit circle characterization** — Li–Keiper map
2. **Li coefficient positivity** — λₙ > 0 for n = 1, …, 2,000 (with truncation bounds)
3. **Power sum symmetry** — Sₖ = 0 for odd k, Sₖ ∈ ℝ for even k
4. **GUE spacing statistics** — D_KS = 0.027 vs GUE, 0.307 vs Poisson
5. **Mertens function** — |M(x)|/√x < 0.90 for x ≤ 10⁷
6. **Möbius orthogonality** — all 1,229 primes p ≤ 10,000
7. **Explicit formula** — including 1/ζ(0) = −2 constant term

## Repository Structure

```
paper.tex          LaTeX source
paper.pdf          Compiled paper
data/              All computed datasets
  zeros_10000.npz    10,000 zeros (numpy compressed)
  zeros_10000.csv    10,000 zeros (CSV)
  li_lambda_2000.csv Li coefficients λ₁…λ₂₀₀₀
  power_sums_100.csv Power sums S₁…S₁₀₀
  zero_spacings_9999.csv  Normalized spacings
  mertens_10M.csv    M(x) at selected x ≤ 10⁷
  mobius_ortho_10000.csv  Möbius orthogonality R_p
  explicit_formula_comparison.csv  Explicit formula vs exact
  summary.json       Summary statistics
scripts/           Computation scripts
  v7_batch_zeros.py    Zero computation (batched)
  v7_batch_analysis.py Analysis pipeline
  theory_v7_10000zeros.py  Monolithic version
```

## Requirements

- Python 3.8+
- `mpmath`, `numpy`, `scipy`

## Citation

```bibtex
@article{Zhou2026SevenPerspectives,
  author  = {Jian Zhou},
  title   = {Seven Perspectives on the {Riemann} Hypothesis: A Unified Computational Exploration with 10,000 Zeros},
  journal = {Research in Number Theory},
  year    = {2026},
  note    = {Submitted}
}
```

## License

MIT
