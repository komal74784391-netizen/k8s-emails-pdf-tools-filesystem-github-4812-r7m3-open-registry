"""Seasonal forecast ensemble utilities."""

import numpy as np


def ensemble_quantiles(ensemble, quantiles=(0.1, 0.5, 0.9)):
    ensemble = np.asarray(ensemble, dtype=float)
    return {q: float(np.quantile(ensemble, q)) for q in quantiles}


def bias_adjust(forecast, observed):
    forecast = np.asarray(forecast, dtype=float)
    observed = np.asarray(observed, dtype=float)
    return forecast + float((observed - forecast).mean())
