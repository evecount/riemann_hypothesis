# DATASET MANIFEST: The 10,000 Zero Dataset

This directory contains the foundational datasets used for the numerical validation of the **Lim-Gemini Resultant** and the **CISM Engine**.

## Data Specifications

- **Target:** The first 10,000 non-trivial zeros of the Riemann Zeta Function $\zeta(s)$.
- **Scope:** 
  - `zeros_10000.csv`: Raw coordinates of the zeros.
  - `li_lambda_2000.csv`: Computed Li coefficients for stability testing.
  - `power_sums_100.csv`: Geometric power sum signatures.
  - `mobius_ortho_10000.csv`: Data for Möbius alignment verification.

## Purpose

These datasets provide the "Inward Sighting" ground truth. The **CISM Engine** utilizes this high-fidelity data to verify the **Volume-Parity Residuals** across the first 1,000+ settlement nodes.

## Credits & Attribution

The foundational 10,000 Zero dataset utilized in this repository for numerical validation is based on the research and computation work of **Jian Zhou**.

If you utilize this baseline data in your own research, please cite the original source:

```bibtex
@article{Zhou2026SevenPerspectives,
  author  = {Jian Zhou},
  title   = {Seven Perspectives on the {Riemann} Hypothesis: A Unified Computational Exploration with 10,000 Zeros},
  journal = {Research in Number Theory},
  year    = {2026},
  note    = {Submitted}
}
```
