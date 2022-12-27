import pandas as pd
import numpy as np

import sys


def profile(reps, log_message):
    from time import time
    def decorator(f):
        def k(*args, **kwargs):
            print(log_message)
            start = time()
            for i in range(reps):
                f(*args, **kwargs)
            end = time()
            measure = (100*end - 100*start) / reps
            print("\t{}".format(measure))
            return f(*args, **kwargs)
        return k
    return decorator


if __name__ == '__main__':
    dataframe = pd.DataFrame.from_dict({
        "a": np.random.randn(2000),
        "b": np.random.randn(2000),
        "N": np.random.randint(100, 1000, (2000), dtype=np.int64),
        "x": "x",
    })
    
    def run_plain_pandas():
        from plain.func import integral_of_f
        
        @profile(10, "** Running plain Python with Pandas")
        def task() -> float:
            return integral_of_f(dataframe)
        
        return task
    
    def run_just_cython():
        from cython.func import integral_of_f
        
        @profile(10, "** Running plain Cython with Pandas")
        def task() -> float:
            return integral_of_f(dataframe)
        
        return task

    def run_typed_cython():
        from typedcython.func import integral_of_f
        
        @profile(10, "* Running Cython with explicit C-types")
        def task() -> float:
            return integral_of_f(dataframe)
        
        return task
    
    def run_unoptimized_sequential():
        from plainsequential.func import apply_integrate_f
        
        @profile(10, "* Running plain Python with Pandas and sequential optimization")
        def task() -> float:
            return apply_integrate_f(
                dataframe["a"].to_numpy(),
                dataframe["b"].to_numpy(),
                dataframe["N"].to_numpy()
            )
            return integral_of_f(dataframe)
        
        return task

    def run_optimized_cython():
        from sequential.func import apply_integrate_f
        
        @profile(10, "** Running Cython with explicit C-types and sequential optimization")
        def task() -> float:
            return apply_integrate_f(
                dataframe["a"].to_numpy(),
                dataframe["b"].to_numpy(),
                dataframe["N"].to_numpy()
            )
            return integral_of_f(dataframe)
        
        return task
    
    
    run_plain_pandas()()
    run_just_cython()()
    run_typed_cython()()
    print("")
    run_unoptimized_sequential()()
    run_optimized_cython()()
    