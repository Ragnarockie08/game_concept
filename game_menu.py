import os
import sys
from text import welcom
import sys, tty, termios

def print_menu():
    while True:
        os.system('clear')
        print(welcom)
        print('''
                Press:
                'S' to start the game
                'I' to se information about the game
                'P' to see your mission
                'X' to quit the game
            ''')
        choice = print_choices()
        if choice == "s":
            break


def getch():

    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def print_choices():

    choice = getch()
    if choice == 'p':
        os.system('clear')
        show_plot()
        input("Press Enter to continue")
    elif choice == 'i':
        os.system('clear')
        print_info()
        input("Press Enter to continue")
    elif choice == 'x':
        print("Thanks for playing!")
        sys.exit()
    elif choice == 's':
        return choice


def show_plot():

    print('''

                                    .___  ___.      ___           _______.     _______.    _______  _______  _______  _______   ______ .___________.
                                    |   \/   |     /   \         /       |    /       |   |   ____||   ____||   ____||   ____| /      ||           |
                                    |  \  /  |    /  ^  \       |   (----`   |   (----`   |  |__   |  |__   |  |__   |  |__   |  ,----'`---|  |----`
                                    |  |\/|  |   /  /_\  \       \   \        \   \       |   __|  |   __|  |   __|  |   __|  |  |         |  |
                                    |  |  |  |  /  _____  \  .----)   |   .----)   |      |  |____ |  |     |  |     |  |____ |  `----.    |  |
                                    |__|  |__| /__/     \__\ |_______/    |_______/       |_______||__|     |__|     |_______| \______|    |__|



                              Your main mission is defeating the Space pirates boss, but first you have to collect elements necesarry to build your weapon.
                              Elements are arranged around the maps. You will be travaling in your spaceship which will lose fuel so look out and collect
                              fuel also! When you will have enough resources the weapon will apear in your inventory and the boss fight will be able!
                                                                           Good luck and have fun !


    ''')

def print_info():

    print('''
                                                                                    W - move up
                                                                                    S - move down
                                                                                    A - move left
                                                                                    D - move right
                                                                                 Elements to collect:
                                                                                    ⛰️ - Platinum
                                                                                    + - Iridium
                                                                                    & - Palladium
                                                                                    % - Fuel
                                                                           ----------------------------------
                                                                            TO COLLECT ELEMENTS MOVE ON THEM
                                                                                    X - quit the game

          ''')
