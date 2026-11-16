"""Model wrapper around the gradient-boosted event classifier."""

from sklearn.ensemble import HistGradientBoostingClassifier

from quarry.features import FEATURE_NAMES


def build_classifier():
    return HistGradientBoostingClassifier(max_depth=6, learning_rate=0.08)


def features_to_vector(feature_rows):
    return [[row[name] for name in FEATURE_NAMES] for row in feature_rows]
