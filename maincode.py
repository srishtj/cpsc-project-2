"""
Author:         Srishti Jaiswal
Date:           25 April
Assignment:     Project 2
Course:         CPSC1051
Lab Section:    2

CODE DESCRIPTION: This is an adventure text-based RPG game. It's set in ancient Persia, like Aladdin. You have to complete a quest the king gives you or you'll be killed. Have fun!
"""
#importing all the different classes 
from classes import Player
from classes import Room
from classes import Map
from classes import Game
import sys

def main():
    game_map = Map() #initialising Map class

    #adding different rooms to the Map and the Room class
    serafiya = Room(
        name='Serafiya',
        description="Serafiya is a bustling city known for its exotic markets and rich culture. Adventurers often gather here to share tales and trade goods.",
        exits=['Zamrud Bay', 'Dunes of Damar', 'Temple of Azar', 'Oasis of Zafira'],
        characters=['Adventurers', 'Merchants']
    )

    zamrud_bay = Room(
        name='Zamrud Bay',
        description="Zamrud Bay is a picturesque bay known for its beautiful waters and thriving fishing community. The fishermen need the Eye of Zarah to resolve their problems.",
        exits=['Serafiya'],
        characters=['Fishermen']
    )

    dunes_of_damar = Room(
        name='Dunes of Damar',
        description="The Dunes of Damar is a vast desert area with treacherous dunes and hidden secrets. You may meet a wandering trader offering unique items.",
        exits=['Serafiya'],
        characters=['Wandering Trader']
    )

    temple_of_azar = Room(
        name='Temple of Azar',
        description="The Temple of Azar is an ancient and mysterious temple that holds many secrets. You may encounter a priest who will test your wisdom.",
        exits=['Serafiya', 'Valley of Shadows'],
        characters=['Priest'],
        condition='riddle_temple'
    )

    oasis_of_zafira = Room(
        name='Oasis of Zafira',
        description="The Oasis of Zafira is a lush and beautiful oasis in the heart of the desert. You may encounter a scribe with stories to share.",
        exits=['Serafiya', 'Ruins of Al-Qamar'],
        characters=['Scribe'],
        condition='riddle_oasis'
    )

    valley_of_shadows = Room(
        name='Valley of Shadows',
        description="The Valley of Shadows is a dark and eerie valley where shadows seem to come alive. You may encounter a shadow assassin.",
        exits=['Serafiya'],
        characters=['Shadow Assassin']
    )

    ruins_of_al_qamar = Room(
        name='Ruins of Al-Qamar',
        description="The Ruins of Al-Qamar are ancient ruins shrouded in mystery and darkness. Explore the ruins to uncover hidden treasures.",
        exits=['Serafiya'],
        characters=[]
    )

    game_map.add_room(serafiya)
    game_map.add_room(zamrud_bay)
    game_map.add_room(dunes_of_damar)
    game_map.add_room(temple_of_azar)
    game_map.add_room(oasis_of_zafira)
    game_map.add_room(valley_of_shadows)
    game_map.add_room(ruins_of_al_qamar)

    game = Game() #initialising the game class

    game.display_welcome_message() #displaying the welcome message to the game

    print("Press any key to continue")
    input()

    print("Welcome to Serafiya!")
    print("A bustling city filled with bazaars, sandstone buildings, and a grand palace at its center. It is a hub of activity where people from all over the land come to trade and socialize.")

    print('Press any key to continue')
    input()

    print("Suddenly, you found yourself surrounded by guards. You're being arrested! What would you like to do? Run (R) or Fight (F)")
    inp1 = input()

    #using while loop to validate player input
    while inp1.lower() not in ['r', 'f']:
        print("Wrong input. Enter R or F.")
        inp1 = input()

    if inp1.lower() == 'r':
        print('You tried to escape through the crowded bazaar and were caught!')

    elif inp1.lower() == 'f':
        print('You tried to fight 5 royal guards without a weapon and were defeated!')

    print("You're walking through the gilded walls of the royal palace for a trial with the Sultan.")
    print("Press any key to continue")
    input()

    print("You're standing in front of the Sultan of Zohar.")
    print('The Sultan will spare your life if you help him resolve the problems of the fishermen of the Zamrud Bay.')
    print('Do you accept? Y|N')
    inp2 = input()

    while inp2.lower() not in ['y', 'n']:
        print('Wrong input. Enter Y or N.')
        inp2 = input()

    if inp2.lower() == 'y':
        print("The Sultan has let you go. Good luck with your mission!")
        print("Press any key to continue")
        input()
        game.play_game(game_map) #starting the main game

    if inp2.lower() == 'n':
        print("You were killed by the Sultan's desert panther for disobedience to the crown!")
        sys.exit(1)

if __name__ == "__main__":
    main()