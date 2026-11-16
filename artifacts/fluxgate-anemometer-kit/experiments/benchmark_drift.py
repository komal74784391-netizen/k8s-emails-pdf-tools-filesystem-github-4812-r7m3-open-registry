"""Benchmark drift correction across historical deployment snapshots."""

import json
from pathlib import Path

import pandas as pd

from fluxgate.calibration import linear_drift_correction, flag_outliers


def main():
    data_path = Path(__file__).resolve().parent.parent / "data" / "sample_readings.csv"
    readings = pd.read_csv(data_path)
    corrected = linear_drift_correction(
        readings["sensor_speed_ms"], readings["reference_speed_ms"]
    )
    flags = flag_outliers(corrected)
    metrics = {
        "samples": int(len(readings)),
        "flagged": int(flags.sum()),
        "mean_abs_error_ms": round(float(abs(corrected - readings["reference_speed_ms"]).mean()), 3),
    }
    out = Path(__file__).resolve().parent.parent / "results" / "drift_benchmark.json"
    out.write_text(json.dumps(metrics, indent=2) + "\n")
    print(metrics)


if __name__ == "__main__":
    main()
