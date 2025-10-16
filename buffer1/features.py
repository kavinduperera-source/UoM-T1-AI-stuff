import numpy as np
from typing import Sequence

def feature_vector(x: np.ndarray) -> list[float]:
    """Compute basic features  for 1D signal x"""
    x = np.asarray(x, dtype=np.float64) 
    rms = np.sqrt(np.mean(x**2))
    zc = np.sum(x[:-1]*x[1:]<0) #if zero crossing, the product will be negative
    p2p = np.max(x) - np.min(x)
    MAD = np.mean(np.abs(np.diff(x)))

    return [f"{float(rms):.1f} , {float(zc):.1f} , {float(p2p):.1f} , {float(MAD):.1f}"]

