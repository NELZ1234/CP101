word_bank = []

while True:
    # Ask the user to enter a word
    word = input("Enter a word: ")
    # Add the word to the word bank
    word_bank.append(word)

    # Ask if the user wants to try again
    try_again = input("Do you want to try again? (Y/y for Yes, N/n for No): ")
    if try_again.lower() == 'n':
        # Exit the loop if the user says No
        break

# Display the total number of words and the words entered
print(f"\nTotal number of words entered: {len(word_bank)}")
print("Words entered:", ', '.join(word_bank))
