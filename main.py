import functions as fc


"""
Esse programa tem o intuito de resolver Sudokus de dificuldade fácil, média e difícil.
"""


# Segue aqui alguns modelos de Sudoku para serem resolvidos
sudoku_easy = [
	[0, 4, 0, 0, 0, 7, 1, 0, 0],
	[5, 3, 0, 0, 9, 0, 0, 7, 0],
	[0, 0, 7, 0, 6, 0, 9, 4, 0],
	[4, 0, 6, 0, 8, 0, 7, 5, 1],
	[0, 1, 0, 0, 0, 0, 6, 9, 0],
	[0, 5, 3, 0, 1, 0, 0, 0, 2],
	[9, 6, 0, 0, 3, 0, 0, 1, 0],
	[3, 7, 0, 0, 5, 1, 0, 0, 0],
	[1, 0, 0, 2, 0, 9, 3, 6, 7]
]
sudoku_medium = [
	[8, 0, 0, 1, 0, 0, 0, 7, 0],
	[0, 2, 0, 0, 4, 0, 8, 0, 0],
	[0, 6, 0, 7, 0, 0, 0, 0, 0],
	[0, 0, 0, 4, 7, 0, 9, 0, 8],
	[2, 4, 0, 0, 8, 0, 0, 0, 0],
	[0, 3, 8, 0, 0, 0, 0, 0, 5],
	[0, 8, 0, 6, 0, 4, 1, 0, 0],
	[9, 0, 0, 0, 0, 7, 2, 0, 4],
	[0, 0, 5, 8, 1, 0, 0, 0, 6]
]
sudoku_hard = [
	[0, 0, 4, 8, 6, 0, 0, 3, 0],
	[0, 0, 1, 0, 0, 0, 0, 9, 0],
	[8, 0, 0, 0, 0, 9, 0, 6, 0],
	[5, 0, 0, 2, 0, 6, 0, 0, 1],
	[0, 2, 7, 0, 0, 1, 0, 0, 0],
	[0, 0, 0, 0, 4, 3, 0, 0, 6],
	[0, 5, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 9, 0, 0, 0, 4, 0, 0],
	[0, 0, 0, 4, 0, 0, 0, 1, 5]
]
sudoku_hard2 = [
	[5, 8, 6, 0, 7, 0, 0, 0, 0],
	[0, 0, 0, 9, 0, 1, 6, 0, 0],
	[0, 0, 0, 6, 0, 0, 2, 5, 4],
	[0, 0, 7, 0, 0, 0, 0, 0, 0],
	[9, 0, 2, 0, 1, 0, 3, 0, 5],
	[0, 0, 5, 0, 9, 0, 0, 0, 0],
	[0, 9, 0, 0, 4, 0, 0, 0, 8],
	[0, 0, 3, 5, 0, 0, 0, 6, 0],
	[0, 0, 0, 0, 2, 0, 4, 7, 0]
]
sudoku_day_challange = [
	[0, 0, 0, 5, 0, 0, 3, 0, 0],
	[0, 7, 0, 0, 3, 2, 0, 0, 5],
	[0, 3, 0, 7, 6, 0, 0, 0, 9],
	[0, 0, 0, 4, 0, 7, 0, 0, 8],
	[0, 0, 0, 0, 0, 0, 0, 3, 0],
	[2, 5, 0, 0, 0, 0, 9, 0, 7],
	[7, 2, 0, 3, 0, 9, 5, 0, 0],
	[8, 9, 0, 2, 0, 0, 0, 0, 0],
	[0, 0, 5, 0, 0, 0, 0, 0, 6]
]


# Resoluções
# fc.sudoku_solver(sudoku_easy)
# fc.sudoku_solver(sudoku_medium)
# fc.sudoku_solver(sudoku_hard)
fc.sudoku_solver(sudoku_hard2)
# fc.sudoku_solver(sudoku_day_challange)
