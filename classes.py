import json 
import os
from random import randint
import sys

class Player: #player class to manage player attributes
    def __init__(self):
        self.health = 100 
        self.inventory = []

    def add_to_inventory(self, item): #adds item to player's inventory
        self.inventory.append(item)
        print(f"{item} has been added to your inventory.")


    def has_item(self, item): #checks if player has a certain item in inventory
        return item in self.inventory

    def reduce_health(self, amount): #redecues player health in combat and checks if they're dead 
        self.health -= amount
        if self.health <= 0:
            print("You have died!")
            sys.exit(1)

class Room: #room class to manange different places on the map
    def __init__(self, name, description, exits, characters, condition=None):
        self.name = name
        self.description = description
        self.exits = exits
        self.characters = characters
        self.condition = condition

    def __str__(self): #returns the details of a room as a string
        return f"Welcome to {self.name}\n{self.description}\n"

    def handle_conditions(self, player): #handles a specific condition to enter a room for the player
        if self.condition == 'coin':
            print("To enter the Oasis of Zafira, you need a merchant to help you make the travel.")
            if not player.has_item('coin'):
                print("You don't have any money. The merchant refuses to take you.")
                return False
        return True

class Map: #map class to keep track of the different places and how they're connected
    def __init__(self):
        self.rooms = {}

    def add_room(self, room): #adds new room to map
        self.rooms[room.name.lower()] = room

    def get_room(self, room_name): #gets info about a specific room
        return self.rooms.get(room_name.lower())

    def list_rooms(self): #lists all the rooms in a map
        return list(self.rooms.keys())

