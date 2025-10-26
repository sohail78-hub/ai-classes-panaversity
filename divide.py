sample = 15
def abc(num1, num2):
    try:
        result = num1 / num2
        print("Result is:", result)
    except ZeroDivisionError as e:
        print("Error:", e)