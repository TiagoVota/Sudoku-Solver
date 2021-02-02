import numpy as np


# Mostrar a tabela de opções por linha
def print_t(options):
	for i in range(9):
		print(options[i])


# Função para verificar disponibilidade de um número num espaço
def is_avalible(space_ij, sudoku, num):
	(i, j) = space_ij

	square_i = i - i % 3  # início coluna do quadrado
	square_j = j - j % 3  # início linha do quadrado

	# Monstrando resultado para o quadrado
	for m in range(square_i, square_i + 3):
		for n in range(square_j, square_j + 3):
			if m == i and n == j:
				# Não precisar verificar o próprio espaço
				continue
			if sudoku[m, n] == num:
				return False
	
	# Mostrando o resultado para linha
	for n in range(9):
		if n // 3 == j // 3:
			# Não verificar novamente o mesmo quadrado
			continue
		if sudoku[i, n] == num:
			return False
	
	# Mostrando o resultado para a coluna
	for m in range(9):
		if m // 3 == i // 3:
			# Não verificar novamente o mesmo quadrado
			continue
		if sudoku[m, j] == num:
			return False
	
	return True


# Gerar o "sudoku" com as possibilidades de cada espaço
def gerator_initial_options(sudoku):
	sudoku_options = []

	for i in range(9):
		sudoku_options.append([])
		for j in range(9):
			sudoku_options[i].append([])

			# Avaliando se o espaço está vazio
			if sudoku[i][j] == 0:
				for k in range(1, 9 + 1):
					if is_avalible((i, j), sudoku, k):
						sudoku_options[i][j].append(k)
	
	return sudoku_options


# Função que tira números da tabela de opções
def remove_option(space_ij, sudoku_options, num):
	(i, j) = space_ij

	square_i = i - i % 3  # início coluna do quadrado
	square_j = j - j % 3  # início linha do quadrado

	# Removendo do quadrado
	for m in range(square_i, square_i + 3):
		for n in range(square_j, square_j + 3):
			if m == i and n == j:
				sudoku_options[i][j] = []
			if num in sudoku_options[m][n]:
				sudoku_options[m][n].remove(num)
	
	# Removendo da linha
	for n in range(9):
		if n // 3 == j // 3:
			# Não verificar novamente no quadrado
			continue
		if num in sudoku_options[i][n]:
			sudoku_options[i][n].remove(num)

	# Removendo da coluna
	for m in range(9):
		if m // 3 == i // 3:
			# Não verificar novamente no quadrado
			continue
		if num in sudoku_options[m][j]:
			sudoku_options[m][j].remove(num)


# Atualizar sudoku
def update_sudoku(space_ij, sudoku_up, num):
	# Função feita com o objetivo de deixar o código de outra função mais claro
	(i, j) = space_ij
	sudoku_up[i, j] = num
	

# Verifica se o número só aparece uma vez no quadrado e grava a sua posição caso isso aconteça
def is_unique_square(space_ij, sudoku_options, num):
	(i, j) = space_ij

	square_i = i - i % 3  # início coluna do quadrado
	square_j = j - j % 3  # início linha do quadrado

	sum_apparitions = 0  # Quantas vezes o número aparece
	for m in range(square_i, square_i + 3):
		if sum_apparitions > 1:
			# Critério de parada para muitas aparições
			break
		
		for n in range(square_j, square_j + 3):
			if num in sudoku_options[m][n]:
				unique_space = (m, n)
				sum_apparitions += 1
	
	if sum_apparitions == 1:
		return [True, unique_space]
	
	return [False]


# Verifica se o número só aparece uma vez na linha e grava a sua posição caso isso aconteça
def is_unique_row(space_ij, sudoku_options, num):
	(i, j) = space_ij

	sum_apparitions = 0  # Quantas vezes o número aparece
	for n in range(9):
		if sum_apparitions > 1:
			# Critério de parada para muitas aparições
			break
		
		if num in sudoku_options[i][n]:
			unique_space = (i, n)
			sum_apparitions += 1
	
	if sum_apparitions == 1:
		return [True, unique_space]
	
	return [False]


# Verifica se o número só aparece uma vez na coluna e grava a sua posição caso isso aconteça
def is_unique_column(space_ij, sudoku_options, num):
	(i, j) = space_ij

	sum_apparitions = 0  # Quantas vezes o número aparece
	for m in range(9):
		if sum_apparitions > 1:
			# Critério de parada para mais de uma aparição
			break
		
		if num in sudoku_options[m][j]:
			unique_space = (m, j)
			sum_apparitions += 1
	
	if sum_apparitions == 1:
		return [True, unique_space]
	
	return [False]


