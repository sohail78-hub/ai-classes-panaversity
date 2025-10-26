
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))  

opr = input("Enter operator (+, -, *, /): ")

def calculator(num1, num2, opr):
    if opr == '+':
        return num1 + num2
    elif opr == '-':
        return num1 - num2
    elif opr == '*':
        return num1 * num2
    elif opr == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"
    
    calculator(num1, num2, opr)
    print("Result is:", result)
