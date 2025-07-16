import random
from art import guessing_the_number

def random_answer():
    return random.randint(1,100)

def difficult_select(user_choice)-> int:
    if user_choice == "hard":
        return 5
    else:
        return 10
    
def check_answer(p_guess:int,f_answer:int,turn:int)->int:
    """Check if player answer right or not"""
    if p_guess > f_answer:
        print("Too high")
        turn -= 1
        return turn

    elif p_guess < f_answer:
        print("Too Low")
        turn -= 1
        return turn
    else:
        print(f"Correct!!, the answer is {f_answer}")
        return turn
   

    
def play_game():
    final_answer = random_answer()

    print(guessing_the_number)
    print("Welcome to Number Guessing Game!")
    life = difficult_select(input("Choose a difficulty. Typr 'easy' or 'hard':".lower()))
    game_over = False
    while not game_over:
        print(f"You have {life} attempts remaining to guess the number")
        player_guess = int(input("Make a guess : "))
        life = check_answer(player_guess,final_answer,life)

        if player_guess == final_answer:
            game_over = True
            
        if life == 0:
            print(f"You run out of life, GAME OVER\n The answer is {final_answer}")

            game_over = True
    
    play_again = input("Do you want to play again? (y/n)").lower()
    if play_again == "y":
        print("\n"*50)
        play_game()

play_game()


