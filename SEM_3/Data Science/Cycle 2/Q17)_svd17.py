import numpy as np
print("NAME  : Anilmon J")
print("Reg No: 22MCA006")
print("Batch : MCA 2022-24 ")
print("-------------------------------------------------------------------")
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
U, S, Vt = np.linalg.svd(A)
reconstructed_A = U @ np.diag(S) @ Vt

print("Original Matrix A:")
print(A)

print("\nU matrix:")
print(U)

print("\nS matrix (diagonal matrix):")
print(np.diag(S))

print("\nVt matrix (transpose of V):")
print(Vt)

print("\nReconstructed Matrix A:")
print(reconstructed_A)