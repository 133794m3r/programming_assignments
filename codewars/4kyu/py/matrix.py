def determinant(matrix):
	i = 0
	n = len(matrix)
	P = [i for i in range(n)]
	ip = 0
	det = 1.0
	if n == 1:
		return matrix[0]
	for i in range(n - 1):
		ip = i
		max_matrix = abs(matrix[P[i]][i])
		for j in range(i + 1, n):
			candidate_matrix = abs(matrix[P[j]][i])
			if candidate_matrix > max_matrix:
				max_matrix = candidate_matrix
				ip = j

		if ip != i:
			P[i], P[ip] = P[ip], P[i]
			det = -det
		ipos = P[i]
		det *= matrix[ipos][i]
		for j in range(i + 1, n):
			jpos = P[j]
			matrix[jpos][i] /= matrix[ipos][i]
			a = matrix[jpos][i]
			for k in range(i + 1, n):
				matrix[jpos][k] -= a * matrix[ipos][k]


	det *= matrix[P[i+1]][i+1]
	return det


m1 = [[1, 3], [2, 5]]
m2 = [[2, 5, 3], [1, -2, -1], [1, 3, 4]]
m1a = [7,11,8,11]
m1b = [[7,11],[8,11]]
m2a = [211,312,415,514,223,213,789,897,978]
print(determinant(m2))
