# Basic if statement
import random
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

# Movie ticket

if age <= 12:
    print("The cost of your ticket is £5")
if age >= 18:
    print("The cost of your ticket is £10")
else:
    print("The cost of your ticket is £7")

# Rock Paper Scissors

list_of_moves = ['Rock' , 'Paper' , 'Scissors']
player_move = input("Please enter your move (Rock, Paper, or scissors): ")
player_move = player_move.lower()
print(f"Your move is {player_move}")

#Computer choice Rock Ppaper Scissors
computer_choice = random.choice(list_of_moves)

#Convert computer choice to lower case
computer_choice = computer_choice.lower()
print(f"Computer picks {computer_choice}")

#Conditions of play
if computer_choice == "rock" and player_move == "scissors":
    print(f"Computer wins!!")
elif computer_choice == "scissors" and player_move == "rock":
    print("You win!!")


# paper wins
elif computer_choice == "rock" and player_move == "paper":
    print("Computer wins!!")

