import random
import re

life = 5
word_bank = ["apple", "banana", "cherry", "figs", "grapes", "honeydew", "jackfruit", "kiwi", "lemon", "mango", "nectarine", "orange", "peach", "raspberry", "strawberry", "watermelon"]

hidden_word = word_bank[random.randint(0, len(word_bank)-1)]

incorrect_guesses = []
blanks = "_ " * len(hidden_word)
while life > 0:
  print(blanks)
  print(f"Incorrect guesses: {incorrect_guesses}")
  guess = input("What is your guess? ")

  if guess in hidden_word:
    character_indexes = ([m.start() for m in re.finditer(guess, hidden_word)])
    print(f"There are {len(character_indexes)} '{guess}'(s)")
    for x in range(len(character_indexes)):
      character_indexes[x] = character_indexes[x] * 2
    for x in range(len(character_indexes)):
      blanks = blanks[:character_indexes[x]] + guess + blanks[character_indexes[x] + 1:]
    
    if "_" not in blanks:
      print("You win!")
      break
  else:
    print("Incorrect guess")
    incorrect_guesses.append(guess)
    life -= 1
    print(f"You have {life} live(s) left")
print(f"The word was {hidden_word}")
