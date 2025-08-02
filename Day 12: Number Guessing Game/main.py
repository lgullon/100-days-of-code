import random
import art

print(art.logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

ans = random.randint(1, 100)
print(f"(psst.. the answer is {ans}..)")

diff = input("Choose a difficulty: Type 'easy' or 'hard': ")
attempts = -1
if diff == "easy":
    attempts = 10
elif diff == "hard":
    attempts = 5
else:
    print("Invalid difficulty.")
    quit()

while attempts != 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > ans:
        print("Too high.")
    elif guess < ans:
        print("Too low.")
    else:
        print(f"You got it! The answer was {ans}.")
        quit()

    attempts -= 1

print("You've run out of guesses. Refresh the page to run again.")

