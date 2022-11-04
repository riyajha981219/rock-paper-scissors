import random

def getChoices():
  player_choice = input("Enter a choice (rock/paper/scissors): ")
  computerOptions= ["rock","paper","scissors"]
  computer_choice = random.choice(computerOptions)
  choices= {"player":player_choice, "computer":computer_choice}
  return choices

def checkWin(player, computer):
  print(f"You chose: {player} \nComputer chose: {computer}")
  win= "You win!! :D"
  lose= "You loose! :("
  rockScissors= "Rock smashes Scissors!"
  rockPaper="Paper covers Rock!"
  paperScissors= "Scissors cut Paper!"
  if player == computer:
    return "It's a tie"
  elif player == "rock": 
    if computer == "scissors":
      return f"{rockScissors} {win}"
    else:
      return f"{rockPaper} {lose}"
  elif player == "paper":
    if computer == "rock":
      return f"{rockPaper} {win}"
    else:
      return f"{paperScissors} {lose}"
  elif player == "scissors": 
    if computer == "rock":
      return f"{rockScissors} {lose}"
    else:
      return f"{paperScissors} {win}"

choices = getChoices()
winner=checkWin(choices["player"],choices["computer"])
print(winner)
      
  

