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

choices = [rock, paper, scissors]
choice_player = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors.\n"))

if choice_player>=3:
  print("You chose an invalid number, you lose")
else:
  print(choices[choice_player])


  import random
  choice_computer = random.randint(0,2)
  print("the computer chose:")
  print(choices[choice_computer])



  if choice_player == choice_computer:
    print("there is a draw")
  elif choice_player < choice_computer:
    if choice_player==0:
      if choice_computer==1:
        print("you lose")
      elif choice_computer==2:
        print("you win")
    elif choice_player==1:
      print("you lose")
  elif choice_player>choice_computer:
    if choice_player==1:
      print("you win")
    elif choice_player==2:
      if choice_computer==0:
        print("you lose")
      if choice_computer==1:
        print("you win")
