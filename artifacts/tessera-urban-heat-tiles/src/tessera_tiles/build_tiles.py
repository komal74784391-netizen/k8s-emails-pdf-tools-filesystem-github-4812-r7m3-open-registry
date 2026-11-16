"""Assemble land-surface temperature tiles from reprojected scenes."""

from pathlib import Path

import numpy as np


TILE_SIZE = 512


def normalise_tile(temperature_kelvin):
    values = np.asarray(temperature_kelvin, dtype=float)
    return (values - 273.15).round(2)


def tile_grid(scene, tile_size=TILE_SIZE):
    height, width = scene.shape[:2]
    for row in range(0, height, tile_size):
        for col in range(0, width, tile_size):
            yield scene[row : row + tile_size, col : col + tile_size]


def write_tile(path, array):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    np.save(path, array)
