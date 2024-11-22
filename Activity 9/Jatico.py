# To define the list of words entered in total
def word_bank_program():
    words = []
    
# This is to apply all the words that have been entered
    while True:
        word = input("Enter a word: ")
        words.append(word)
        
# This is to let more words be entered in the list
        enter_new_word = input("Do you want to list more words? (Y/y for Yes, N/n for No): ").strip().lower()
        if enter_new_word == 'n':
            break
    
    print(f"\nTotal number of words entered: {len(words)}")
    print("Words that have been listed:")
    for word in words:
        print(word)

# Run the word bank program
word_bank_program()
