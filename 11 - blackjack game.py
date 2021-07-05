import random 
from replit import clear 
from art import logo 

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

#draw cards randomly
def deal_card():
  cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  card = random.choice(cards)
  return card

#calculate scores with checking blackjack and ace
def calculate_score(cards):
  if sum(cards)>21 and len(cards)==2:
    return 0
  if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

#compare the scores and determine the results
def compare(user_score,computer_score):
  #Bug fix. If you and the computer are both over, you lose.
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"
  elif user_score== computer_score:
    return "there is a draw"
  elif user_score == 0:
    return "You win with a blackjack"
  elif computer_score == 0:
    return "You lose, the opponent has a blackjack"
  elif user_score>21:
    return "You went over 21, you lose"
  elif computer_score>21:
    return "The opponent went over 21, you win"
  elif user_score>computer_score:
    return "You win with a higher score"
  else:
    return "You lose with a lower score"


def play_game():

  print(logo)

  user_cards = []
  computer_cards = []
  continue_to_play = True

  #randomly draw 2 cards for each player
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  #use a while loop to iterate the game
  while continue_to_play == True:
    #calculate the initial scores
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    #print out the initial score
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    #check if either player has a blackjack
    if user_score>21 or computer_score==0 or user_score==0:
      continue_to_play == False
    else:
    #use this input to start the iteration
      if input("Type 'y' to get another card, type 'n' to pass: ") == "y":
        user_cards.append(deal_card())
      else:
        #use this to stop the user draw and start the computer draw
        continue_to_play == False

  #computer's turn to draw cards
  while computer_score<17 and computer_score!=0:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  #print out two players' final scores
  print(f"Your final hand is: {user_cards}, final score: {user_score}")
  print(f"Computer's final hand is: {computer_cards}, final score: {computer_score}")

  #compare the scores 
  print(compare(user_score, computer_score))

#ask if wanna restart the game and clear the console
while input("Do you wanna paly a game of Blacjkack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()
