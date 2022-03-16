# Project developed by Emily Suzan Lanzarin in 2022 for the Análise e Desenvolvimento de Sistemas course
# Please, read "README" file for rules on how to play and extra details about the project

# import libraries
import random  # generates random numbers or letters
import time  # for small pauses between rounds and text

# define variables that will be used
rounds = 0
brains = 0
hearts = 3
steps = 0
B = 'brain'
G = 'gunshot'
S = 'steps'

# defines the lists to be filled
players = []
diceChoice = []
side = []

# defines the sides of each dice
GreenDice = 'BSBGSB'
YellowDice = 'GSBGSB'
RedDice = 'GSGBSG'

# defines the list of dice to be sorted from the cup/tube
cup = ['GreenDice', 'GreenDice', 'GreenDice', 'GreenDice', 'GreenDice', 'GreenDice', 'YellowDice', 'YellowDice',
       'YellowDice', 'YellowDice', 'RedDice', 'RedDice', 'RedDice']

# greetings for the players
print("WELCOME, ZOMBIES! ARE YOU READY FOR THE MOST THRILLING ADVENTURE OF ALL?")  # shows this message
time.sleep(1)  # waits 1 sec for the next message

# creates variable for number of players
nPlayers = int(input("How many zombies will be joining us today?"))

# conditions for the game to start
if nPlayers < 2:
    print("We need at least 2 players to continue!")

elif nPlayers > 8:
    print("Sorry, too many zombies in this game! We accept up to 8 players:")

# nPlayers >= 2 or nPlayers <= 8
else:
    print("Alright! Let's meet our players!")
    time.sleep(1)

# identify and store the name of the players
    name = str(input("Please, press ENTER and type the names of the zombies separated by ENTER:"))

# stores players' names in the list 'players'
    for i in range(nPlayers):
        players.append(input())
        i += 1

print("STARTING GAME...")
time.sleep(1)

roundPlayer = players[0]

print("It's your turn", roundPlayer)
time.sleep(1)

# randomly selects 3 dice from the dice holder
diceChoice = random.sample(cup, 3)
print("Your dice are:", diceChoice)
time.sleep(1)

#
for c in diceChoice:
    if c == 'GreenDice':
        side = random.choice('BSBGSB')
    elif c == 'YellowDice':
        side = random.choice('GSBGSB')
    elif c == 'RedDice':
        side = random.choice('GSGBSG')

    print("Your sides are:", side)
    time.sleep(1)

    while side == 'B':
        brains = brains + 1
        break
    while side == 'G':
        hearts = hearts - 1
        break
    while side == 'S':
        steps = steps + 1
        break

print("You've eaten:", brains, "brains!")
time.sleep(1)

print(steps, "of your victims ran away...")
time.sleep(1)

print("You still have", hearts, "hearts!")
time.sleep(1)

print("ROUND 1 SCORE:")
time.sleep(1)

print("BRAINS:", brains)
time.sleep(1)

print("HEARTS:", hearts)
time.sleep(1)
