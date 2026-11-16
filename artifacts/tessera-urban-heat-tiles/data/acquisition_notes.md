# Acquisition notes

- Source: harmonised Landsat 8/9 thermal bands, 2025-2026 acquisition windows.
- Reprojection: UTM zones per metropolitan area, resampled to 100 m.
- Cloud masking: Fmask 4.0, dilated by two pixels.
- Tiles are named `<metro>_<year>_<quarter>_t<row>_<col>.npy`.

The published release contains tiles through 2026-Q2 only.
