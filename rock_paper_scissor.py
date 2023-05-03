import random
rock='''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper='''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors='''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''  
game=[rock, paper, scissors]
num=int(input("enter 0 for rock, 1 for paper and 2 for scissors"))
computer=random.randint(0,2)
if num==computer:
    print(game[num])
    print(game[computer])
    print("Match Draw")
elif num==0 and computer==1:
    print(game[num])
    print(game[computer])
    print("You Loose")
elif num==0 and computer==2:
    print(game[num])
    print(game[computer])
    print("You WIn")
elif num==1 and computer==0:
    print(game[num])
    print(game[computer])
    print("You WIn")
elif num==1 and computer==2:
    print(game[num])
    print(game[computer])
    print("You Loose")
elif num==2 and computer==0:
    print(game[num])
    print(game[computer])
    print("You Loose")
elif num==2 and computer==1:
    print(game[num])
    print(game[computer])
    print("You Win")
else:
    print("enter valid input")


