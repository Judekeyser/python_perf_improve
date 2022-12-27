cimport numpy as np

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

def integral_of_f(dataframe: pd.DataFrame):
    integrate_inline = lambda x: integrate_f(x["a"], x["b"], x["N"])
    return dataframe.apply(integrate_inline, axis=1)