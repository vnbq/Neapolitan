def add (n1 , n2):
    return n1 + n2

def subtract (n1 , n2):
    return n1 - n2

def mul (n1 , n2):
    return n1 * n2

def div (n1 , n2):
    return n1/n2

print('Welcome to Neapolitan!')

print('Please select an operation you want to do!')

print('1. Addition')

print('2. Subtraction')

print('3. Multiplication')

print('4. Division')

while True:
    c = input("Please choose an operation.")

    if c in ('1', '2', '3', '4'):
        try:
            n1 = float(input("Enter first number: "))
            n2 = float(input("Enter second number: "))
        except ValueError:
            print("Invaild, enter an actual number to continue. If you think this is an actual operation, report it to the github bug tracker.")
            continue


        if c == '1':
            print(n1, "+", n1, "=", add(n1, n2))

        elif c == '2':
            print(n1, "-", n2, "=", subtract(n1, n2))

        elif c == '3':
            print(n1, "*", n2, "=", mul(n1, n2))

        elif c == '4':
            print(n1, "/", n2, "=", div(n1, n2))




