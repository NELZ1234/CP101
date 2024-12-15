word_bank = []

while True:
  word = input("Enter a word: ")
  word_bank.append(word)

  again = input("Do you want to enter another word? (Yeah/Nor): ")
  if again.lower() == 'yeah':
    continue
  else:
    break

print(f"\nYou entered {len(word_bank)} words:")
for word in word_bank:
  print(word)
  
