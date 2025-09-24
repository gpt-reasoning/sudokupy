import os
import sys
from cffi import FFI
import numpy as np

# Determine the correct shared library extension and compiler
if os.name == "nt":
    lib_ext = ".dll"
    compiler = "gcc"  # Windows users need MinGW or similar
elif sys.platform == "darwin":
    lib_ext = ".dylib"
    compiler = "clang"  # macOS uses Clang
else:
    lib_ext = ".so"
    compiler = "gcc"

# Check if the compiler exists
def compiler_available(compiler_name):
    return os.system(f"{compiler_name} --version > nul 2>&1" if os.name == "nt" else f"which {compiler_name} > /dev/null 2>&1") == 0

if not compiler_available(compiler):
    raise RuntimeError(f"Compiler '{compiler}' not found! Install GCC (Linux), MinGW (Windows), or Clang (macOS).")

# Define paths to C code and shared library location
c_code_path = os.path.join("sudokupy", "c_code")
lib_path = os.path.join(c_code_path, f"libsolver{lib_ext}")

# Compile C code into a shared library if not already compiled
if not os.path.exists(lib_path):
    compile_cmd = f"{compiler} -O3 -shared -o {lib_path} -fPIC {c_code_path}/jczsolver.c {c_code_path}/sudoku.c"
    
    if os.name == "nt":
        compile_cmd += " -D_DLL"  # Ensures proper Windows DLL handling
    os.system(compile_cmd)

# Load the compiled shared library using cffi
ffi = FFI()
puzzle_solver = ffi.dlopen(os.path.abspath(lib_path))

ffi.cdef("""
    int JCZSolver(const char *puzzle, char *solution, int limit);
    void JCZGenerate(char *puzzle, int *perm);
""")

# Puzzle solver is based on JCZ-C solver
def puzzle_generate(inp, p):
    if type(inp) != str:
        inp = "".join(map(str, inp.tolist()))
    puzzle = ffi.new("char[]", inp.encode('utf-8'))
    perm = ffi.new("int[]", list(p))
    puzzle_solver.JCZGenerate(puzzle, perm)
    return ffi.string(puzzle).decode('utf-8')