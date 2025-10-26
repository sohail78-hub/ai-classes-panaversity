# Module means code divided into different files
# This is module.py file

# import divide  # Importing divide module
# import divide as dv  # Importing divide module with alias

import math as mt;
import random as rd;

from agents import Agent  # Importing Agent class from agents module

from random import sample
from divide import abc, sample  # Importing abc function from divide module

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

abc(num1, num2)  # Calling abc function from divide module
print("Sample value from divide module is:", sample)