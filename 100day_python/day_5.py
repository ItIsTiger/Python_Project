fruits = [
    "apple",
    "banana",
    "cherry",
    "date",
    "elderberry",
    "fig"
]

for fruit in fruits:

    print(fruit)

print(fruits)

#--------------------------------------------------------------------------------------------------
import random
def random_student_scores():
    student_scores = []
    for _ in range(15):  # Generate scores for 15 students
        student_scores.append(random.randint(0, 100))
    print("Student scores:", student_scores)
    total_score = sum(student_scores)
    max_score = max(student_scores)
    average_score = total_score / len(student_scores)
    print(f"Total score: {total_score}")
    print(f"Max score: {max_score}")
    print(f"Average score: {average_score:.2f}")

#Code to print star in pyramid shape
def print_star_pyramid(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))

#---------------------------------------------------------------------------------------------------

import random
import string
def generate_password(length=12, include_symbols=True):
    print("Welcome to PyPassword Generator!")
    characters = string.ascii_letters + string.digits
    if include_symbols:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
print("Generated password:", generate_password(16, True))  # Example with no symbols

def gen_pass():
    letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbol = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    print("Welcome to PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password? "))
    nr_symbols = int(input("How many symbols would you like? "))
    nr_numbers = int(input("How many numbers would you like? "))
    
    #Easy Level
    password = ""
    for _ in range(nr_letters):
        password += random.choice(letter)
    for _ in range(nr_symbols):
        password += random.choice(symbol)   
    for _ in range(nr_numbers):
        password += random.choice(number)
    print("Your password is:", password)

    #Hard Level
    password_list = []
    for _ in range(nr_letters):
        password_list.append(random.choice(letter))
    for _ in range(nr_symbols):
        password_list.append(random.choice(symbol))
    for _ in range(nr_numbers):
        password_list.append(random.choice(number))
    random.shuffle(password_list)  # Shuffle the list to randomize the order
    password_hard = ''.join(password_list)
    print("Your hard password is:", password_hard)
gen_pass()



