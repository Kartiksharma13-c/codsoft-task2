def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def main():
    print("Welcome to the Simple Calculator!")
    
   
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    operation = input("Enter the number corresponding to the operation (1/2/3/4): ")
    
    
    if operation == '1':
        result = add(num1, num2)
        print(f"\nResult: {num1} + {num2} = {result}")
    elif operation == '2':
        result = subtract(num1, num2)
        print(f"\nResult: {num1} - {num2} = {result}")
    elif operation == '3':
        result = multiply(num1, num2)
        print(f"\nResult: {num1} * {num2} = {result}")
    elif operation == '4':
        result = divide(num1, num2)
        print(f"\nResult: {num1} / {num2} = {result}")
    else:
        print("Invalid operation selected. Please try again.")

if __name__ == "__main__":
    main()
