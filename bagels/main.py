import random
from .helpers import getSecretNum, getClues


NUM_DIGITS: int = 3
MAX_GUESSES: int = 10

def main():
    print('''
    Let's Play Bagels
    - A game inspired by the bagels game presented in the Al-Sweigart

    Rules are pretty simple, you will have to guess {} digit number and you will
    get {} tries to do that!

    If you guess a number which has digits in the right place you will see a 'Fermi' Output
    And if you guess a number which has correct digit but at the wrong place, you will see a 'Pico' message.
    And if your number doesn't satisy the above conditions you will receive a 'Bagel Output'
    '''.format(NUM_DIGITS, MAX_GUESSES))

    while True:

        secretNum: str = getSecretNum()
        print('The Numbers been decided, let\'s begin guess game')

        numGuesses: int = 1
        while numGuesses < MAX_GUESSES:
            guess: str = ''
            while len(guess) < NUM_DIGITS and guess.isdecimal():
                print('Enter your guess\n')
                guess = input('> ')
            
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            
            if numGuesses>MAX_GUESSES:
                print('You ran out of guesses')
                print('The Secret Number was {}'.format(secretNum))
                break







