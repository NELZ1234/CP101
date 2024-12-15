def word_bank():
    
    words = []

    
    while True:
        
        word = input("Enter a word: ")
        words.append(word)  

    
        try_again = input("Do you want to try again? (Y/y for Yes, N/n for No): ").strip().lower()

        if try_again == 'n':  
            break
        elif try_again != 'y':  
            print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
    
    
    print(f"\nYou entered {len(words)} words.")
    print("The words you entered are:")
    for word in words:
        print(word)
word_bank()
