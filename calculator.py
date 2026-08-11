num1 =int(input("enter the number: "))
num2 =int(input("enter the number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

num3 =int(input("enter your choice: "))

if num3 == 1:
    print(num1+num2)
elif num3 == 2:
    print(abs(num1-num2))
elif num3 == 3:
    print(num1*num2)
elif num3 == 4:
    print(num1/num2)
else:
    print("Invalid Choice")    