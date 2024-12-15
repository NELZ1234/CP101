import random


number_to_guess = random.randint(1, 30)


max_attempts = 4


print("Welcome to Guess the Number!")
print(f"Try to guess the number between 1 and 30. You have {max_attempts} attempts.")

for attempt in range(1, max_attempts + 2):
    
    guess = int(input(f"Attempt {attempt}: Enter your guess: "))
    
    
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {number_to_guess} correctly.")
        break
else:
    print(f"Sorry, you've used all your attempts. The correct number was {number_to_guess}.")
    
