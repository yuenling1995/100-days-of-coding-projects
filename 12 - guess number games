#Here I listed 2 ways to do this:

from art import logo 
import random

print(logo)

answer = random.randint(1,100)
is_game_over = False

game_level = input("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nChoose a difficulty. Type 'easy' or 'hard': ")

if game_level== "easy":
  attempt = 10
elif game_level== "hard":
  attempt = 5

while not is_game_over and attempt>0:

  print(f"You have {attempt} remaining to guess the number.")

  guess_number = int(input("Make a guess: "))
  attempt-=1

  if guess_number>answer:
    print("Too high.\nGuess again.")
  elif guess_number<answer:
    print("Too low.\nGuess again.")
  elif guess_number==answer:
    print(f"You got it. The answer was {answer}.")
    is_game_over = True

if attempt==0 and guess_number!=answer:
  print("You have run out of your guesses,you lose.")
  
  
  
  
  
  
  
  
  
  
#Here's the 2nd way:
import random
from art import logo

EASY_ATTEMPT = 10
HARD_ATTEMPT = 5

#this function is to compare the guess to the answer
def compare(guess,answer,attempt):
  if guess>answer:
    print("Too high.")
    return attempt-1
  elif guess<answer:
    print("Too low.")
    return attempt-1
  elif guess==answer:
    print(f"You got it. The answer was {answer}.")


#this function sets game difficulty level
def game_level():
  if input("Choose a difficulty. Type 'easy' or 'hard': ") == 'easy':
    return EASY_ATTEMPT
  else:
    return HARD_ATTEMPT

#define this function so we can use all the global variables
def game():
  print(logo)

  answer = random.randint(1,100)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")

  attempt = game_level()

  guess=0
  while guess !=answer: 
    print(f"You have {attempt} remaining to guess the number.")

    guess = int(input("Make a guess: "))

    attempt = compare(guess,answer,attempt)
    if attempt==0:
      print("You have run out of your guesses,you lose.")
      return 
    elif guess!=answer:
      print("Guess again.")


game()
