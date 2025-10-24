abc = {'a', 'b', 'c'}
print(type(abc))  # <class 'set'>
print(abc)        # {'a', 'c', 'b'}

# creating empty set

empty_set = set()
print(type(empty_set))  # <class 'set'>

numbers = set([1, 2, 3, 2, 1]) # duplicates will be removed
print(numbers)  # {1, 2, 3}

# Adding elements to a set
fruits = {"apple", "banana"}
fruits.add("cherry")
print(fruits)  # {'apple', 'banana', 'cherry'}

# Removing elements from a set
fruits.remove("banana")   # Removes item; raises error if not found
fruits.discard("grape")   # Safer: does nothing if item doesn't exist
fruits.discard("apple")
print(fruits)  # {'cherry'}

# Set operations
if "apple" in fruits:
    print("Found!")
else:
    print("Not found!")  # Not found!

# Set operations
A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)  # Union: {1, 2, 3, 4, 5}
print(A & B)  # Intersection: {3}
print(A - B)  # Difference: {1, 2}
print(A ^ B)  # Symmetric diff: {1, 2, 4, 5}

# Remove duplicates from a list using set
data = [1, 2, 2, 3, 4, 4, 5]
unique_data = list(set(data))

print(unique_data)  # {1, 2, 3, 4, 5} → order may vary!

print(type(unique_data))

# Check membership in a set
allowed_roles = {"admin", "editor", "moderator"}
user_role = "admin"

if user_role not in allowed_roles:
    print("Access not granted!")
else:
    print("Access granted!") 

# Much faster than using a list
blacklist = {"spam@example.com", "fake@domain.com", "suspicious@user.com"}  # Could be thousands
email = "spam@example.com"

if email in blacklist:  # Very fast O(1) average case
    print("Blocked!")
else:
    print("Allowed!")

# If you need a set that cannot be changed, use frozenset.
# Immutable set
frozen = frozenset([1, 2, 3])
# frozen.add(4)  # ❌ AttributeError: 'frozenset' object has no attribute 'add'