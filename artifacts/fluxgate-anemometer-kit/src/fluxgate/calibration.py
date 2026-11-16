"""Drift correction routines for coastal profiler anemometers."""

import numpy as np


def linear_drift_correction(speeds, reference_speeds):
    """Apply a least-squares gain correction between two speed series."""
    speeds = np.asarray(speeds, dtype=float)
    reference_speeds = np.asarray(reference_speeds, dtype=float)
    if speeds.shape != reference_speeds.shape:
        raise ValueError("speed series must have the same length")
    gain, offset = np.polyfit(speeds, reference_speeds, 1)
    return gain * speeds + offset


def flag_outliers(speeds, window=7, threshold=3.5):
    """Flag readings whose rolling z-score exceeds ``threshold``."""
    speeds = np.asarray(speeds, dtype=float)
    rolling = np.convolve(speeds, np.ones(window) / window, mode="same")
    residual = speeds - rolling
    scale = np.std(residual) or 1.0
    return np.abs(residual) > threshold * scale
