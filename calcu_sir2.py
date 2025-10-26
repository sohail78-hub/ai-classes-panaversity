def calculate (op: str):
    try:     
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        
        if op == '+':
            print("Result is:", num1 + num2)
        
        elif op == '-':
            print("Result is:", num1 - num2)
        
        elif op == '*':
            print("Result is:", num1 * num2)
        
        elif op == '/':
            print("Result is:", num1 / num2)
        
        else:   # In this function we manually raise an exception for invalid operator
            raise Exception("Operator Galat dala hey")

    except Exception as e:          # for any other error / General Exception (e store the actual error message)
        print("Some error occurred:", e)
    
    except ValueError as e: # for invalid input error
        print("Error:", e)
    
    except ZeroDivisionError as e:   # for Division by zero error as e (e store the actual error message)
        print("Error:",e)

    
    except SyntaxError as e:
        print("Syntax Error:", e)
    
    else:   # if no error occurs   (it will be part of try block)
        print("No error occurred")
    
    finally:   # it will always execute in last (no matter what)
        print("Execution Completed")
        
calculate('a')