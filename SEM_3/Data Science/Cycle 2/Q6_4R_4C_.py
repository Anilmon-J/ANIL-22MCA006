import numpy as np

array_2d = np.array([[1, 2, 3, 4],
                     [5, 6, 7, 8],
                     [9, 10, 11, 12],
                     [13, 14, 15, 16]])
print("NAME  : Anilmon J")
print("Reg No: 22MCA006")
print("Batch : MCA 2022-24 ")
print("-------------------------------------------------------------------")
print("All elements excluding the first row:")
print(array_2d[1:, :])
print("\nAll elements excluding the last column:")
print(array_2d[:, :-1])
print("\nElements of the 1st and 2nd column in the 2nd and 3rd row:")
print(array_2d[1:3, 0:2])
print("\nElements of the 2nd and 3rd column:")
print(array_2d[:, 1:3])
print("\n2nd and 3rd element of the 1st row:")
print(array_2d[0, 1:3])
print("\nElements from indices 4 to 10 in descending order:")
print(array_2d.flatten()[10:3:-1])