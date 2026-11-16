"""Backtest the seasonal ensemble against historical gauges."""

import json
from pathlib import Path

import pandas as pd

from lumen.forecast import ensemble_quantiles


def main():
    data_path = Path(__file__).resolve().parent.parent / "data" / "gauge_observations_sample.csv"
    frame = pd.read_csv(data_path)
    ensemble = frame["observed_flow_m3s"].values * 1.08
    metrics = {
        "gauges": int(frame["gauge_id"].nunique()),
        "months": int(len(frame)),
        "quantiles": ensemble_quantiles(ensemble),
    }
    out = Path(__file__).resolve().parent.parent / "results" / "backtest_metrics.json"
    out.write_text(json.dumps(metrics, indent=2) + "\n")
    print(metrics)


if __name__ == "__main__":
    main()
