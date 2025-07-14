print("Welcome to the rolercoaster!")   
height = float(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bills = 5
        print("Please pay $5.")
    elif age <= 18:
        bills = 7
        print("Please pay $7.")
    elif 45 <= age <= 65:
        bills = 12
        print("Everting is going to be ok, come ride with us.")
    else:
        bills = 12
        print("Please pay $12.")
    wants_photo = input("Do you want a photo taken? (Y/N) ").strip().upper()
    if wants_photo == 'Y':
        bills += 3
        print(f"Your total bill is ${bills} including the photo.")
    else:
        print(f"No photo taken, Your total bill is ${bills}, enjoy your ride!")
else:
    print("Sorry, you have to grow taller before you can ride.")


#--------------------------------------------------------------------------------------------------

weight = 85
height = 1.85

bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi:.2f}")  # Print the BMI rounded to 2 decimal places

# 🚨 Do not modify the values above
# Write your code below 👇

if bmi <18.5:
    print("underweight")
elif 18.5 < bmi < 25:
    print("normal weight")
else:
    print("overweight")


#--------------------------------------------------------------------------------------------------
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: \n").strip().upper()
add_pepperoni = input("Do you want pepperoni? Y or N: \n").strip().upper()
extra_cheese = input("Do you want extra cheese? Y or N: \n").strip().upper() 
bill = 0
# Calculate the bill based on the size and toppings

if size == 'S':
    bill = 15
elif size == 'M':
    bill = 20
elif size == 'L':
    bill = 25  

# Add costs for pepperoni 
if add_pepperoni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3

# Add cost for extra cheese
if extra_cheese == 'Y':
    bill += 1

# Print the final bill amount
print(f"Your final bill is: ${bill}")
#--------------------------------------------------------------------------------------------------

print("Welcoime to Treasure Island!")
print("Your mission is to find the treasure.")  # Prompt the user for their mission
choice1 = input("You're at a crossroad. Do you want to go left or right? \n").strip().lower()
if choice1 == "left":
    choice2 = input("You've come to a lake. Do you want to swim across or wait for a boat? \n").strip().lower()
    if choice2 == "wait":
        choice3 = input("You arrive at a house with three doors. One red, one yellow, and one blue. Which color do you choose? \n").strip().lower()
        if choice3 == "yellow":
            print("You found the treasure! You win!")
        elif choice3 == "red":
            print("It's a room full of fire. Game over.")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game over.")
        else:
            print("You chose a door that doesn't exist. Game over.")
    else:
        print("You got attacked by an angry trout. Game over.")
else:
    print("You fell into a hole. Game over.")
