# python_perf_improve
Testing the performance improvement described in https://pandas.pydata.org/docs/user_guide/enhancingperf.html

# Set up

## Install Python

First, install Python on your machine.
I've tested the code with Python 3.9 and Python 3.10.
Below Python 3.7, I think it might not be a good idea.

On Windows, we recommand using Conda or Miniconda,
as it is less likely to destroy your system. Check out
https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html

You might also be interested in a Docker solution:
https://hub.docker.com/_/python

## Create a Python environment

Create a Python environment. If you have Python 3.7 or above,
you might just use the built-in solution:
```
python -m venv my_env_name
source my_env_name/bin/activate
```
If you are using Conda or Miniconda, you'd better create a conda env:
```
conda create --name my_env_name python=3.9
conda activate my_env_name
```
Make sure `pip` is installed in the environment (should be the default behavior):
```
pip -v
```
(Pip is a Package Installer for Python, and the de facto standard to handle package downloads.)
(Environments are a way to isolate a Python runtime and the packages installed in there,
so that you're running in an isolated workspace under control.)

## Install requirements

In order to play with the project, you need Pandas and Cython.
I haven't fixed any version, so likely you could also just do:
```
pip install pandas
pip install cython
```
Note that NumPy is a dependency of Pandas, so the first call should
install NumPy too; so you don't have to install it yourself.

## Building the Cython code

Since the project is using Cython code (`pyx` files) for some of the cases,
you need to compile it. (For that, your system should have a valid C compiler. The standard ones
are supported.)

In order to compile Cython code, run
```
python setup.py build_ext --inplace
```
This should terminate without error, and generate C files and compiled objects
in place (in the source directories).

# Running the experiment

Once the setup is finished, run the experiment:
```
python perftest/main.py
```
You should see a bunch of measures on the screen. On my computer, I got:
```
** Running plain Python with Pandas
*** Tic-Toc yields 27.020730590820314
** Running plain Cython with Pandas
*** Tic-Toc yields 11.93927001953125
** Running Cython with explicit C-types
*** Tic-Toc yields 2.655621337890625

** Running plain Python with Pandas and sequential optimization
*** Tic-Toc yields 45.21981201171875
** Running Cython with explicit C-types and sequential optimization
*** Tic-Toc yields 0.155859375
```