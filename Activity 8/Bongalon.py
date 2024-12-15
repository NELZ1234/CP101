import random
import time

def guess_the_number():
    print("🎉 Welcome to the Ultimate 'Guess the Number' Challenge! 🎉")
    print("I'm thinking of a number between 1 and 20. Can you guess what it is?")
    print("You have 3 attempts. Let's see if you're lucky or skilled!")
    
    # Generate a random number between 1 and 20
    number_to_guess = random.randint(1, 20)
    attempts = 3  # Maximum attempts
    hint_given = False  # To track if a hint has been provided

    for attempt in range(1, attempts + 1):
        try:
            print(f"\n🕵️ Attempt {attempt}/{attempts}:")
            guess = int(input("🔢 Enter your guess: "))
            
            if guess < 1 or guess > 20:
                print("⚠️ Please pick a number between 1 and 20. Try again!")
                continue

            if guess == number_to_guess:
                print("🎉🎊 BOOM! You guessed it! Congratulations, genius! 🎊🎉")
                break
            elif abs(guess - number_to_guess) <= 2:
                print("🔥 So close! You're almost there!")
                if guess < number_to_guess:
                    print("📉 Just a little higher!")
                else:
                    print("📈 Just a little lower!")
            elif guess < number_to_guess:
                print("📉 Too low! Go a bit higher!")
            else:
                print("📈 Too high! Go a bit lower!")
            
            # Provide a hint after the first incorrect guess if not already given
            if not hint_given:
                hint = "even" if number_to_guess % 2 == 0 else "odd"
                print(f"🤔 Hint: The number is {hint}.")
                hint_given = True
        except ValueError:
            print("🤦‍♂️ That's not a number! Let's stick to numbers, shall we?")
        
        # Dramatic pause for the final attempt
        if attempt == attempts - 1:
            print("\n⏳ Last chance coming up... Think carefully!")
        elif attempt == attempts:
            print(f"\n😞 Oh no! You're out of attempts. The correct number was {number_to_guess}. Better luck next time!")
            break

    print("\nThanks for playing! Come back soon for another round of fun!")
    time.sleep(1)

guess_the_number()
