import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# print(operations["*"](4, 8))

print(art.logo)

keep = False
while True:
    if not keep:
        n1 = float(input("What's the first number?:  "))
    for symbol in operations:
        print(symbol)
    operation = input("Pick an operation:  ")
    n2 = float(input("What's the next number?:  "))
    result = operations[operation](n1, n2)
    print(f"{n1} {operation} {n2} = {result}")
    again = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:  ").lower()
    if again == 'y':
        n1 = result
        keep = True
    elif again == 'n':
        keep = False
        print("\n" * 100)
        print(art.logo)
