
word_bank = []

while True:

    word = input("Enter a word: ")
    word_bank.append(word)  

    try_again = input("Do you want to enter another word? (Y/y for Yes, N/n for No): ")
    
    if try_again.lower() != 'y':
        break  
    
print(f"\nTotal number of words: {len(word_bank)}")
print("Words entered:", ', '.join(word_bank))
