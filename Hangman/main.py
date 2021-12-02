#Step 5

import random
from hangman_art import stages
from hangman_art import logo
from hangman_words import word_list
#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(logo)

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')
for _ in range(len(chosen_word)) :
  print("_", end=" ")
print("\n")

#Create blanks
words = []
display = []
for _ in range(word_length):
    display += "_"
    
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

    #Check guessed letter
    if guess not in words:
      for position in range(word_length):
          letter = chosen_word[position]
          #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
          if letter == guess:
              display[position] = letter
              words += guess
              print(words)
              print(lives)
    else :
      print("You've already found this one")        
      print(lives)

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        lives -= 1
        print("That is a wrong call.")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])