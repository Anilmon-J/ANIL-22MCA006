import numpy as np

matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
matrix2 = np.array([[9, 8, 7],
                    [6, 5, 4],
                    [3, 2, 1]])
print("NAME  : Anilmon J")
print("Reg No: 22MCA006")
print("Batch : MCA 2022-24 ")
print("-------------------------------------------------------------------")
addition_result = matrix1 + matrix2
print("Matrix addition:")
print(addition_result)

subtraction_result = matrix1 - matrix2
print("\nMatrix Subtraction:")
print(subtraction_result)

multiplication_result = matrix1 * matrix2
print("\nMatrix Element-wise Multiplication:")
print(multiplication_result)

division_result = matrix1 / matrix2
print("\nMatrix Element-wise Division:")
print(division_result)

matrix_multiplication_result = np.dot(matrix1, matrix2)
print("\nMatrix Multiplication:")
print(matrix_multiplication_result)

matrix1_transpose = np.transpose(matrix1)
print("\nTranspose of Matrix1:")
print(matrix1_transpose)

diagonal_sum = np.trace(matrix1)
print("\nSum of Diagonal Elements:")
print(diagonal_sum)