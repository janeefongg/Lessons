import math
import random

def name_to_number(name):
    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    elif name == "scissors":
        number = 4
    else:
        print "error! entry not valid."
    return number

def number_to_name(number):
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
    else:
        print "error! invalid range."
    return name

def rpsls(player_choice):
    player_num = name_to_number(player_choice)
    comp_num = random.randrange(0, 5)
    diff = (player_num - comp_num) % 5
    print " "
    print "Player chooses " + player_choice
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0, 5)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses " + comp_choice
    difference = (comp_number - player_number) % 5
    if difference == 0:
        print "Player and computer tie!"
    elif difference == 1:
        print "Computer wins!"
    elif difference == 2:
        print "Computer wins!"
    elif difference == 3:
        print "Player wins!"
    elif difference == 4:
        print "Player wins!"
    return rpsls

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
