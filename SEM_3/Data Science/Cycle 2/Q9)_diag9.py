import numpy as np
print("NAME  : Anilmon J")
print("Reg No: 22MCA006")
print("Batch : MCA 2022-24 ")
print("-------------------------------------------------------------------")
arr_id = np.array([1, 2, 3, 4, 5])
diagonal_matrix = np.diag(arr_id)
print("1D Array:")
print(arr_id)
print("\nDiagonal Matrix:")
print(diagonal_matrix)

arr_2d_square = np.array([[1, 2, 3],
                          [4, 5, 6],
                          [7, 8, 9]])
diagonal_elements = np.diag(arr_2d_square)

print("\n2D Square Matrix:")
print(arr_2d_square)
print("\nDiagonal Elements:")
print(diagonal_elements)

arr_2d_non_square = np.array([[1, 2, 3],
                              [4, 5, 6]])
diagonal_elements_non_square = np.diag(arr_2d_non_square)

print("\n2D Non-Square Matrix:")
print(arr_2d_non_square)
print("\nDiagonal Elements (Non-Square):")
print(diagonal_elements_non_square)