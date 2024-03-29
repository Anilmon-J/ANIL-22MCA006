import numpy as np
print("NAME  : Anilmon J")
print("Reg No: 22MCA006")
print("Batch : MCA 2022-24 ")
print("-------------------------------------------------------------------")
A = np.array([[1, 2, 3, 4, 5, 6],
              [7, 8, 9, 10, 11, 12],
              [13, 14, 15, 16, 17, 18],
              [19, 20, 21, 22, 23, 24],
              [25, 26, 27, 28, 29, 30]])

B = np.array([[2, 3, 4],
              [5, 6, 7],
              [8, 9, 10]])

submatrix_A = A[:3, :3]

result = np.dot(submatrix_A, B)

A[:3, :3] = result

print("Updated Matrix A:")
print(A)