def add_lists(a,b):

    if len(a) != len(b):
        return None

    result = []

    for i in range(len(a)):
        result.append(a[i] + b[i])

    return result

try:
    print("NAME  : Anilmon J")
    print("Reg No: 22MCA006")
    print("Batch : MCA 2022-24 ")
    print("-----------------------------------------------------------------------------------")
    a = input("Enter the first list of numbers : ").split()
    a = [int(x) for x in a]

    b = input("Enter the second list of numbers : ").split()
    b = [int(x) for x in b]

    result = add_lists(a, b)

    if result is None:
        print("The lists have different lengths and cannot be added.")
    else:
        print("Result of addition:", result)
except ValueError:
    print("Invalid input. Please enter valid numbers separated by spaces.")