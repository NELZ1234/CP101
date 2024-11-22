import random

def guess_the_number():
    random_number = random.randint(1, 20)
    attempts = 3

    print("Welcome to 'Guess the Number'!")
    print("I have picked a number between 1 and 20. You have 3 attempts to guess it.")
  
    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}/{attempts}: Enter your guess: "))

            if guess == random_number:
                print(f"Congratulations! You guessed the number {random_number} correctly!")
                break
            elif guess < random_number:
                print("Too low!")
            else:
                print("Too high!")
        except ValueError:
            print("Please enter a valid number.")
        
        if attempt == attempts:
            print(f"Sorry, you've run out of attempts. The number was {random_number}.")

guess_the_number()
