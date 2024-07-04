def add(num1, num2):
    return num1 + num2

while True:
    print('\nSelect your action:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit')
    action = int(input(""))

    if action > 4:
        print("Tata ✌️")
        break

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    if action == 1:
        print(f'\n> Addition is : {add(num1, num2)}')
    elif action == 2:
        print(f'\n> Subtraction is : {num1 - num2}')
    elif action == 3:
        print(f'\n> Multiplication is : {num1 * num2}')
    elif action == 4:
        print(f'\n> Division is : {num1 / num2}')
        
        
