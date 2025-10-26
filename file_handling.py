# File handling in Python
# File handling means reading from and writing to files
# Python has built-in functions for file handling
# open() function is used to open a file
# close() function is used to close a file

file = open("example.txt", "w")  # Open a file in write mode (file is variable)
file.write("This text created from/to file_handling.py.")  # Write to the file
file.close()  # Close the file


# file3 = open("error.py", "r") 
# content2 = file3.read()  # Read the content of the file
# print(content2)  # Print the content
# file3.close()  # Close the file

file3 = open("example.txt", "a")  # Open the file in append mode
file3.write("\nAppending new line to the file.")
file3.write("\n 3rd Line # Append to the file")
file3.close()  # Close the file

# file2 = open("example.txt", "r")  # Open the file in read mode
# content = file2.read()  # Read the content of the file
# print(content)  # Print the content
# file2.close()  # Close the file

# Auto close using with statement
with open("example.txt", "r") as file4:  # Open the file in read mode
    content3 = file4.read()  # Read the content of the file
    print(content3)  # Print the contegnt