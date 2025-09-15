# Sohail Ahmed Khatri
# Assignment 2 - Simple Calculator
# Batch-76 (Karachi)

while True:
    
# Types of Airthmatic Operators
    print("\nSelect a Calculation Type:")
    print("=========================")
    print("\n1. + Addition ")
    print("2. - Subtraction")
    print("3. x Multiplication")
    print("4. / Division")
    print("5. % Modulus")
    print("6. // Floor Division")
    print("7. ** Exponentiation")
    print("8. Exit")

    operator_types = input("\nEnter Choice from (1 to 8): ")

    # if user wants to exit
    if operator_types == '8':
        print("Exiting the Calculator, Goodbye!")
        break

    # Take input from the user
    if operator_types in ('1', '2', '3', '4', '5', '6', '7'):
        num1 = float(input("\nEnter First Number: "))
        num2 = float(input("Enter Second Number: "))


    if operator_types == '1':
        print('\nYou have selected Addition "+"')
        print(f'{num1} + {num2} = Ans {num1 + num2}')

    elif operator_types == '2':
        print('\nYou have selected Subtraction "-"')
        print(f'{num1} - {num2} = Ans {num1 - num2}')

    elif operator_types == '3':
        print('\nYou have selected Multiplication "x"')
        print(f'{num1} x {num2} = Ans {num1 * num2}')
        
    elif operator_types == '4':
        print('\nYou have selected Division "/"')
        print(f'{num1} / {num2} = Ans {num1 / num2}')
        
    elif operator_types == '5':
        print('\nYou have selected Modulus "%"')
        print(f'{num1} % {num2} = Ans {num1 % num2}')
        
    elif operator_types == '6':
        print('\nYou have selected Floor Division "//"')
        print(f'{num1} // {num2} = Ans {num1 // num2}')

    elif operator_types == '7':
        print('\nYou have selected Exponentiation "**"')
        print(f'{num1} ** {num2} = Ans {num1 ** num2}')
                   
    else:
        print("Invalid Input")
        
