from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo 
print (logo)

print("Welcome to the secret auction program.")

continue_game = True
auction_list = {}


while continue_game == True:
  name = input("What is your name?\n")
  price = int(input("What's your bid?\n"))
  auction_list[name] = price
  continue_to_bid = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()


  if continue_to_bid == "yes":
    clear()
  else:
    continue_game = False
    highest_bid = 0
    for bidder in auction_list:
      bid_amount = auction_list[bidder]
      if bid_amount > highest_bid:
        highest_bid = bid_amount
        highest_bidder = bidder


    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")


#another way to loop through the dictionary and find the highest bidder:

# def find_highest_bidder(auction_list):
#   highest_bid = 0
#   for bidder in auction_list:
#     bid_amount = auction_list[bidder] 
#     if bid_amount > highest_bid:
#       highest_bid = bid_amount
#       highest_bidder = bidder
#   print(f"The winnder is {highest_bidder} with a bid of ${highest_bid}.")

