import numpy as np
print("NAME  : Anilmon J")
print("Reg No: 22MCA006")
print("Batch : MCA 2022-24 ")
print("-------------------------------------------------------------------")
X = np.array([[1, 2],
              [3, 4]])
Y = np.random.rand(*X.shape)
result = X * 2 + 2 * Y
print("The result:")
print(result)