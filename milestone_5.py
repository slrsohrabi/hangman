# import the random module 
import random   

class Hangman():

    def __init__(self, word_list, num_lives = 5):      # Picked randomly from the word_list.
        self.num_lives = num_lives                      # The number of lives the player has at the start of the game.
        self.word = random.choice(word_list) 
        self.num_letters = len(self.word)               #The number of UNIQUE letters in the word that have not been guessed yet.
        self.word_guessed = self.num_letters*["_"]     
        self.list_of_guesses = []
        print(f"{self.word}")
        print(f"{self.word_guessed}")

    def check_guess(self, guess):
        if guess in self.word:
            print(f"Good guess!,{guess} is in the word")
            for i in range(len(self.word)):
                if guess == self.word[i]:
                    self.word_guessed[i] = guess        
            self.num_letters += -1   
            print(f"{self.word_guessed}")
            return self.word_guessed
        else:
            self.num_lives += -1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"you have {self.num_lives} left...")       

    def ask_for_input(self):
        self.guess = input("Please enter a letter:").lower()
        if len(self.guess) != 1 or self.guess.isalpha() == False :
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif self.guess in self.list_of_guesses:
            print("You already tried that letter!")
        else : 
            self.check_guess(self.guess)
            self.list_of_guesses.append(self.guess)
                
def play_game():   
    word_list = ['orange', 'lemons', 'mangoes', 'pineapple', 'strawberries']           
    game = Hangman(word_list)                               # step 3 & 4
    while True:
        if game.num_lives == 0 :                 # step 5.1
            print('you lost!')
            break
        elif game.num_lives >= 0 and game.num_letters == 0 :
            print('you won!')
            break
        else: 
            game.ask_for_input()

play_game()

#add option of fruit, car brand, pokemon, guitar brands, authors, rock bandsquit

