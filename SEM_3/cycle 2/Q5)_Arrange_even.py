
import numpy as np
print("NAME  : Anilmon J")
print("Reg No: 22MCA006")
print("Batch : MCA 2022-24 ")
print("-------------------------------------------------------------------")
arr = np.arange(2, 32, 2)
slice_a = arr[2:9:2]
last_3_elements = arr[-3:]
alternate_elements = arr[::2]
last_3_alternate_elements = alternate_elements[-3:]
print("Original Array:", arr)
print("a. Elements from index 2 to 8 with step 2:", slice_a)
print("b. Last 3 elements of the array using negative index:", last_3_elements)
print("c. Alternate elements of the array:", alternate_elements)
print("d. Last 3 alternate elements:", last_3_alternate_elements)