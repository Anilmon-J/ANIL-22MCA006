print("NAME  : Anilmon J")
print("Reg No: 22MCA006")
print("Batch : MCA 2022-24 ")
print("-----------------------------------------------------------------------------------")

n=int(input("Enter a number:\n"))
sum=0
for i in range(1,n):
    if(n % i == 0):
        sum=sum+i
if( sum == n):
    print("The number is perfect number")
else:
    print("The entered number is not perfect")