#Calculator Program
# This program performs basic arithmetic operations based on user input.
#Creat fuctions for each operation
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

#Store the operations in a dictionary
operations = {
    "+": add, 
    "-": subtract,
    "*": multiply,
    "/": divide
}

# Use dictionary to perform operations
def calculator():
    print("Welcome to the Calculator!")
    num1 = float(input("Enter the first number: "))
    continue_calculate = True
    while continue_calculate : 
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation from the above symbols: ")
        
        # if operation_symbol not in operations:
        #     print("Invalid operation. Please try again.")
        #     return
        
        while operation_symbol not in ["+", "-","*","/"]:
            for symbol in operations:
                print(symbol)
            operation_symbol = input("Pick an operation from the above symbols: ")
        
        num2 = float(input("Enter the second number: ")) 
        
        # Perform the operation using the dictionary
        calculation_function = operations[operation_symbol]
        result = calculation_function(num1, num2)
        
        print(f"{num1} {operation_symbol} {num2} = {result}")

        next_action = input(f"Type 'yes' to continue with another operation with {result}, or 'no', Type 'Exist' to Terminate:\n").lower()

        while next_action not in ["yes", "no","exist"]:
            print("Invalid choice. Please type 'yes' or 'no'.")
            next_action = input("Type 'yes' to continue with another operation, or 'no', Type 'Exist' to Terminate :\n").lower()

        if next_action == "exist":
            print("Thank you for using the Calculator program. Goodbye!")
            continue_calculate = False
            return
        
        elif next_action == "yes":
            num1 = result

        elif next_action == "no":
            calculator()


calculator()