print("NAME  : Anilmon J")
print("Reg No: 22MCA006")
print("Batch : MCA 2022-24 ")
print("-----------------------------------------------------------------------------------")

num = int(input("Enter the value of n: "))
a= 0
b = 1
n = 0
count = 1

while(count <= num):
     print(n,end=" ")
     count += 1
     a = b
     b = n
     n = a + b
     t_number = a + b
