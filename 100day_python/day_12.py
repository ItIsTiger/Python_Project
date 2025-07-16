#Modify Global Scope

enemies = 1
enemy = 1
def increase_enemies():
    global enemies
    enemies = 2
    enemy = 2
    print(enemies)

# increase_enemies()
# print(enemies)
# print(enemy)

#Globla scope
player_health = 10

#Global constant
#use all capital 
PI = 3.14567




#local scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)

def is_prime(num:int):
    if num == 1:
        return False
    else:
        for i in range(2,num+1):
            if num%i == 0 and i!= num:
                return False
        return True    

# print(str(is_prime(int(input("Enter the number to check: ")))))

