# Project developed by Emily Suzan Lanzarin in 2022 for the Análise e Desenvolvimento de Sistemas course
# Please, read "README" file for rules on how to play and extra details about the project

# import libraries
import random  # generates random numbers or letters
import time  # for small pauses between rounds and text

# define variables that will be used
B = 'brain'
G = 'gunshot'
S = 'steps'

# defines the lists to be filled
players = []
side = []

# defines the sides of each dice
GreenDice = ('BSBGSB',)
YellowDice = ('GSBGSB',)
RedDice = ('GSGBSG',)

# defines the list of dice to be sorted from the dice holder
cup = ('GreenDice', 'GreenDice', 'GreenDice', 'GreenDice', 'GreenDice', 'GreenDice', 'YellowDice', 'YellowDice',
       'YellowDice', 'YellowDice', 'RedDice', 'RedDice', 'RedDice')

rounds = 0

# greetings for the players
print("WELCOME TO ZOMBIE DICE!!!")
time.sleep(1)

print("ARE YOU READY FOR THE MOST THRILLING ADVENTURE OF ALL?")
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

    for i in range(nPlayers):
        # identify and store the name of the players inside the list 'players'
        name = str(input("Please, type the name of the zombies:"))
        players.append(name)

print("STARTING GAME...")
time.sleep(1)

i = 0
rounds = 1
brains = 0
steps = 0
hearts = 3

while True:
    for j in range(0, nPlayers):
        print("It's your turn,", players[i])
        time.sleep(1)

        # randomly selects 3 dice from the dice holder
        diceChoice = random.sample(cup, 3)
        print("Your dice are:", diceChoice)
        time.sleep(1)

        # identifies the items in the list and defines what to do w/ them
        for c in diceChoice:
            if c == 'GreenDice':
                side = random.choice('BSBGSB')
            elif c == 'YellowDice':
                side = random.choice('GSBGSB')
            elif c == 'RedDice':
                side = random.choice('GSGBSG')

# prints the selected sides for the players
            print("Your sides are:", side)
            time.sleep(1)

# counts the players' points
            while side == 'B':
                brains = brains + 1
                break
            while side == 'G':
                hearts = hearts - 1
                break
            while side == 'S':
                steps = steps + 1
                break

# prints what happened in the current round
        print("You've eaten", brains, "brains!")
        time.sleep(1)

        print(steps, "of your victims ran away...")
        time.sleep(1)

        print("You still have", hearts, "hearts!")
        time.sleep(1)

        keepPlay = input("Do you want to keep playing? [y/n]")
        while keepPlay == 'n' or 'N':
            # prints the players' score in case they don't keep playing the current round
            print(players[i], "SCORE:")
            time.sleep(1)

            print("BRAINS -----", brains)
            time.sleep(1)

            print("HEARTS -----", hearts)
            time.sleep(1)

            break

    # game continues on to the next player but doesn't start their round
    # diceChoice = []
    # currentPlayer = currentPlayer + 1
    # brains = 0
    # hearts = 3
    # steps = 0

        i = i+1

    break
