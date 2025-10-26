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
    
    except ValueError as e: # for invalid input error
        print("Error:", e)
    
    except ZeroDivisionError as e:   # for Division by zero error as e (e store the actual error message)
        print("Error:",e)

    except Exception as e:          # for any other error / General Exception (e store the actual error message)
        print("Some error occurred", e)
    
    except SyntaxError as e:
        print("Syntax Error:", e)
        
    # Interrupted by User Error
    except KeyboardInterrupt as e:  # for Keyboard Interrupt error(e store the actual error message)
        print("Process Interrupted by User", e)
    
    finally:   # it will always execute in last (no matter what)
        print("Execution Completed")
        
calculate('/')