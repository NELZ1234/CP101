
def word_bank():
    words = [] 

    while True:
        word = input("Enter a word: ")
        words.append(word)  

        
        try_again = input("Do you want to enter another word? (Y/y for Yes, N/n for No): ")
        
        if try_again.lower() == 'n':
            break  
        elif try_again.lower() != 'y':
            print("Invalid input. Please enter Y/y or N/n.")
    
    
    print(f"\nTotal number of words entered: {len(words)}")
    print("Words entered:")
    for word in words:
        print(word)

word_bank()
