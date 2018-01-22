""" Anthony Lorenzo Wingo
    CS 103 Introduction to Computation
    Laboratory 11"""
import random
from sys import exit
from collections import Counter

print("____    __    ____  __  .___  ___. .______     ______    __    __  .___________.\n" +
      "\   \  /  \  /   / |  | |   \/   | |   _  \   /  __  \  |  |  |  | |           |\n" +
      " \   \/    \/   /  |  | |  \  /  | |  |_)  | |  |  |  | |  |  |  | `---|  |----`\n" +
      "  \            /   |  | |  |\/|  | |   ___/  |  |  |  | |  |  |  |     |  |\n" +
      "   \    /\    /    |  | |  |  |  | |  |      |  `--'  | |  `--'  |     |  |\n" +
      "    \__/  \__/     |__| |__|  |__| | _|       \______/   \______/      |__|\n")



def roll(n):
    """
    Input: a number of dice to roll
    Output: a list
    :param n: int
    :return: dice: list
    """
    dice = []
    for x in range(n):
        dice.append(random.randint(1,6))
    return dice

def get_dice(dice, x):
    """
    Input: a random list of integers that are the rolled dice
    Output: the value of a die at a given index
    :param dice: a list of the dice
    :param x: an index for where to get the value from
    :return:
    """
    return dice[x-1]

def freight_train(dice):
    """
    Input: a random list of integers that are the rolled dice
    Output: the amount of points to be awarded according to the freight train rule
    :param dice: a list of the dice
    :return: points
    """
    if dice.count(6) == 5:
        winning()
    elif dice.count(1) == 5:
        losing()
    elif dice.count(2) == 5:
         return 200
    elif dice.count(4) == 5:
        return 400
    elif dice.count(5) == 5:
        return 500
    else:
        return 0

def flash(dice):
    """
    Input: a random list of integers that are the rolled dice
    Output: the amount of points to be awarded according to the flash rule
    :param dice: a list of the dice
    :return: points
    """
    if dice.count(1) == 3:
        return 100
    elif dice.count(2) == 3:
        return 20
    elif dice.count(3) == 3:
         return 30
    elif dice.count(4) == 3:
        return 40
    elif dice.count(5) == 3:
        return 50
    elif dice.count(6) == 3:
        return 60
    else:
        return 0

def extra_points(dice):
    """
    Input: a random list of integers that are the rolled dice
    Output: add 10 points for a die that's value is 1 and 5 points for a die that's value is 5
    :param dice: a list of the dice
    :return: points
    """
    points = 0
    for x in range(len(dice)):
        if get_dice(dice, x) == 5:
            points += 5
        if get_dice(dice, x) == 1:
            points += 10
    return points

def three_of_kind(dice):
    """
    Input: a random list of integers that are the rolled dice
    Output: the amount of points to be awarded according to the special die rule
    :param dice: a list of the dice
    :return: points
    """
    if dice[0] == 3:
        if dice.count(1) == 2:
            return 100
        elif dice.count(2) == 2:
            return 20
        elif dice.count(3) == 2:
            return 30
        elif dice.count(4) == 2:
            return 40
        elif dice.count(5) == 2:
            return 50
        elif dice.count(6) == 2:
            return 60
    else:
        return 0

def turn():
    """
    Input: none
    Output: playing the game in the console
    :return:
    """
    total_points = 0
    re_roll = True
    first_dice = roll(5)
    print("It's your turn! \nReady to roll? \nRolling...")
    print("These are all the dice: " + str(first_dice))
    if flash(first_dice) == 100 or flash(first_dice) == 50:
        total_points += freight_train(first_dice) + flash(first_dice) + three_of_kind(first_dice)
    else:
        total_points += freight_train(first_dice) + flash(first_dice) + three_of_kind(first_dice) + extra_points(first_dice)
    print("Your points so far are " + str(total_points))
    while(re_roll == True):
        roll_again = input("Would you like to roll again? [Y/N] ")
        dice = roll(5)
        if roll_again.upper() == "Y":
            re_roll = True
            print("These are all the dice: " + str(dice))
            if flash(dice) == 100 or flash(dice) == 50:
                points = freight_train(dice) + flash(dice) + three_of_kind(dice)
                total_points += freight_train(dice) + flash(dice) + three_of_kind(dice)
                if points == 0:
                    losing()
            else:
                points = freight_train(dice) + flash(dice) + three_of_kind(dice) + extra_points(dice)
                total_points += freight_train(dice) + flash(dice) + three_of_kind(dice) + extra_points(dice)
                if points == 0:
                    losing()
            print("Your points so far are " + str(total_points))
        else:
            re_roll = False
            print("You have concluded your turn.")
            if freight_train(dice) != 0:
                print("You have to re-roll since you you got five of a kind! Pick Y.")
                re_roll = True

def winning():
    """
    Input: none
    Output: tells player they won and exits the game
    :return:
    """
    print("You have won the game!")
    exit(0)

def losing():
    """
    Input: none
    Output: tells player they lost and exits the game
    :return:
    """
    print("You Wimped Out....")
    exit(0)

turn()

