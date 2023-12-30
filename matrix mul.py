def matrix_multiply(matrix1, matrix2):
  if len(matrix1) != 3 or len(matrix2) != 3 or len(matrix1[0]) != 3 or len(matrix2[0]) != 3:
    raise ValueError("Matrices must be 3x3")
  result = [[0 for _ in range(3)] for _ in range(3)]
  for i in range(3):
    for j in range(3):
      for k in range(3):
        result[i][j] += matrix1[i][k] * matrix2[k][j]
  return result
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
product = matrix_multiply(matrix1, matrix2)
for row in product:
  print(row)