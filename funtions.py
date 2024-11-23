# WITHOUT PARAMETER AND WITHOUT RETURN
def add():
    num1 = int(input("Enter a number : "))
    num2 = int(input("Enter a number : "))
    print(num1+num2)
add()

# WITHOUT PARAMETER AND WITH RETURN
def add():
    num1 = int(input("Enter a number : "))
    num2 = int(input("Enter a number : "))
    return num1+num2
print(add())

# WITH PARAMETER AND WITHOUT RETURN
def add(num1,num2):
    print(num1+num2)
num1 = int(input("Enter a number : "))
num2 = int(input("Enter a number : "))
add(num1,num2)

# WITH PARAMETER AND WITH RETURN
def add(num1,num2):
    return num1+num2
num1 = int(input("Enter a number : "))
num2 = int(input("Enter a number : "))
print(add(num1,num2))