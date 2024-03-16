import random

number = random.randint(1, 100)

guess = int(input("Guess a number between 1 and 100: "))
if guess == number:
    print(f"Congratulations! You guessed it first try!")
else:
    counter = 1
    while guess != number:
        counter += 1
        if guess < number:
          print("Too low")
        elif guess > number:
          print("Too high")
        guess = int(input("Guess a number between 1 and 100: "))
    print(f"Congratulations! You guessed it on your {counter} try!")
