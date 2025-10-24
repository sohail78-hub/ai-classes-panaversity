# A mapping is an object that maps keys to values.

# Creating a dictionary (mapping)
# Method 1: Curly braces
person = {"name": "Alice", "age": 30, "city": "New York"}
print(person)
print(type(person))

# Method 2: Using dict() constructor
person = dict(name="Alice", age=30, city="New York")
print(person)

# From a list of tuples
pairs = [("name", "Alice"), ("age", 30)]
person = dict(pairs)
print(person)
print(type(person))
