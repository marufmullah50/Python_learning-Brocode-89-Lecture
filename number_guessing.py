 #Number guessing model
import random
high = 100
low = 1
i = 0
number = random.randint(low, high)
print("Welcome to the number guessing game!")
while True:
    guess = int(input(f"Guess a number between {low} and {high}: "))
    if guess <number:
        print(f"{guess} is Too low! Try again.")
    elif guess > number:
        print(f"{guess} is Too high! Try again.")
    else:
        print("You got it!")
        break
    i +=1

print (f"You took {i} attempts to guess the number {number}.")
print("Thanks for playing!")