class Game:
    def __init__(self):
        self.player = Player()
        self.current_room = None

    def display_welcome_message(self): #displaying the welcome game message
        print("""
Welcome to the Seas of Sand!

You've arrived in the majestic Kingdom of Zohar,
a land of ancient wonders and vibrant culture.

Embark on a journey filled with mystery and adventure,
as you explore exotic bazaars, majestic temples, and hidden ruins.

Your path is set; embrace the challenge and forge your destiny
in the heart of this enchanting desert realm.

Prepare to start a new life and discover your true purpose.
        """)

    def play_game(self, game_map): #playing game with the map 
        self.current_room = game_map.get_room('serafiya') #setting the starting point to serafiya
        while True:
            #asking player about their next move
            print("\nWhere would you like to go next? (Exits: " + ', '.join(self.current_room.exits) + ")")
            print("Please type in the name of the place you'd like to go to next:")
            print("Type 'save' to save the game, 'load' to load the game, or 'q' to quit the game.")
            choice = input().lower().strip()

            #if loop to handle player choices if they decide to save the game, load a saved game or quit
            if choice == 'save':
                self.save_game(game_map)
                continue
            elif choice == 'load':
                self.load_game(game_map)
                continue
            elif choice == 'q':
                print("Quitting the game. Goodbye!")
                sys.exit(1)

            #checking player input in a while loop to make sure its a valid input
            while choice.lower() not in [exit.lower() for exit in self.current_room.exits]:
                print("Invalid exit. Please choose a valid exit.")
                print(f"Available exits: {', '.join(self.current_room.exits)}")
                choice = input().lower().strip()

            #printing out room instructions and changing current room to the new room
            next_room = game_map.get_room(choice)
            self.current_room = next_room
            self.handle_room(self.current_room)



    def save_game(self, game_map): #saves current game data
        game_data = {
        "current_room": self.current_room.name,
        "player": {
            "health": self.player.health,
            "inventory": self.player.inventory
            }
        }

        #saving the game data to a json file
        with open("save_game.json", "w") as file:
            json.dump(game_data, file)
            print("Game saved successfully.")
            sys.exit(1)

    def load_game(self, game_map): #loading game data from saved json file
        if os.path.exists("save_game.json"): 
            with open("save_game.json", "r") as file:
                game_data = json.load(file)
                self.current_room = game_map.get_room(game_data["current_room"])
                self.player.health = game_data["player"]["health"]
                self.player.inventory = game_data["player"]["inventory"]
                print("Game loaded successfully.")
        else:
            print("No save game file found.")

    
    def handle_room(self, room): #method to assign a different method depending on the room the player picks
        if room.name == 'Zamrud Bay':
            self.handle_zamrud_bay()
        elif room.name == 'Dunes of Damar':
            self.handle_dunes_of_damar()
        elif room.name == 'Temple of Azar':
            self.handle_temple_of_azar()
        elif room.name == 'Valley of Shadows':
            self.handle_valley_of_shadows()
        elif room.name == 'Oasis of Zafira':
            self.handle_oasis_of_zafira()
        elif room.name == 'Ruins of Al-Qamar':
            self.handle_ruins_of_al_qamar()

    def handle_zamrud_bay(self): #room method for zamrud bay
        
        if not self.player.has_item("Emerald Eye of Zarah"):
            print("\nYou have arrived at Zamrud Bay, a picturesque bay known for its beautiful waters and thriving fishing community.")
            print("press any key to continue")
            input()
            print("The fishermen need the Eye of Zarah to resolve their conflict.")
            print("The fishermen suggest you find the Eye of Zarah and bring it back to them.")

        #condition to win the game
        if self.player.has_item('Emerald Eye of Zarah'):
            print("The fishermen thank you for getting the Eye back to them!")
            print("You've won the game!")
            print("press any key")
            input()
            sys.exit(1)
    
    def handle_dunes_of_damar(self): #room method for dunes of damar
        print("\nYou have arrived at the Dunes of Damar, a vast desert area with treacherous dunes and hidden secrets.")
        print("You meet a wandering trader named Kaveh.")
        print("press any key to conitnue")
        input()
        print("Kaveh offers you three items: a magic carpet made of rich silk and velvet, a dagger with rubies on the hilt, and a crown made with the finest gold and amethysts.")
        print("You can only choose one item.")
        
        #prompting a choice between the different items for the player to take
        choice = input("\nWhich item would you like to take? (magic carpet, dagger, crown): ").strip().lower()
        while choice not in ['magic carpet', 'dagger', 'crown']:
            print("Invalid choice. Please choose 'magic carpet', 'dagger', or 'crown'.")
            choice = input("Which item would you like to take? (magic carpet, dagger, crown): ").strip().lower()

        if choice == 'magic carpet':
            print("You have taken the magic carpet.")
        elif choice == 'dagger':
            self.player.add_to_inventory('dagger')
        elif choice == 'crown':
            print("The crown is beautiful but cursed. It kills you instantly. You have died.")
            sys.exit(1)


    def handle_temple_of_azar(self): #room method for temple of azar
        print("\nYou have arrived at the Temple of Azar, an ancient and mysterious temple that holds many secrets.")
        print("You meet a priest named Azar.")
        print("press any key to continue")
        input()
        print("To enter the temple, you must answer a riddle.")
        print("Riddle: What gets wetter the more it dries?")
        riddle_answer = input("Your answer: ").strip().lower()
        
        #checking to see if the answer to the riddle is correct
        if riddle_answer != 'towel':
            print("Incorrect answer. You cannot enter the temple.")
            print("You were used as a sacrifice to the Gods by the priest instead.")
            sys.exit(1)

        print("Correct! You may enter the temple.")
        print("The priest Azar gives you a coin as a token of your intelligence.")
        self.player.add_to_inventory('coin')


    def handle_valley_of_shadows(self): #room method for valley of shadows
        print("\nYou have arrived at the Valley of Shadows, a dark and eerie valley where shadows seem to come alive.")
        print("You encounter a shadow assassin named Omar.")
        print("You engage in combat with the shadow assassin.")
        print("Press any key to continue")
        input()

        if not self.player.has_item('dagger'):
            print("You didn't have a weapon to fight the assassin, so you died instantly.")
            sys.exit(1)

        #using randint to randomise damage during combat
        player_damage = randint(20, 50)
        assassin_damage = randint(10, 20)
        
        #reduing player's health based on the damage inflicted
        self.player.reduce_health(assassin_damage)
        print(f"You dealt {player_damage} damage to the shadow assassin.")
        print(f"The shadow assassin dealt {assassin_damage} damage to you.")

        if self.player.health > 0:
            print("You defeated the shadow assassin!")
            print("You meet the faction leader of the Valley, and they reward you with a sapphire talisman.")
            self.player.add_to_inventory('sapphire talisman')


    def handle_oasis_of_zafira(self): #room method to handle oasis of zafira

        print("\nYou meet a merchant who offers to take you across the lake in a boat to reach Zafira.")
        print("The merchant will only take you across if you are able to ply him.")
        print("press any key to continue")
        input()

        #checking player's inventory to see if they have a desired item
        if not self.player.has_item('coin'):
            print("You don't have any money. The merchant refuses to take you across the lake.")
            return
        
        if self.player.has_item('coin'):
            print("The merchant accepts your coin and takes you across the lake.")
            print("You have arrived at the Oasis of Zafira, a lush and beautiful oasis in the heart of the desert.")


    def handle_ruins_of_al_qamar(self): #room method to handle ruins fo al-qamar
        print("To enter the ruins, you must solve a riddle.")
        print("Riddle: What is so fragile that saying its name breaks it?")
        riddle_answer = input("Your answer: ").strip().lower()

        if riddle_answer != 'silence':
            print("Incorrect answer. You cannot enter the ruins.")
            print("The scholars were offended by the lack of intelligence and killed you!")
            sys.exit(1)
        
        #checking player's answer to riddle
        if riddle_answer == 'silence':
            print("Correct! You may enter the ruins.")
            print("You have arrived at the Ruins of Al-Qamar, ancient ruins shrouded in mysterious curses and darkness.")
            print("Press any key to continue")
            input()

            #checking players inventory to see if they have the item needed
            if not self.player.has_item('sapphire talisman'):
                print("You don't have protection against the curses. You were cursed by the scholars and died instantly.")
                sys.exit(1)

            print("You enter the ruins and meet the cursed society of scholars.")
            print("press any key to continue")
            input()
            print("The scholars offer you the Eye of Zarah in exchange for the sapphire talisman.")

            if self.player.has_item('sapphire talisman'):
                print("You give the sapphire talisman to the scholars.")
                self.player.inventory.remove('sapphire talisman')
                print("The scholars reward you with the Eye of Zarah.")
                self.player.add_to_inventory('Emerald Eye of Zarah')