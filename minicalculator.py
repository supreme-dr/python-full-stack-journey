# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def main():
    print("Welcome to CLI Calculator!")
    
    # Open log file in append mode
    with open("calculator_log.txt", "a", encoding="utf-8") as log_file:
        
        while True:
            print("\nChoose operation:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Exit")
            
            choice = input("Enter choice (1-5): ")
            
            if choice == "5":
                print("Exiting calculator. Goodbye!")
                log_file.write("Calculator session ended.\n\n")
                break
            
            if choice not in ["1", "2", "3", "4"]:
                print("Invalid choice. Try again.")
                continue
            
            try:
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))
            except ValueError:
                print("Error: Please enter a valid number.")
                continue
            
            # Perform calculation
            if choice == "1":
                result = add(num1, num2)
                operation = "Addition"
            elif choice == "2":
                result = subtract(num1, num2)
                operation = "Subtraction"
            elif choice == "3":
                result = multiply(num1, num2)
                operation = "Multiplication"
            elif choice == "4":
                result = divide(num1, num2)
                operation = "Division"
            
            print(f"Result: {result}")
            
            # Log calculation to file
            log_file.write(f"{operation}: {num1} and {num2} = {result}\n")

if __name__ == "__main__":
    main()
