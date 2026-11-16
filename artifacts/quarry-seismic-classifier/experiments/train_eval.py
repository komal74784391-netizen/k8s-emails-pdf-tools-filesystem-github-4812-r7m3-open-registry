"""Training and validation entry point for the Quarry classifier."""

import json
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

from quarry.model import build_classifier, features_to_vector


def main():
    data_path = Path(__file__).resolve().parent.parent / "data" / "events_sample.csv"
    frame = pd.read_csv(data_path)
    X = features_to_vector(frame.to_dict("records"))
    y = frame["label"].tolist()
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=7)
    model = build_classifier()
    model.fit(x_train, y_train)
    accuracy = float(model.score(x_test, y_test))
    print(json.dumps({"validation_accuracy": round(accuracy, 3)}))


if __name__ == "__main__":
    main()
