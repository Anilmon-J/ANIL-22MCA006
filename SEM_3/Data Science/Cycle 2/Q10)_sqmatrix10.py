import numpy as np
print("NAME  : Anilmon J")
print("Reg No: 22MCA006")
print("Batch : MCA 2022-24 ")
print("-------------------------------------------------------------------")
matrix_size = 3
matrix = np.random.randint(1, 10, size=(matrix_size, matrix_size))
print("Original Matrix:")
print(matrix)

if np.linalg.matrix_rank(matrix) == matrix_size:
    inverse_matrix = np.linalg.inv(matrix)
    print("\nInverse Matrix:")
    print(inverse_matrix)
else:
    print("\nThe matrix is not invertible (its rank is less than the size).")

rank = np.linalg.matrix_rank(matrix)
print("\nRank of the Matrix:", rank)

determinant = np.linalg.det(matrix)
print("\nDeterminant of the Matrix:", determinant)

matrix_1d = matrix.flatten()
print("\nMatrix as 1D Array:")
print(matrix_1d)

eigenvalues, eigenvectors = np.linalg.eig(matrix)
print("\nEigenvalues:")
print(eigenvalues)
print("\nEigenvectors:")
print(eigenvectors)