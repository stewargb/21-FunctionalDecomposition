"""
Hangman.

Authors: Grant Stewart and Zachary Juday.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implement Hangman using your Iterative Enhancement Plan.

####### Do NOT attempt this assignment before class! #######

import random

with open('words.txt') as f:
    f.readline()
    string = f.read()
    words = string.split()

def main():
    word = random_word(words)
    print(word)
    hangman_main(word)
    play_again()

def random_word(words):
    r = random.randrange(0,len(words))
    item = words[r]
    return item

def hangman_main(word):
    n = int(input('please enter a number of trys: '))
    blank = []
    for _ in range(len(word)):
       blank = blank + ['-']
    print(blank)
    win = len(word)
    letters_correct = 0
    while True:
        guess = str(input('Please guess a letter: '))
        check = 0
        for k in range(len(word)):
            if word[k] == guess:
                blank[k] = word[k]
                check = 1
                letters_correct += 1
        if check == 1:
            print('Good guess! You still have',n,'unsuccesful guesses left before you Lose the game')
        if check == 0:
            n = n-1
            print('Sorry! There are no',guess,'letters in the secret word. You have',n,'unsuccessful guesses left before you LOSE the game!')
        print(blank)
        if n == 0:
            print('You lose! The secret word was:',word)
            break
        if letters_correct == win:
            print('Congratulations, you WIN! the word was:', word)
            break
def play_again():
    y = 'y'
    n = 'n'
    x = input('Play another game? (y/n):')
    x.strip().lower()
    if y == x:
        main()
    if n == x:
        print('Thanks for playing Hangman!')



main()