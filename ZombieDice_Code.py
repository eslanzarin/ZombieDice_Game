"""
Project developed by Emily Suzan Lanzarin in 2022 for the Análise e Desenvolvimento de Sistemas course
Please, read "README" file for rules on how to play and extra details about the project
"""

# Import libraries
from random import shuffle, choice
from collections import namedtuple
import time


def menu():
    """
    Function will explain the rules of the game before it begins
    :return: Nothing
    """
    print("\t**** WELCOME TO ZOMBIE DICE ****\n")
    print(f"\tHOW TO PLAY:")
    print(f"\tAT EACH ROUND, EACH PLAYER WILL THROW 3 DICE FROM THE CUP.")
    print(f"\tTO WIN, YOU'VE GOT TO HAVE 13 EATEN BRAINS IN YOUR SCORE!")
    print(f"\tBUT BE CAREFUL! IF YOU GET 3 GUNSHOTS IN A ROUND, YOU'LL LOSE ALL YOUR EATEN BRAINS!!!\n")


print(f'ARE YOU READY FOR THE MOST THRILLING ADVENTURE OF ALL?\n')
time.sleep(1)
start = menu()


def add_players():
    """
    Function to check and validate the numbers of players for the game to start
    :return: variable containing the list with names/scores for each player
    """
    players = []

    # Check the condition for the game to start (players > 2)
    while True:
        try:
            n_players = int(input(f"\tTYPE THE NUMBER OF PLAYERS: "))
            time.sleep(0.5)
            if n_players > 1:
                break
            else:
                print(f"\tYOU NEED AT LEAST 2 PLAYERS TO PLAY!")
                time.sleep(0.5)
        except ValueError:
            print(f"\tTYPE AN INTEGER NUMBER!")
            time.sleep(0.5)

    # Store the name of the players in a list
    for i in range(n_players):
        name = input(f"\tTYPE ZOMBIE'S {i+1} NAME: ").upper()
        time.sleep(0.5)
        player = {'name': name, 'score': 0}
        players.append(player)

    return players


def create_dice():
    """
    Creates the dice list and each side
    :return: variable containing the dice list
    """
    # named tuple for each die color
    Die = namedtuple("Die", ['color', 'side'])
    green_die = Die('green', ['brain', 'brain', 'brain', 'step', 'step', 'gunshot'])
    red_die = Die('red', ['brain', 'step', 'step', 'gunshot', 'gunshot', 'gunshot'])
    yellow_die = Die('yellow', ['brain', 'brain', 'step', 'step', 'gunshot', 'gunshot'])

    # Add each tuple in a specified list that can be modified
    dice_list = []
    for _ in range(6):
        dice_list.append(green_die)
    for _ in range(3):
        dice_list.append(red_die)
    for _ in range(4):
        dice_list.append(yellow_die)

    shuffle(dice_list)
    return dice_list


def turn(player):
    """
    Creates a variable for the score, which has points for brains and gunshots (added at each round for each player).
    Creates a variable for removing dice from the list at each round to count as the dice being held in the players
    hand
    :param player: variable to call
    :return: Nothing
    """
    print(f"\n\tIT'S PLAYER {player['name']}'S TURN!")
    time.sleep(0.5)

    dice_list = create_dice()
    score_turn = {'brains': 0, 'hearts': 3, 'steps': 0}
    holding_dice = []

    while True:
        while len(holding_dice) < 3:
            holding_dice.append(dice_list.pop())

        n = 1

        for die in reversed(holding_dice):
            time.sleep(0.5)
            print(f"\tTHROWING DICE {n}")
            n += 1

            color = die.color
            shuffle(die.side)
            sorted_side = choice(die.side)

            print(f"\tCOLOR: {color}\n\tSIDE: {sorted_side}\n")

            if sorted_side == 'brain':
                score_turn['brains'] += 1
                dice_list.append(holding_dice.pop(holding_dice.index(die)))
            elif sorted_side == 'gunshot':
                score_turn['hearts'] -= 1
                dice_list.append(holding_dice.pop(holding_dice.index(die)))
            elif sorted_side == 'step':
                score_turn['steps'] += 1
                dice_list.append(holding_dice.pop(holding_dice.index(die)))
            shuffle(dice_list)

        print(f"\t**** SCORE ****")
        print(f"\n\tBRAINS: {score_turn['brains']}\n\tHEARTS: {score_turn['hearts']}\n\tSTEPS: {score_turn['steps']}")
        if score_turn['hearts'] > 0 and score_turn['steps'] > 0:
            if input("\n\tWould you like to keep playing? (y/n): ").upper() != 'Y':
                print(f"\n\tYou've got {score_turn['brains']} brains.")
                player['score'] += score_turn['brains']
                break
        else:
            print(f"\n\tYou've got shot many times and lost all of your hearts! Next player...")
            break


def score_points(players):
    """
    Function will score the points for each player in the game
    :param players: variable to call
    :return: Nothing
    """
    print("\n\t*** ROUND SCORE ***")
    for player in players:
        print(f"\n\t{player['name']}: {player['score']} points")


players = add_players()


# Defining the conditions for the game to be over
game_over = False
while not game_over:
    for player in players:
        turn(player)
        if player['score'] >= 13:
            winner = player['name']
            game_over = True
    if not game_over:
        score_points(players)
    else:
        print(f"\n\tTHE WINNER IS: {winner}.")
        score_points(players)
