# Basic if statement
from operator import truediv

age = 20

if age >= 18:
    print("You are an adult")

# Using if, elif, and else
age = 16

if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")

# Nested if statement
age = 20
is_student = True

if age >= 18:
    print("You are an adult.")
    if is_student:
        print("You are also a student.")
else:
    print("You are a minor.")

# Using logical operators
age = 19
has_pass = True

if age >= 18 and has_pass:
    print("You are allowed entry")
else:
    print("You are not allowed entry")


