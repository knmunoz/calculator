# addition fcn
def add(a, b):
    return a + b

# subtraction fcn
def subtract(a, b):
    return a - b

# multiplication fcn
def multiply(a, b):
    return a * b

# division fcn
def divide(a, b):
    return a / b

print("Select operation")
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")

while True:
    # take input from user
    choice = input("Enter choice (1-4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid input")