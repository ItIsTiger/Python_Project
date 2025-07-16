import art
import random
#Blackjack Game
def blackjack():
    card = {
        "A": 11,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "K": 10,
        "AA" : 1 # Ace can also be 1
    }

    def calculate_score(card_in,score,card_index=card):
        """Calculate the score of the cards."""
        new_score = score
        if score == 21 and len(card_in) == 2:
            return card_in,int(new_score)
          # Calculate scores if over 21, change Ace to 1
        if score > 21 and "A" in card_in:
            card_in.remove("A")
            card_in.append("AA")
            new_score = sum(card_index[card_h] for card_h in card_in)
        return card_in,int(new_score)

    card_values = list(card.values())
    card_keys = list(card.keys())
    card_keys.remove("AA")  # Remove Ace from the list to avoid confusion
    player_cards = []
    computer_cards = []
    player_score = 0
    computer_score = 0
    game_over = False
    print(art.black_jack_logo)
    print("Welcome to Blackjack!")
    while not game_over:
        #randomly draw two cards for player and computer
        player_cards.append(random.choice(card_keys))  # Using random.choice to simulate drawing a card
        player_cards.append(random.choice(card_keys)) 
        computer_cards.append(random.choice(card_keys))
        computer_cards.append(random.choice(card_keys))
        

        player_score = sum(card[card_h] for card_h in player_cards)
        computer_score = sum(card[card_h] for card_h in computer_cards)

        # Calculate scores
        player_cards, player_score = calculate_score(player_cards, player_score)
        computer_cards, computer_score = calculate_score(computer_cards, computer_score)

        print(f"Your cards: {player_cards}, current score: {player_score}")

        


        print(f"Computer's first card: {computer_cards[0]}")
        if player_score == 21:
            print("Blackjack! You win!")
            game_over = True
        elif player_score > 21:
            print("You went over 21. You lose!")
            game_over = True
        else:
            draw = True
            another_card = input("Type 'y' to get another card, 'n' to pass: ").strip().lower()
            if another_card == 'y':
                while draw:
                    player_cards.append(random.choice(card_keys))  
                    player_score = sum(card[card_h] for card_h in player_cards)
                    player_cards, player_score = calculate_score(player_cards, player_score)
                    print(f"Your cards: {player_cards}, current score: {player_score}")
                    if player_score > 21:
                        print("You went over 21. You lose!")
                        game_over = True
                        draw = False
                        continue
                    draw_more = input("Do you want to draw more cards? (yes/no): ").strip().lower()
                    if draw_more == 'no' or draw_more == 'n':
                        draw = False

            else:
                draw = False
            if not game_over:
                while computer_score < 17:
                    computer_cards.append(random.choice(card_keys))
                    computer_score = sum(card[card_h] for card_h in computer_cards)
                    computer_cards,computer_score = calculate_score(computer_cards, computer_score)
            print(f"Computer's cards: {computer_cards}, final score: {computer_score}")
            if not game_over and computer_score < 22:
                if computer_score > 21 or player_score > computer_score :
                    print("You win!")
                    game_over = True
                elif player_score < computer_score:
                    print("You lose!")
                    game_over = True
                else:
                    print("It's a draw!")
                    game_over = True
            else:
                game_over = True

           
        if game_over:
            print("Game Over! Thanks for playing.")
            want_to_play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if want_to_play_again == 'yes' or want_to_play_again == 'y':
                blackjack()
            else:
                break

# Start the game
if __name__ == "__main__":
    blackjack()