import random

# The attempts needed
def guess_the_number():
  """Plays a number guessing game with the user."""

  number = random.randint(1, 20)
  attempts = 0
  max_attempts = 3

# To enter a number to guess it
  print("Try to guess a number between 1 and 20, let's see if you're right.")

  while attempts < max_attempts:
    attempts += 1

    try:
      guess = int(input(f"Attempt {attempts}: Enter your guessing number: "))
    except ValueError:
      print("Invalid input. Please enter a number to continue.")
      continue

# To see if the number guessed is correct or not
    if guess < number:
      print("The number you guessed is too low! Try again.")
    elif guess > number:
      print("The number you guessed is too high! Try again.")
    else:
      print(f"Congratulations! You guessed the right number in {attempts} attempts!")
      return

  print(f"You have unfortunately ran out of attempts. The number was {number}.")

if __name__ == "__main__":
  guess_the_number()
