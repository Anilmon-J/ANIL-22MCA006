def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
print("NAME  : Anilmon J")
print("Reg No: 22MCA006")
print("Batch : MCA 2022-24 ")
print("-----------------------------------------------------------------------------------")


N = int(input("Enter the number :"))
current_num = 2
print( end=" ")
while N > 0:
    if not is_prime(current_num):
        print(current_num, end=" ")
        N -= 1
    current_num += 1