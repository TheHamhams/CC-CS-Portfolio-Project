from weapon import Weapon
from weapon_list import weapon_list

wep_range = ""
complexity = ""
speed = ""
mobility = ""
utility = ""


def program_start():
    response = input("""
    Welcome to the Monster Hunter Weapon Finder! THE place to get help deciding on a weapon to use in Monster Hunter. Would you like to get started?
    (yes/no)
    """).lower()

    if response == "yes":
        ask_range()
    elif response == "no":
        exit_program()
    else:
        print("Please try again")
        program_start()

def ask_range():
    global wep_range
    response = input(""" 
    Do you want a long range or short range weapon?
    1 - Long Range  2 - Short Range
    """)
    
    if response == '1':
        wep_range = "Long"
        ask_complexity()

    elif response == '2':
        wep_range = "Short"
        ask_complexity()
    else:
        print("Please try again")
        ask_range()

def ask_complexity():
    global complexity
    response = input(""" 
    Do you want a simpler or a more complex weapon?
    1 - Simple  2 - Complex
    """)
    
    if response == '1':
        complexity= "Simple"
        ask_speed()

    elif response == '2':
        complexity = "Complex"
        ask_speed()
    else:
        print("Please try again")
        ask_complexity()

def ask_speed():
    global speed
    response = input(""" 
    Do you want a fast or hard hitting weapon?
    1 - Fast  2 - Hard Hitting
    """)
    
    if response == '1':
        speed = "Fast"
        ask_mobility()

    elif response == '2':
        speed = "Hard Hitting"
        ask_mobility()
    else:
        print("Please try again")
        ask_speed()

def ask_mobility():
    global mobility
    response = input(""" 
    What type of mobility do you want?
    1 - Mobile  2 - Simple Movement 3 - Defensive
    """)
    
    if response == '1':
        mobility = "Mobile"
        ask_utility()

    elif response == '2':
        mobility = "Simple Movement"
        ask_utility()

    elif response == '3':
        mobility = "Defensive"

    else:
        print("Please try again")
        ask_mobility()

def ask_utility():
    global utility
    response = input(""" 
    What would you like your weapon to focus on?
    1 - Damage  2 - Utility
    """)
    
    if response == '1':
        utility = "Damage"
        results()

    elif response == '2':
        utility = "Utility"
        results()
    else:
        print("Please try again")
        ask_utility()

def results():
    result_array = [wep_range, complexity, speed, mobility, utility]
    result = []
    count_max = 0
    i = 0

    for weapon in weapon_list:
        while i < len(weapon.array):
            if weapon.array[i] == result_array[i]:
                weapon.match_count += 1
            i += 1
        i = 0
    
    for weapon in weapon_list:
        if weapon.match_count > count_max:
            count_max = weapon.match_count
    
    for weapon in weapon_list:
        if weapon.match_count == count_max:
            result.append(weapon)


    print("Your ideal weapons are:")
    for weapon in result:
        weapon.display()
    
    exit_program()

def exit_program():
    print("Happy Hunting!")
    exit()

program_start()