# Add
def add(n1, n2):
    return n1+n2

# Subtract


def subtract(n1, n2):
    return n1-n2

# Multiply


def multiply(n1, n2):
    return n1*n2

# Divide


def divide(n1, n2):
    return n1/n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# change from int to float for decimal
num1 = int(input("What is the first number? : "))
num2 = int(input("What is the second number?: "))

for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation from the line above: ")

calc_func = operations[operation_symbol]

answer = calc_func(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")