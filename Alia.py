def word_bank_program():
    word_list = []  

    while True:
    
        word = input("Enter a word: ")
        word_list.append(word)

      
        try_again = input("Do you want to enter another word? (Y/N): ").strip().lower()

        
        if try_again == 'n':
            break
        elif try_again != 'y':
            print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
    

    print(f"\nYou entered {len(word_list)} words.")
    print("Here are the words you entered:")
    for i, word in enumerate(word_list, start=1):
        print(f"{i}. {word}")


word_bank_program()
