print("NAME  : Anilmon J")
print("Reg No: 22MCA006")
print("Batch : MCA 2022-24 ")
print("-------------------------------------------------------------------")
my_list = [1, 2, 3, 4, 5]
my_list.insert(2, 10)
print(my_list)
print("--------------------------")

my_2d_array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

element_to_insert = 10
row_index = 1
column_index = 1

my_2d_array[row_index].insert(column_index, element_to_insert)
for row in my_2d_array:
    print(row)