# import the random module 
import random   
            
# create word and alphabet lists
word_list = ['orange', 'lemons', 'mangoes', 'pineapple', 'strawberries']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


class Hangman():

    def __init__(self, word_list, num_lives = 5):      # Picked randomly from the word_list.
        self.num_lives = num_lives                      # The number of lives the player has at the start of the game.
        self.word = random.choice(word_list) 
        self.num_letters = len(self.word)               #The number of UNIQUE letters in the word that have not been guessed yet.
        self.word_guessed = [self.num_letters*("_")]      # (help!!!) gets me following error: "File "<stdin>", line 1, in <module> 
      
                                                          #                                  NameError: name 'self' is not defined"
        self.list_of_guesses = []
        print("instance initiated...")


    """(help) word_guessed: list - A list of the letters of the word, with '' for each letter not yet guessed. 
        For example, if the word is 'apple', the word_guessed list would be ['', '', '', '', '']. 
        If the player guesses 'a', the list would be ['a', '', '', '', '']    """

    def check_guess(self, guess):

            # gets the letter
            guess = guess.lower()
           
            if guess in self.word:
                print(f"Good guess!,{guess} is in the word")

            else:
                print(f"Sorry, {guess} is not in the word. Try again.")
            
            print("check_guess is working")
        




guess = input("Please enter a letter:")
game = Hangman(word_list)
game.check_guess(guess)




