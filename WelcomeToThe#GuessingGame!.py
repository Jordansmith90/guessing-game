import random

print("Welcome to the Number Guessing Game!")
print("Choose a difficulty level:")
print("1-Easy (1 to 50)")
print("2-Medium (1 to 100)")
print("3-Hard (1 to 500)")

Difficulty = input("Enter 1, 2, or 3: ")

if Difficulty == "1":
    max_number = 50
elif Difficulty == "2":
    max_number = 100
elif Difficulty == "3":
    max_number = 500
else:
    print("Invalid choice. Defaulting to medium. /n")
    max_number = 100

secret_number = random.randint(1, max_number)
guess = None
attempts = 0

while guess != secret_number:
    print(f"Guess a number between 1 and {max_number}:")
    guess = int(input())
    attempts += 1

    if guess < secret_number:
        print("Too Low!")
    elif guess > secret_number:
        print("Too High!")
    else:
        print(f"Correct! You guessed it in {attempts} tries.")
