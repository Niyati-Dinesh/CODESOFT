def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error! Division by zero."

def multiply(a, b):
    return a * b

def get_numbers():
    while True:
        try:
            a = float(input("Enter number 1: "))
            b = float(input("Enter number 2: "))
            return a, b
        except ValueError:
            print("Invalid input! Please enter numerical values.")

def calculator():
    print("CALCULATOR")
    print("----------")
    
    while True:
        print("\n1. ADD")
        print("2. SUBTRACT")
        print("3. DIVIDE")
        print("4. MULTIPLY")
        print("5. EXIT")
        
        try:
            ch = int(input("Enter operation (1, 2, 3, 4, 5): "))
            
            if ch == 1:
                a, b = get_numbers()
                print(f"{a} + {b} = {add(a, b)}")
            elif ch == 2:
                a, b = get_numbers()
                print(f"{a} - {b} = {subtract(a, b)}")
            elif ch == 3:
                a, b = get_numbers()
                print(f"{a} / {b} = {divide(a, b)}")
            elif ch == 4:
                a, b = get_numbers()
                print(f"{a} x {b} = {multiply(a, b)}")
            elif ch == 5:
                print("Thank you! Exiting the calculator.")
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 5.")
                
        except ValueError:
            print("Invalid option! Please enter a valid number.")
        
        print("\n---------------------------")

calculator()