# Ver se o número é único no quadrado, linha ou coluna
def is_unique(space_ij, sudoku_options, num):
	(i, j) = space_ij

	square_i = i - i % 3  # início coluna do quadrado
	square_j = j - j % 3  # início linha do quadrado

	# Verificando no quadrado
	sum_apparitions = 0
	for m in range(square_i, square_i + 3):
		if sum_apparitions > 1:
			# Critério de parada por muitas aparições
			break
		
		for n in range(square_j, square_j + 3):
			if num in sudoku_options[m][n]:
				sum_apparitions += 1
	
	if sum_apparitions == 1:
		return True
	
	# Verificando na linhas
	sum_apparitions = 0
	for n in range(9):
		if sum_apparitions > 1:
			# Critério de parada por muitas aparições
			break
		
		if num in sudoku_options[i][n]:
			sum_apparitions += 1
	
	if sum_apparitions == 1:
		return True
	
	# Verificando nas colunas
	sum_apparitions = 0
	for m in range(9):
		if sum_apparitions > 1:
			# Critério de parada por muitas aparições
			break
		
		if num == sudoku_options[m][j]:
			sum_apparitions += 1
	
	if sum_apparitions == 1:
		return True

	# Caso não é único em nenhuma das opções
	return False


# Resolver sudoku
def sudoku_solver(sudoku):
	sudoku = np.asarray(sudoku)
	sudoku_up = np.copy(sudoku)
	print(sudoku)
	sudoku_options = gerator_initial_options(sudoku)

	sum_len, sum_changes = 42, 42  # Iniciando com um valor não nulo
	while sum_len != 0:
		# Critério de parada por exaustão
		if sum_changes == 0:
			print('Critério de parada ativado: não há mais movimentos a serem feitos no Sudoku!')
			break
		
		sum_len = 0  # Contador de quantas opções tem disponíveis
		sum_changes = 0  # Contagem de mudanças pelo primeiro método

		# Método de encontrar espaços com somente uma opção
		for i in range(9):
			for j in range(9):
				space_ij = (i, j)
				# Método única opção
				if len(sudoku_options[i][j]) == 1:
					num = sudoku_options[i][j][0]
					
					remove_option(space_ij, sudoku_options, num)
					update_sudoku(space_ij, sudoku_up, num)

					print('Número exclusivo:', num)
					print('i, j: {}, {}'.format(i + 1, j + 1))
					print('Sudoku_up: \n{}'.format(sudoku_up))
					sum_changes += 1
					continue
				
				# Método opção sozinha
				for num in sudoku_options[i][j]:
					if is_unique(space_ij, sudoku_options, num):
						
						remove_option(space_ij, sudoku_options, num)
						update_sudoku(space_ij, sudoku_up, num)

						print('Número único removido: {}; posição: {}, {}.'.format(num, i, j))
						print('Sudoku_up: \n{}'.format(sudoku_up))

						sum_changes += 1
						break
				
				# Caso não haja nenhuma alteração nas opções
				sum_len += len(sudoku_options[i][j])
		
		# Método para verificar únicas opções por quadrados
		if sum_changes == 0:
			# Percorrendo todos os quadrados
			for i in range(3):
				for j in range(3):
					for k in range(1, 9 + 1):
						result = is_unique_square((i * 3, j * 3), sudoku_options, k)
						
						if result[0]:
							print('Número removido quadrado: {}; Posição: {}, {}.'.format(k, result[1][0] + 1, result[1][1] + 1))
							remove_option(result[1], sudoku_options, k)
							update_sudoku(result[1], sudoku_up, k)
							print('Sudoku_up: \n{}'.format(sudoku_up))

							sum_changes += 1
							break
			
			# Percorrendo todas as linhas e colunas
			for i in range(9):
				for j in range(9):
					for k in range(1, 9 + 1):
						# removendo da linha
						result_row = is_unique_row((i, j), sudoku_options, k)
						
						if result_row[0]:
							print('Número removido linha: {}; Posição: {}, {}.'.format(k, result_row[1][0] + 1, result_row[1][1] + 1))
							remove_option(result_row[1], sudoku_options, k)
							update_sudoku(result_row[1], sudoku_up, k)
							print('Sudoku_up: \n{}'.format(sudoku_up))
							
							sum_changes += 1
							break
						
						# Removendo da coluna
						result_column = is_unique_column((i, j), sudoku_options, k)

						if result_column[0]:
							print('Número removido coluna: {}; Posição: {}, {}.'.format(k, result_column[1][0] + 1, result_column[1][1] + 1))
							remove_option(result_column[1], sudoku_options, k)
							update_sudoku(result_column[1], sudoku_up, k)
							print('Sudoku_up: \n{}'.format(sudoku_up))
							
							sum_changes += 1
							break
						
	return sudoku_up
