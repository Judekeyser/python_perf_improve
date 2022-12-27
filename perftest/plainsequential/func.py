import numpy as np
import pandas as pd


def f(x: float) -> float:
    return x * (x - 1)

def integrate_f(a: float, b: float, N: int) -> float:
    s = 0
    dx = (b - a) / N
    for i in range(N):
        s += f(a + i * dx)
    return s * dx

def apply_integrate_f(
    col_a: np.ndarray,
    col_b: np.ndarray,
    col_N: np.ndarray
) -> np.ndarray:
    n = len(col_N)
    res = np.empty(n)
    
    for i in range(n):
        res[i] = integrate_f(col_a[i], col_b[i], col_N[i])
    return res