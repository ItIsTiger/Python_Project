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
        return card_in
        # Calculate scores if over 21, change Ace to 1
    if score > 21 and "A" in card_in:
        card_in.remove("A")
        card_in.append("AA")
        new_score = sum(card_index[card_h] for card_h in card_in)
    return card_in,new_score

card_player = ["A"  , "K" ,"2"]
player_score = sum(card[card_h] for card_h in card_player)
card_player, player_score = calculate_score(card_player, player_score)
print(f"Player's cards: {card_player}, score: {player_score}")