word_list = ["camel","balloon","hangman"]
import random
lives = 6
chosen_word = random.choice(word_list)
placeholder = "_"*len(chosen_word)
print(placeholder)
game_over = False
right_letter = []
while not game_over:
    guess_letter = input("Guess a letter:").lower()
    print(guess_letter)
    display = ""
    for letter in chosen_word:
      if letter == guess_letter:
        display += guess_letter
        if guess_letter not in right_letter:
            right_letter.append(guess_letter)
        
      elif letter in right_letter:
        display += letter
      else:
        display += "_"
    print(display)
    if guess_letter not in chosen_word:
      lives -= 1
      print(f"Incorrect! You have {lives} lives remaining.")
      if lives == 5:
            print("  +---+")
            print("  |   |")
            print("  O   |")
            print("      |")
            print("      |")
            print("      |")
      elif lives == 4:
            print("  +---+")
            print("  |   |")
            print("  O   |")
            print("  |   |")
            print("      |")
            print("      |")
      elif lives == 3:
            print("  +---+")
            print("  |   |")
            print("  O   |")
            print(" /|   |")
            print("      |")
            print("      |")
      elif lives == 2:
            print("  +---+")
            print("  |   |")
            print("  O   |")
            print(" /|\\  |")
            print("      |")
            print("      |")
      elif lives == 1:
            print("  +---+")
            print("  |   |")
            print("  O   |")
            print(" /|\\  |")
            print(" /    |")
            print("      |")
      elif lives == 0:
            print("  +---+")
            print("  |   |")
            print("  O   |")
            print(" /|\\  |")
            print(" / \\  |")
            print("      |")
            game_over = True
            print("You lose!")
      

    if "_" not in display:
      game_over = True
      print("You Win!")
