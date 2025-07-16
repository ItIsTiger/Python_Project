try:
    age= int(input("How old are you?"))
except ValueError:
    print("You have typed in an invalid number")
    age= int(input("How old are you?"))