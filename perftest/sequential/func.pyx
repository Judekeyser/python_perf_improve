cimport numpy as np

import numpy as np
import pandas as pd


cdef np.float64_t f(np.float64_t x):
    return x * (x - 1)

cpdef np.float64_t integrate_f(np.float64_t a, np.float64_t b, np.int64_t N):
    cdef np.int64_t i
    cdef np.float64_t s, dx
    
    s = 0
    dx = (b - a) / N
    for i in range(N):
        s += f(a + i * dx)
    return s * dx

cpdef np.ndarray[np.float64_t] apply_integrate_f(
    np.ndarray[np.float64_t] col_a,
    np.ndarray[np.float64_t] col_b,
    np.ndarray[np.int64_t] col_N
):
    cdef Py_ssize_t i, n
    cdef np.ndarray[np.float64_t] res
    
    n = len(col_N)
    res = np.empty(n, dtype=np.float64)
    
    for i in range(n):
        res[i] = integrate_f(col_a[i], col_b[i], col_N[i])
    return res