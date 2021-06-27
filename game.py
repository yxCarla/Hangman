"""
credit to ben for helping me
"""

import time
import random
print("Let's play Hangman!")
time.sleep(1)
print('I am thinking of a word. Can you guess it?')
time.sleep(1)
words = ['chocolate', 'elephant', 'soccer', 'binder', 'restaurant', 'holiday', 'iphone', 'president',
        'cookie', 'television', 'videogames', 'music', 'japanese', 'dictionary', 'xbox', 'tennis', 'obama', 'system',
        'youtube', 'casino', 'monopoly', 'banana', 'rubiks cube', 'computer', 'python', 'typewriter', 'money', 'pencil',
        'airplane', 'trophy', 'picture', 'lizard', 'apple', 'football', 'amazon'] 
attempts = ''
rounds = 10
word = random.choice(words)
while rounds > 0:
    failed = 0

    for char in word:
        if char in attempts:
            print(char, end='')
        else:
            print('_', end='')
            failed += 1
    
    print('')

    if failed == 0:
        print(f'You win! The word was "{word}"')
        break
        
    letter = input('Guess a letter! ')
    attempts += letter
    if letter not in word:
        print('Incorrect!')
        rounds -= 1
        print(f'You have {rounds} attempts left')
    if rounds == 0:
        print(f'You lost! The word was "{word}"')
