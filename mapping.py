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
print(type(pairs))
person = dict(pairs)
print(person)
print(type(person))


# Common operations on mappings (dictionaries)
person = {"name": "Alice", "age": 30}

# Access value by key
print(person["name"])           # Alice

# Add or modify
person["job"] = "Engineer"

# Remove key
del person["age"]

# Check if key exists
if "name" in person:
    print("Key exists")

# Get all keys, values, or both
print(person.keys())     # dict_keys(['name', 'job'])
print(person.values())   # dict_values(['Alice', 'Engineer'])
print(person.items())    # dict_items([('name', 'Alice'), ('job', 'Engineer')])

# Loop through items
for key, value in person.items():
    print(f"{key}: {value}")