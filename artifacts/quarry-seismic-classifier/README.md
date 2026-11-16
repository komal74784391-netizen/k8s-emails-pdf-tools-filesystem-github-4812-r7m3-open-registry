# Quarry — Shallow Seismic Event Classifier

Gradient-boosted classifier for shallow seismic events recorded by regional
arrays.

**Release status:** Public release v2.3.0 — 2026-06-30.
**License:** MIT

## Layout

- `src/quarry/` — feature extraction and model training code
- `data/events_sample.csv` — de-identified sample events
- `experiments/train_eval.py` — training and validation harness
- `results/validation_report.json` — held-out validation metrics
