def get_name_age():
    return "Alice", 30  # Returns a tuple

name, age = get_name_age()  # Tuple unpacking
print(name, age)  # Alice 30

lambda get_name_age2 = (str, int): ("Alice2", 32)  # Returns a tuple

name2, age2 = get_name_age2()  # Tuple unpacking
print(name2, age2)  # Alice2 32