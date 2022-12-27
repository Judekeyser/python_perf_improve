from distutils.core import setup
from Cython.Build import cythonize

import numpy

setup(
    ext_modules=cythonize(
        [
            "perftest/cython/func.pyx",
            "perftest/typedcython/func.pyx",
            "perftest/sequential/func.pyx"
        ]
    ),
    include_dirs=[numpy.get_include()]
)