import random


#Rock Paper Scissors Game
def play_game():
    choices = ["rock", "paper", "scissors"]
    user_choice = input("Enter rock, paper, or scissors: ").strip().lower()
    
    if user_choice not in choices:
        print("Invalid choice! Please try again.")
        return play_game()  # Restart the game if invalid input
    
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")

def random_integer():
    random_number = random.randint(1, 100)
    print(f"Random integer between 1 and 100: {random_number}")

def random_float():
    random_float = random.random() * 10
    print(f"Random float : {random_float}")

    random_number = random.uniform(1, 10)
    print(f"Random float between 1 and 10: {random_number}")

def heads_or_tails():
    result = random.randint(0, 1)
    if result == 0:
        print("Heads")
    else:
        print("Tails")


#--------------------------------------------------------------------------------------------

state_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
                    "Massachusetts", "Maryland", "South Carolina", "New Hampshire",
                    "Virginia", "New York", "North Carolina", "Rhode Island",
                    "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana"]
state_of_america.extend(["Indiana", "Mississippi", "Illinois", "Alabama", "Maine",
                         "Missouri", "Arkansas", "Michigan", "Florida", "Texas",
                            "Iowa", "Wisconsin", "California", "Minnesota", "Oregon",
                            "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                            "North Dakota", "South Dakota", "Montana", "Washington",
                            "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico",
                            "Arizona", "Alaska"])
state_of_america.append("Hawaii")

def print_states():
    print(len(state_of_america), "states in America:")
    for state in state_of_america:
        print(state)


def who_will_pay():
    print("Welcome to the Who Will Pay?")
    names = input("Enter the names of people separated by commas: ").split(",")
    if not names:
        print("No names provided.")
        return
    payer = random.choice(names).strip()
    print(f"{payer} will pay the bill today!")

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: ")
    rock = '''
     ___________
---\'       ____)
         (_____)
         (_____)
         (____)
------.  (____)

    '''
    paper = '''
           ______
---\'       ______)
           _____)
           _____)
            ____)
-----.      ____)

     '''    
    scispors = '''
            _______
---\'         ____)__
                _____))        
                _____))
            (____)
-----.      (____)

    '''
    choices = [rock, paper, scispors]
    choices_str = ["rock", "paper", "scispors"]
    
    if user_choice.isdigit() and int(user_choice) in [0, 1, 2]:
        print(f"You chose:\n{choices_str[int(user_choice)]}")
        print(choices[int(user_choice)])
    else:
        print("Invalid choice! Please enter 0, 1, or 2.")
    compuer_choice = random.randint(0, 2)
    print(f"Computer chose:\n{choices_str[compuer_choice]}")
    print(f"Computer chose:\n{choices[compuer_choice]}")
    if user_choice == str(compuer_choice):
        print("It's a draw!")
    elif (user_choice == '0' and compuer_choice == 2) or \
         (user_choice == '1' and compuer_choice == 0) or \
         (user_choice == '2' and compuer_choice == 1):
        print("You win!")
    else:
        print("You lose!")

rock_paper_scissors()