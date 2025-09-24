from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy

setup(
    name='sudokupy',
    version='0.0.1',
    description='A Sudoku library',
    author='Your Name',
    author_email='your.email@example.com',
    packages=['your_package'],
    package_data={'your_package': ['data/sudoku_processed.csv.gz']},
    ext_modules=cythonize([Extension(
        "your_package.solver",
        sources=["c_code/jscsolver.c", "c_code/sudoku.c"],
        extra_compile_args=['-O3'],
    )]),
    include_dirs=[numpy.get_include()],
    install_requires=[
        'numpy',
        'gdown',
        'cffi',
    ],
)