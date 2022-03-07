# Project developed by Emily Suzan Lanzarin in 2022 for the Análise e Desenvolvimento de Sistemas course
# Please, read "README" file for rules on how to play and extra details about the project

# import libraries

import random  # generates random numbers or letters
import time  # for small pauses between rounds and text

# define variables (this is still something I've got to think about carefully)

rounds = 0
players = []

# code sorts 3 values from the list, then sorts the specific letter from each item

cup = ['BSBGSB','BSBGSB','BSBGSB','BSBGSB','BSBGSB','BSBGSB','GSBGSB','GSBGSB','GSBGSB','GSBGSB','GSGBSG','GSGBSG','GSGBSG']

GreenDice = "BSBGSB"
YellowDice = "GSBGSB"
RedDice = "GSGBSG"

# greetings for the players
print("WELCOME, ZOMBIES! ARE YOU READY FOR THE MOST THRILLING ADVENTURE OF ALL?")  # shows this message
time.sleep(1)  # waits 1 sec for the next message

nPlayers = int(input("How many zombies will be joining us today?"))

if nPlayers < 2:
    print("We need at least 2 players to continue!")

elif nPlayers > 8:
    print("Sorry, too many zombies in this game! We accept up to 8 players:")

else:
    print("Alright! Let's start!")

    name = str(input("Please, press ENTER and type the names of the zombies separated by ENTER:"))  # identify and store the name of the players (how to make pressing enter not needed?

    i = 0

    for i in range(nPlayers):
        players.append(input())  # stores players' names in a list
        i += 1
    time.sleep(0.5)

print("ALRIGHT! Now let's start!")
time.sleep(0.5)

print("It's your turn", (players[0])) # random library chooses a player
time.sleep(0.5)

dice = random.sample(cup, 3) #trying to make it choose 3 dice and return the value of their faces
for DiceFace in dice:
    for x in DiceFace:


print(DiceFace)

# toss the dice from the cup