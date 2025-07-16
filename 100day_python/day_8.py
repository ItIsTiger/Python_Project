#Code to print star in pyramid shape
def print_star_pyramid(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))

# n = int(input("Enter the number of rows for the star pyramid: "))
# print_star_pyramid(n)

def life_in_week(age):
    total_week = 90*52
    your_life_spen = age*52
    time_left = total_week - your_life_spen
    print(f"You have {time_left} weeks left.")

def greet_with(name, location):
    print(f"Hello {name}, welcome to {location}!")

greet_with("Alice", "Wonderland")

def calculate_love_score(name1:str,name2:str):
    concat_str = "".join((name1+name2).split()).upper()
    print(concat_str)
  
    T_Score=R_Score=U_Score=E_Score=L_Score=O_Score=V_Score=0
    for string in concat_str:
        if string == "T":
            T_Score += 1
        elif string == "R":
            R_Score += 1 
        elif string == "U":
            U_Score += 1 
        elif string == "E":
            E_Score += 1
        elif string == "L":
            L_Score += 1 
        elif string == "O":
            O_Score += 1
        elif string == "V":
            V_Score += 1 
    True_Score = T_Score + R_Score + U_Score + E_Score
    Love_Score = L_Score + O_Score + V_Score + E_Score
        
    print(f"T occurs {T_Score} times")
    print(f"R occurs {R_Score} times")
    print(f"U occurs {U_Score} times")
    print(f"E occurs {E_Score} times")
    print(f"Total = {True_Score}")
    print(f"L occurs {L_Score} times")
    print(f"O occurs {O_Score} times")
    print(f"V occurs {V_Score} times")
    print(f"E occurs {E_Score} times")
    print(f"Total = {Love_Score}")
    
    print(f"Love Score = {True_Score*10 + Love_Score}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cipher(text, shift, direction):
    result = ""
    if direction == "encode":
        for char in text:
            if char.isalpha():
                index = alphabet.index(char.lower())
                new_index = (index + shift) % len(alphabet)
                new_char = alphabet[new_index]
                if char.isupper():
                    new_char = new_char.upper()
                result += new_char
            else:
                result += char
    elif direction == "decode":
        for char in text:
            if char.isalpha():
                index = alphabet.index(char.lower())
                new_index = (index - shift) % len(alphabet)
                new_char = alphabet[new_index]
                if char.isupper():
                    new_char = new_char.upper()
                result += new_char
            else:
                result += char
    return result

def main():
    print("Welcome to the Caesar Cipher!")
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    while direction not in ["encode", "decode"]:
        print("Invalid choice. Please type 'encode' or 'decode'.")
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))
    if shift > len(alphabet):
        shift = shift % len(alphabet)
    print(f"The {direction}d text is: {caesar_cipher(text, shift, direction)}")
    next_action = input("Type 'yes' to continue with another operation, or 'no' to exit:\n").lower()
    while next_action not in ["yes", "no"]:
        print("Invalid choice. Please type 'yes' or 'no'.")
        next_action = input("Type 'yes' to continue with another operation, or 'no' to exit:\n").lower()
    if next_action == "yes":
        main()
    else:   
        print("Thank you for using the Caesar Cipher program. Goodbye!")


if __name__ == "__main__":
    print((-1)% 26)  # Example usage of modulo operation
    # main()
    
