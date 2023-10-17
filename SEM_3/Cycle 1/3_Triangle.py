print("NAME  : Anilmon J")
print("Reg No: 22MCA006")
print("Batch : MCA 2022-24 ")
print("-----------------------------------------------------------------------------------")

print("Input length of Triangle Sides:")
x=int(input("x:"))
y=int(input("y:"))
z=int(input("z:"))
if( x == y == z):
    print("Equilateral triangle")
elif(x == y or y==z or z==x):
    print("Isosceles triangle")
else:
    print("Triangle is Scalene")
