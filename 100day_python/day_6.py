def my_function():
    print("This is my function in day 6 of the 100-day Python challenge.")

my_function()

#Laerning about for loops and range also while 

def turn_left():
    print("Turning left")

def move():
    print("Moving forward")

def turn_right():
    turn_left()
    turn_left()
    turn_left() 

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left() 


def turn_right():
    turn_left()
    turn_left()
    turn_left() 

def wall_on_right():
    return False  # Placeholder for actual wall detection logic

def front_is_clear():
    return True  # Placeholder for actual front clear logic

def at_goal():
    return False  # Placeholder for actual goal detection logic

def wall_in_front():
    return True  # Placeholder for actual wall detection logic

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

    
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

    