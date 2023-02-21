import random


#print a welcome for the user and invite them to play
print("Welcome to Hangman!")
name = input("What should we call you? ")
print(f"Hello {name}! Let's play")
print("You must complete the game within 8 guesses... OR ELSE!!!")
print("\n+---+")
print(" |   |")
print(" O   |")
print("/|\  |")
print("/ \  |")
print("    ===")
print("-------------------------------------------")


#add difficulty selection for users that increases the letter count relative to difficulty selected
difficulty = input("Select your preferred difficulty level\n easy - 6 Letter words,\n medium - 7 Letter words,\n hard - 8 Letter words):\n ")
while difficulty not in ['easy', 'medium', 'hard']:
  print("Invalid input. Please select a valid difficulty level.")
  difficulty = input("Please select the difficulty level (easy, medium, or hard): ")


#chooses a word dictionary based on the users selected difficulty 
if difficulty == 'easy':
  word_dictionary = ["pickax", "whacky", "quacks", "boozey", "joyful", "chubby", "enzyme", "hotdog", "cheese", "jacket"]
elif difficulty == 'medium':
  word_dictionary = ["buzzcut", "qualify", "salvage", "sunbeam", "reading", "witness", "stencil", "costume", "grimace", "serving"]
else:
  word_dictionary = ["illusion", "teaching", "policies", "exorcist", "stumbled", "invested", "pregnant", "hydrated", "tapestry", "remarked"]


#chooses a random word from a dictionary based on the players selected difficulty
randomWord = random.choice(word_dictionary)


#prints an underscore to represent the number of letters in a chosen word
for x in randomWord:
  print("_", end=" ")


def print_hangman(wrong):
    """
    Prints a different piece of the hangman character depending on the number of incorrect guesses
    """
    if(wrong == 0):
        print("\n     ")
        print("     ")
        print("     ")
        print("     ")
        print("   ===")
    elif(wrong == 1): 
        print("\n     ")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
    elif(wrong == 2):
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
    elif(wrong == 3):
        print("\n+---+")
        print(" O  |")
        print("    |")
        print("    |")
        print("   ===")
    elif(wrong == 4):
        print("\n+---+")
        print(" O  |")
        print(" |  |")
        print("    |")
        print("   ===")
    elif(wrong == 5):
        print("\n+---+")
        print(" O  |")
        print("/|  |")
        print("    |")
        print("   ===")
    elif(wrong == 6):
        print("\n+---+")
        print(" O   |")
        print("/|\  |")
        print("     |")
        print("    ===")
    elif(wrong == 7):
        print("\n+---+")
        print(" O   |")
        print("/|\  |")
        print("/    |")
        print("    ===")
    elif(wrong == 8):
        print("\n+---+")
        print(" O   |")
        print("/|\  |")
        print("/ \  |")
        print("    ===")


def printWord(guessedLetters):
    """
    Prints the letters that have been guessed correctly by the player
    and adds an underscore for letters that have not yet been guessed
    """
    counter=0
    rightLetters=0
    for char in randomWord:
        if(char in guessedLetters):
            print(randomWord[counter], end=" ")
            rightLetters+=1
        else:
            print(" ", end=" ")
        counter+=1
    return rightLetters


def printLines():
    """
    Prints a line of dashes to separate each guess
    """
    print("\r")
    for char in randomWord:
        print("\u203E", end=" ")


#variables to keep track of a players progress
length_of_word_to_guess = len(randomWord)
amount_of_times_wrong = 0
current_guess_index = 0
current_letters_guessed = []
current_letters_right = 0
remaining_guesses = 8


while amount_of_times_wrong != 8 and current_letters_right != length_of_word_to_guess:
    """
    A loop that runs as long as the player has not guessed wrong more than 8 times
    """

    #prints all letters guessed by the player
    print("\nLetters guessed:\n ", end="")
    for letter in current_letters_guessed:
        print(letter, end=" ")
    
    #asks the player to input their next guess
    letter_guessed = input("\nGuess a letter: ")

    #checks if the players guess is right
    if randomWord[current_guess_index] == letter_guessed:
        print_hangman(amount_of_times_wrong)
        
        #updates the index if the players guess is correct
        current_guess_index += 1
        current_letters_guessed.append(letter_guessed)
        current_letters_right = printWord(current_letters_guessed)
        printLines()
    
    #checks if the players guess is wrong
    else:
        amount_of_times_wrong += 1
        current_letters_guessed.append(letter_guessed)

        #updates the hangman character after the players input
        print_hangman(amount_of_times_wrong)
        
        #prints the list of letters currently guessed correctly
        current_letters_right = printWord(current_letters_guessed)
        printLines()


if current_letters_right == length_of_word_to_guess:
    """
    Confirmation to the user if they have won or lost
    """
    print(f"Congratulations {name}! You live to see another day!")
else:
    print(f"You lost {name}, lights out for you. The word was '{randomWord}'.")

print("Game over! Thank you for playing Hangman, feel free to try again.")

"""
Credit to Shaun Halverson and his "How To Code Hangman In Python" tutorial for beginners.
His code was used as a foundation for me to build on and modify, creating my own take on the game. 
"""