from sudokupy.python_code.sudoku import board_generate, encode
from sudokupy.python_code.solver import solve_logic, puzzle_generate

def test_board_generation():
    print("Testing board generation...")
    sudoku_id = 123456789  # Example ID
    board = board_generate(sudoku_id)
    assert isinstance(board, str) and len(board) == 81, "Board generation failed"
    print("Board generation passed!")

def test_encoding():
    print("Testing encoding...")
    sudoku_id = 123456789
    board = board_generate(sudoku_id)
    encoded_value = encode(board)
    assert isinstance(encoded_value, int), "Encoding failed"
    print("Encoding passed!")

def test_puzzle_generation():
    print("Testing puzzle generation...")
    sudoku_id = 123456789
    solution = board_generate(sudoku_id)
    puzzle = puzzle_generate(solution, list(range(81)))
    assert isinstance(puzzle, str) and len(puzzle) == 81, "Puzzle generation failed"
    print("Puzzle generation passed!")

def test_solver():
    print("Testing solver...")
    sudoku_id = 123456789
    solution = board_generate(sudoku_id)
    puzzle = puzzle_generate(solution, list(range(81)))
    candidates, solved_board = solve_logic(puzzle)
    assert isinstance(solved_board, str) and len(solved_board) == 81, "Solver failed"
    print("Solver passed!")

if __name__ == "__main__":
    test_board_generation()
    test_encoding()
    test_puzzle_generation()
    test_solver()
    print("All tests completed successfully!")