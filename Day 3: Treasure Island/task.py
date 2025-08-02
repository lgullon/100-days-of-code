print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("You're at a crossroads, will you go left or right?").lower()

if direction == "right":
    print("In the darkness you feel your way towards the right, unknowingly walking right off a cliff. GAME OVER.")
elif direction == "left":
    action = input("Would you like to swim or wait? ").lower()
    if action == "swim":
        print("You were attacked by a trout, and are so weak that you lost. GAME OVER.")
    elif action == "wait":
        door = input("3 doors materialize after you waited long enough, a red one, a yellow one and a blue one."
                     " Which do you pick? ").lower()
        if door == "red":
            print("You opened the red door and waltzed right into a fire, buring to death. GAME OVER.")
        elif door == "yellow":
            print("You open the yellow door to see piles and piles of treasure waiting for you, "
                  "and a path to the outside world. YOU WIN!")
        elif door == "blue":
            print("You open the blue door and are greeted by sharp, snarling fangs. "
                  "You are eaten by beasts. GAME OVER.")
        else:
            print("Not a valid input, shame on you. GAME OVER.")
    else:
        print("Not a valid input, shame on you. GAME OVER.")
else:
    print("Not a valid input, shame on you. GAME OVER.")
