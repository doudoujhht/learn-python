


import random

HANGMANPICS = ['''
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

#Word bank of animals
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

def print_hangman_choice(guess):
    for i in guess:
        print(i, end=" ")
    print("\n")
    

while True:
    is_win = False
    is_lose = False
    word = words[random.randint(0, len(words) - 1)]
    guess = []
    nbOfTry = 0
    nb_of_correct_guess = 0
    all_guess = []
    for i in range(len(word)):
        guess.append('_')
    print_hangman_choice(guess)
    while not is_lose and not is_win:
        guess_letter = input("Guess a letter: ")
        if len(guess_letter) != 1:
            print("Please enter a single letter")
            continue

        if guess_letter in all_guess:
            print("You already guess the letter", guess_letter)
            continue


        all_guess.append(guess_letter)
        if guess_letter in word:
            for i in range(len(word)):
                if word[i] == guess_letter:
                    guess[i] = guess_letter
                    nb_of_correct_guess += 1

            if nb_of_correct_guess == len(word):
                is_win = True
                print("You win!")
                continue

        else:
            print(HANGMANPICS[nbOfTry])
            if nbOfTry == 6:
                is_lose = True
                print("it was", word)
                print("You lose!")
                continue

            nbOfTry += 1
        print_hangman_choice(guess)
    
    play_again = input("Do you want to play again? (y/n)")
    if play_again.lower() != 'y':
        print("Bye!")
        break
