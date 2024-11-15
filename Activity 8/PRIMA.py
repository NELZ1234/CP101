import random

def guess_the_number():
  """Plays a number guessing game with the user."""

  number = random.randint(1, 20)
  attempts = 0
  max_attempts = 3

  print("Guess a Number 1 between 20.")

  while attempts < max_attempts:
    attempts += 1
    
    try:
      guess = int(input(f"Attempt {attempts}: Enter your guess: "))
    except ValueError:
      print("Invalid input. Please enter a number.")
      continue

    if guess < number:
      print("Too low! Try again.")
    elif guess > number:
      print("Too high! Try again.")
    else:
      print(f"Congratulations! You guessed the number in {attempts} attempts!")
      return

  print(f"You ran out of attempts. The number was {number}.")

if __name__ == "__main__":
  guess_the_number()


import random

def guess_the_number():
  """Plays a simple number guessing game with the user."""

  number = random.randint(1, 20)
  attempts = 0
  max_attempts = 3

  print("I'm thinking of a number between 1 and 20.")

  while attempts < max_attempts:
    attempts += 1
    guess = int(input(f"Attempt {attempts}: Enter your guess: "))

    if guess < number:
      print("Too low! Try again.")
    elif guess > number:
      print("Too high! Try again.")
    else:
      print(f"Congratulations! You guessed the number {number} in {attempts} attempts!")
      return

  print(f"Sorry, you're out of attempts. The number was {number}.")

if __name__ == "__main__":
  guess_the_number()


