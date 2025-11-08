# Assignment 3: Guess the Number Game
import random

def guess_the_number():
    print("Guess the Number Game!")
    print("I am thinking of a number between 1 and 100.")
    print("You have 10 attempts to guess it.")

    # Computer picks a random number
    secret_number = random.randint(1, 100)
    max_attempts = 10
    attempts = 0

    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts} - Enter your guess from ( 1 to 100 ): "))
            attempts += 1

            # Check if guess is within range
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 to 100.")
                continue

            # Compare guess with secret number
            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} accurately!")
                print(f"It took you {attempts} attempt(s).")
                break  # Exit loop on correct guess

        except ValueError:
            print("Invalid input! Please enter a valid number.")
            # Note: Invalid input counts as an attempt (you can change this behavior if needed)

    else:
        # This runs if the loop ended without 'break' (i.e., no correct guess)
        print(f"\nSorry, you have used all {max_attempts} attempts.")
        print(f"The correct number was {secret_number}. Better luck next time!")

# Start the game
guess_the_number()