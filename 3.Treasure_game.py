print(''' *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
      ''')
      
      
print("welcome to the treasure island\n your mission is to find the treasure")
choice1=input("where do you want to head left or right?").lower()
if choice1=="left":
    print("you have reached the lake\n Now do you want to swim or wait? ")
    choice2=input("").lower()
    if choice2=="wait":
        print("a door appears\n which door you want to go in")
        choice3=input("red or yellow or blue? ").lower()
        if choice3=="yellow":
            print("wohhooo,you find the treasure\n, now go back and code")
        else:
            print("bad for you no treasure through this door, you loose\n now go and code again lol")
       
    else:
        print("you died, crocodile.....Game Over")
else:
    print("oops game over, you fell of the cliff ")