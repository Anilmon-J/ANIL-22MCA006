import math
def are_coprime(a, b):
    gcd = math.gcd(a, b)
    return gcd == 1
print("NAME  : Anilmon J")
print("Reg No: 22MCA006")
print("Batch : MCA 2022-24 ")
print("-----------------------------------------------------------------------------------")
a = int(input("Enter the first number: "))
b= int(input("Enter the second number: "))

if are_coprime(a,b):
    print(f"{a} and {b} are coprime")
else:
    print("They are not coprime")