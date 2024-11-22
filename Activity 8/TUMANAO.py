import random


secret_number = random.randint(5, 100)


attempts = 6


for attempt in range(attempts):
  print(f"You have {attempts - attempt} attempts left.")
  guess = int(input("Guess a number between 5 and 100: "))

 
  if guess == secret_number:
    print("Congratulations! You guessed it!")
    break
  elif guess < secret_number:
    print("Too low! Try again.")
  else:
    print("Too high! Try again.")


if guess != secret_number:
  print(f"You ran out of attempts. The secret number was {secret_number}.")
