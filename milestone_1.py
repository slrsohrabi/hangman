
import random

from secrets import choice

word_list = ['orange', 'lemons', 'mangoes', 'pineapple', 'strawberries']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

word = random.choice(word_list)

print(word)


guess = input("Please enter a letter: ")


if len(guess) == 1 and guess.lower() in alphabet:
    
    print ("Good guess!")

else:
    
    print("Oops! That is not a valid input.")

