import random

HANGMANSTATUS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def draw_board(missed_chars, correct_chars, secret_word):
    print(HANGMANSTATUS[len(missed_chars)])
    print()
    print('Missed characters:', end=' ')
    for letter in missed_chars:
        print(letter, end=' ')
    print()
    for char in secret_word:
        if char in correct_chars:
            print(char, end=' ')
            continue
        print('-', end=' ')
    print()

def get_guess(already_guessed):
    while True:
        guess = input('Guess a character: ')
        if len(guess) != 1:
            print('Please only use one character.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please use a character that is in the alphabet.')
        elif guess in already_guessed:
            print('Please pick a character, that you have not used yet.')
        else:
            return guess

def check_win(secret_word, correct_chars):
    for char in secret_word:
        if char not in correct_chars:
            return False
    print('You have guessed the word! It was "{0}".'.format(secret_word))
    return True

def check_lose(missed_chars, correct_chars, secret_word):
    if len(missed_chars) == len(HANGMANSTATUS) - 1:
        missed = len(missed_chars)
        correct = len(correct_chars)
        word = secret_word
        print(HANGMANSTATUS[len(missed_chars)])
        print('You have used up all your guesses! With {0} missed guesses and {1} correct guesses, the word was "{2}".'.format(missed, correct, word))
        return True

def hangman():
    words = ('house mouse california calling missing letter graveyard sanctuary').split()
    secret_word = random.choice(words)
    missed_chars = ''
    correct_chars = ''
    game_is_done = False
    while not game_is_done:
        draw_board(missed_chars, correct_chars, secret_word)
        already_guessed = missed_chars + correct_chars
        guess = get_guess(already_guessed)
        if guess in secret_word:
            correct_chars = correct_chars + guess
            if check_win(secret_word, correct_chars): game_is_done = True
        elif guess not in secret_word:
            missed_chars = missed_chars + guess
            if check_lose(missed_chars, correct_chars, secret_word): game_is_done = True

if __name__ == '__main__':
    hangman()