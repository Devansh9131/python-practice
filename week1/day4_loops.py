import random

# Program 1: multiplication table

number = int(input("Enter a number:"))
for i in range(1, 11):
    print(f"{number} * {i} = {number*i}")


# Program 2: sum of 1 to N

n = int(input("Enter N:"))
total = 0
for i in range(1, n + 1):
    total += i
print(f"Sum of 1 to {n} is: {total}")


# Program 3: number guessing game

secret_number = random.randint(1, 100)
attempts = 0
print(secret_number)
while attempts < 7:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess == secret_number:
        break
    if guess > secret_number:
        print("Too high.")
    else:
        print("Too low.")
if guess == secret_number:
    if attempts == 1:
        print("Correct! You guessed it on your first attempt.")
    else:
        print(f"Correct! You guessed it in {attempts} attempts.")
else:
    print(f"You lost, the number was {secret_number}")
