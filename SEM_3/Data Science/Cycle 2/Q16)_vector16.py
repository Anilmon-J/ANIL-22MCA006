import numpy as np
print("NAME  : Anilmon J")
print("Reg No: 22MCA006")
print("Batch : MCA 2022-24 ")
print("-------------------------------------------------------------------")
A = np.array([[2, 1, -2],
              [3, 0, 1],
              [1, 1, -1]])

b = np.array([[-3],
              [5],
              [-2]])

try:

    X = np.linalg.solve(A, b)


    print("Solution X:")
    print(X)
except np.linalg.LinAlgError:
    print("Matrix A is singular. The system of equations may not have a unique solution.")