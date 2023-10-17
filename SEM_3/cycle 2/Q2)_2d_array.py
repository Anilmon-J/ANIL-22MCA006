import numpy as np
print("NAME  : Anilmon J")
print("Reg No: 22MCA006")
print("Batch : MCA 2022-24 ")
print("-------------------------------------------------------------------")
complex_array = np.array([[1+2j, 2+3j, 3+4j],
                          [4+5j, 5+6j, 6+ 7j]])
print("Complex array:")
print(complex_array)

num_rows, num_cols = complex_array.shape
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_cols}")

dimensions = complex_array.shape
print(f"Dimensions of the array: {dimensions}")

reshaped_array = complex_array.reshape(3, 2)
print("Reshaped Array:")
print(reshaped_array)