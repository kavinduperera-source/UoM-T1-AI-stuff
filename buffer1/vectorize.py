from typing import Sequence
import numpy as np
import math

def python_rms(seq: Sequence[float]) -> float:
    '''Calculate the RMS using pure (core) python'''
    sq_sum = sum(x**2 for x in seq)
    rms = math.sqrt(sq_sum/len(seq))
    return rms

def numpy_rms(arr: np.ndarray) -> float:
    '''NumPy-vectorized RMS implementation.'''
    rms = float(np.sqrt(np.mean(arr**2)))
    return rms