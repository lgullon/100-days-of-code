import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

player = int(input("Rock, Paper, or Scissors? Enter 0 for rock, 1 for paper, and 2 for scissors: \n"))
if user >= 0 or user <= 2:
    print(options[player])
computer = random.randint(0, 2)
print("Computer chose: \n" + options[computer])

if player != 0 or player != 1 or player != 2:
    print("You typed an invalid number. You lose!")
elif computer == player:
    print("It's a draw")
elif (computer == 0 and player == 1) or (computer == 1 and player == 2) or (computer == 2 and player == 0):
    print("You win!")
else:
    print("You lose")


# if player == 0 and computer == 2:
#     print("You win!")
# elif computer == 0 and player == 2:
#     print("You lose!")
# elif computer > player:
#     print("You lose!")
# elif player > computer:
#     print("You win!")
# elif computer == player:
#     print("It's a draw!")
# else:
#     print("You typed an invalid number. You lose!")
