print(len("Hello World")) # This will return the length of the string "Hello World"

print(type(100))  # This will print the type of the number 100, which is <class 'int'>
print(type(100.0))  # This will print the type of the number 100.0, which is <class 'float'>
print(type("Hello World"))  # This will print the type of the string "Hello World", which is <class 'str'>
print(type(True))  # This will print the type of the boolean value True, which is <class 'bool'>

#-------------------------------------------------------------------------------------------------------------------------

print("123" + "456")  # This will concatenate the two strings "123" and "456", resulting in "123456"
print(int("123") + int("456"))  # This will convert the strings "123" and "456" to integers and then add them, resulting in 579

print(number := 100)  # This will assign the value 100 to the variable number and print it
print(f"The value of number is {number}")  # This will print the value of the variable number, which is 100

name = input("Enter your name: ")  
length_name = len(name)  # This will calculate the length of the name entered by the user
print(f"Your name is {name} and it has {length_name} characters.")

#-------------------------------------------------------------------------------------------------------------------------

print("My age: " + str(25))  # This will print "My age: 25" by converting the integer 25 to a string
print(123+456)
print(7 - 3)
print(8 * 2)
print(9 / 3)  # This will print the result of dividing 9 by 3, which is 3.0
print(10 % 3)  # This will print the remainder of dividing 10 by 3, which is 1
print(2 ** 3)  # This will print the result of 2 raised to the power of 3, which is 8  
print(10 // 3)  # This will print the result of integer division of 10 by 3, which is 3

# PEMDAS
print(2 + 3 * 4)  # This will print 14, as multiplication is performed before addition
print((2 + 3) * 4)  # This will print 20, as the parentheses change the order of operations
print(3 * 3 + 3 / 3 - 3)

#-------------------------------------------------------------------------------------------------------------------------
bmi = 84/1.65 **2
print(bmi)

print(int(bmi))
print(round(bmi))  # This will round the BMI to the nearest integer
print(round(bmi, 2))  # This will round the BMI to 2 decimal places

score = 0

score += 1  # This will increment the score by 1
print(score)  # This will print the updated score, which is now 1

print("Your score is: %d" % score)  # This will print "Your score is: 1" using old-style formatting
print(f"Your score is: {score}")  # This will print "Your score is: 1" using f-string formatting
print("Your score is: {}".format(score))  # This will print "Your score is: 1" using the format method

#----------------------------------------------------------------------------------------------------------------------------
#code for bill split  
print("Welcome to the bill split calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
total_bill = bill * (1 + tip / 100)  # Calculate the total bill including tip
bill_per_person = total_bill / people  # Calculate the bill per person
print(f"Each person should pay: ${bill_per_person:.2f}")  # Print the bill per person formatted to 2 decimal places
#----------------------------------------------------------------------------------------------------------------------------

