import random
number = random.randint(1, 10)
print(number)
attempts = 0

guess = int(input("Enter your guess: "))
attempts = attempts + 1

while guess != number:

    if guess > number:
        print("Too High!")
    else:
        print("Too Low!")

    guess = int(input("Enter your guess: "))
    attempts = attempts + 1

print("Correct!")
print("Attempts:",attempts)
