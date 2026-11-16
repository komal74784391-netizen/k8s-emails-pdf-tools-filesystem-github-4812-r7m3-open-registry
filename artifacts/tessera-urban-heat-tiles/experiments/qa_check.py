"""Quality checks for the urban heat island tile set."""

import json
from pathlib import Path

import pandas as pd


def main():
    index_path = Path(__file__).resolve().parent.parent / "data" / "sample_tile_index.csv"
    index = pd.read_csv(index_path)
    report = {
        "tiles_indexed": int(len(index)),
        "metros": int(index["metro"].nunique()),
        "null_pixels": int(index["valid_pixels"].isna().sum()),
        "max_surface_temp_c": float(index["mean_surface_temp_c"].max()),
    }
    out = Path(__file__).resolve().parent.parent / "results" / "qa_report.json"
    out.write_text(json.dumps(report, indent=2) + "\n")
    print(report)


if __name__ == "__main__":
    main()
