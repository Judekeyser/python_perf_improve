import pandas as pd

def f(x: float) -> float:
    return x * (x - 1)

def integrate_f(a: float, b: float, N: int) -> float:
    s = 0
    dx = (b - a) / N
    for i in range(N):
        s += f(a + i * dx)
    return s * dx

def integral_of_f(dataframe: pd.DataFrame):
    integrate_inline = lambda x: integrate_f(x["a"], x["b"], x["N"])
    return dataframe.apply(integrate_inline, axis=1)