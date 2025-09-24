import numpy as np
from SudokuPy.python_code.puzzle_generator import board_decode
from SudokuPy.python_code.puzzle_solver import puzzle_generate

def sudokupy_gen(k):
    """
    Generates `k` Sudoku puzzles and their solutions.

    Args:
    - k (int): The number of puzzles and solutions to generate.

    Returns:
    - list: A list of tuples where each tuple contains a puzzle and its solution.
    """
    puzzles_and_solutions = []

    for _ in range(k):
        # Generate a random Sudoku ID
        board_encode = np.random.randint(18383222420692992) + np.random.randint(1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9) * 18383222420692992

        # Generate solution board and puzzle
        solution = board_decode(board_encode)
        puzzle = puzzle_generate(solution, np.random.permutation(81))

        # Append the puzzle and its solution to the list
        puzzles_and_solutions.append((puzzle, solution))

    return puzzles_and_solutions