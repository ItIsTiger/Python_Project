import random
from hangman_word import word_list

die =''' 
_________
|         |
|         O
|        /|\\
|        / \\
|
|_________'''

start = '''
_________
|         |
|         
|        
|        
|
|_________'''


missed_1 = '''
_________
|         |
|         O
|        
|        
|
|_________'''


missed_2 = '''
_________
|         |
|         O
|          \\
|
|
|_________'''

missed_3 = '''
_________
|         |
|         O
|        / \\
|
|
|_________'''

missed_4 = '''
_________
|         |
|         O
|        /|\\
|
|
|_________'''

missed_5 = '''
_________
|         |
|         O
|        /|\\
|        /
|
|_________'''



def get_hangman_stage(misses):
    stages = [
        start,
        missed_1,
        missed_2,
        missed_3,
        missed_4,
        missed_5,
        die
    ]
    return stages[misses]


print("Welcome to Hangman!")
def play_hangman(word):
    print("Let's play Hangman!")
    print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/   
          
          ''')
    word = word.lower()
    guessed_letters = set()
    misses = 0
    max_misses = 6


    while misses < max_misses:
        print(get_hangman_stage(misses))

        # display = []
        # for letter in word:
        #     if letter in guessed_letters:
        #         display.append(letter)
        #     else:
        #         display.append('_')

        # print("Word:", ' '.join(display))
        # use join to create the display string
        
        print("Word:", ' '.join(letter if letter in guessed_letters else '_' for letter in word))
        print("Guessed letters:", ' '.join(sorted(guessed_letters)))

        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            misses += 1
            print(f"Wrong guess! You have {max_misses - misses} tries left.")
        else:
            print("Good guess!")

        # success = True
        # for letter in word:
        #     if letter not in guessed_letters:
        #         success = False
        #         break

        # if success:
        #     print("You guessed it!")
        #use all() to check if all letters in the word are guessed

        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You've guessed the word: {word}")
            print(''' 

             __     ______  _    _   _    _   _  ____  _   _ 
             \ \   / / __ \| |  | | | |  | | | |/ __ \| \ | |
              \ \_/ / |  | | |  | | | |  | | | | |  | |  \| |
               \   /| |  | | |  | | | |  | | | | |  | | . ` |
                | | | |__| | |__| | | |__| |_| | |__| | |\  |
                |_|  \____/ \____/  \____/\___/ \____/|_| \_|
''')

            return

    print(get_hangman_stage(misses))
    print(f"Game over! The word was: {word}")

#Code for random word hangman game
def get_random_word():
    words = ["python", "hangman", "challenge", "programming", "developer"]
    return random.choice(word_list)
word = get_random_word()
play_hangman(word)