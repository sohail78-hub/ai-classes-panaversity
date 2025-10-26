# Error handling 
# 1. SyntaxError
# This error occurs when there is a mistake in the syntax of the code.

# 2. LogicError
# This error occurs when the code runs without syntax errors but produces incorrect results due to flawed logic.

# try except


try:
    num = int(input("Enter a number: "))  # Code that may raise an exception
    result = 10 / num
    print("Result is:", result)

except ZeroDivisionError:  # ZeroDivisionError Class
    print("Zero Division Error")
    
except ValueError:  # ValueError Class
    print("Value Error")

except Exception as error: # Local Error
    print(error)