from weapon import Weapon
from weapon_list import weapon_list

wep_range = ""
complexity = ""
speed = ""
mobility = ""
utility = ""

count = 0

def program_start():
    response = input("""
    Welcome to the Monster Hunter Weapon Finder! THE place to get help deciding on a weapon to use in Monster Hunter. Would you like to get started?
    (yes/no)
    """).lower()

    if response == "yes":
        ask_range()
    else:
        exit_program()

def ask_range():
    response = input(""" 
    Do you want a long range or short range weapon?
    1 - Long Range  2 - Short Range
    """)
    
    if response == '1':
        wep_range = "Long"
        ask_complexity()

def exit_program():
    print("Happy Hunting!")
    exit()

def ask_complexity():
    pass

program_start()