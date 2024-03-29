import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', "r")
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word


def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''

    # TODO: Loop through the letters in the secret_word and check if a letter is not in letters_guessed
    letters = "".join([i for i in secret_word if i in letters_guessed])
    if letters == secret_word:
        return True
    else:
        return False
    # pass


def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    # TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    guessed_word = [i if i in letters_guessed else '_' for i in secret_word]
    return "".join(guessed_word)


def playagain(player):
    while True:
        if player.isalpha():
            if player == 'y':
                spaceman(load_word())
            elif player == 'n':
                print('Bye Bye!')
                return False
            else:
                print('Not an option!')
                continue
        else:
            print('Not a letter!')
            continue


def get_valid_input():
    while True:
        guess = input('Please guess a letter: ').lower().strip()
        if guess.isalpha():
            if len(guess) > 1:
                print('Not a valid input: ' + guess)
                continue
            else:
                return guess
                break
        else:
            print('Not a valid input: ' + guess)
            continue


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    # TODO: show the player information about the game according to the project spec
    print("Welcome to Spaceman!")
    print('------------')
    print("The secret word contains: " + str(len(secret_word)) + " letters")
    # TODO: Ask the player to guess one letter per round and check that it is only one letter
    # TODO: Check if the guessed letter is in the secret or not and give the player feedback
    # TODO: show the guessed word so far
    # TODO: check if the game has been won or lost

    wordGuessed = False
    guess = ""
    letters_guessed = []
    guesses_left = len(secret_word)

    while guesses_left > 0 and guesses_left <= len(secret_word) and wordGuessed is False:
        if secret_word == get_guessed_word(secret_word, letters_guessed):
            wordGuessed = True
            break
        print('You have ' + str(guesses_left) + ' guesses left.')

        guess = get_valid_input()

        if guess in letters_guessed:
            if guess in letters_guessed:
                print("Oops! You've already guessed that letter: " +
                      get_guessed_word(secret_word, letters_guessed))
                print('------------')
            else:
                letters_guessed.append(guess)
                print('Good guess: ' +
                      get_guessed_word(secret_word, letters_guessed))
                print('------------')
        else:
            if guess in letters_guessed:
                print("Oops! You've already guessed that letter: " +
                      get_guessed_word(secret_word, letters_guessed))
                print('------------')
            else:
                letters_guessed.append(guess)
                guesses_left -= 1
                print('Oops! That letter is not in the word: ' +
                      get_guessed_word(secret_word, letters_guessed))
                print('------------')
    if is_word_guessed(secret_word, letters_guessed):
        print('Congratulations, you won!')
        player = input("Would you like to play again? (y/n): ").lower().strip()
        playagain(player)
    elif guesses_left == 0:
        print('Sorry, you ran out of guesses. The word was ' + secret_word)
        player = input("Would you like to play again? (y/n): ").lower().strip()
        playagain(player)


# These function calls that will start the game
secret_word = load_word()
# spaceman(secret_word)

def test_guessed_word():
    assert get_guessed_word("apple",['a','l','e']) == "a__le"
    assert get_guessed_word("apple",['a','x','b']) == "a____"

def test_word_guessed():
    assert is_word_guessed('alligator',['a','l','i','g','t','o','r']) ==True
    assert is_word_guessed('alligator',['a','l','i','t','o','r']) ==False
    
def test_pay_again():
    assert playagain('n')==False
