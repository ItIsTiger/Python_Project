from art import black_jack_logo
import random
#Blackjack Game
def deal_card():
    """Returns a random card from the deck."""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]  # 11 represents Ace
    return random.choice(cards)

def calculate_score(cards):
    """Take a list of card and return score calculate with a list"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    else:
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
    return sum(cards)

def compare_score(u_score,c_score):
    """Compare User Score with Computer Score to find out who will win"""
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, opponent has Blackjack!!!"
    elif u_score == 0:
        return "Win with Blackjack!!!"
    elif u_score > 21:
        return "You went over, game over"
    elif u_score > c_score:
        return "You win"
    else:
        return "You lose"

def play_game():
    print(black_jack_logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}: Current Score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_should_card = input("Do you want to draw another card? (y/n): \n")
            if user_should_card == "y":
                user_cards.append(deal_card())
            else:
                game_over = True


    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your Final hand is: {user_cards} and your score is {user_score}")
    print(f"Computer's final hane: {computer_cards}, final score {computer_score}")
    print(compare_score(user_score,computer_score))

    next_round = input("Do you want to play another round?").lower().strip()
    if next_round == "y":
        print("\n"*50)
        play_game()

play_game()






        

