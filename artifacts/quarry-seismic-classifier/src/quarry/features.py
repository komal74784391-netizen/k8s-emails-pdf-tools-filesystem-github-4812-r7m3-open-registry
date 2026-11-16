"""Feature extraction for regional seismic waveforms."""

import numpy as np


FEATURE_NAMES = ["peak_amplitude", "duration_s", "spectral_centroid_hz", "onset_sharpness"]


def extract_features(waveform, sample_rate_hz):
    waveform = np.asarray(waveform, dtype=float)
    spectrum = np.abs(np.fft.rfft(waveform))
    freqs = np.fft.rfftfreq(len(waveform), d=1.0 / sample_rate_hz)
    centroid = float((spectrum * freqs).sum() / (spectrum.sum() or 1.0))
    return {
        "peak_amplitude": float(np.max(np.abs(waveform))),
        "duration_s": round(len(waveform) / sample_rate_hz, 3),
        "spectral_centroid_hz": round(centroid, 3),
        "onset_sharpness": float(np.gradient(waveform)[:5].std()),
    }
