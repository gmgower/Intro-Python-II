from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ["sword", "shield"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ["crossbow"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ["food"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ["leather boots"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ["gold coins"]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# s1 instantiate the Player class
# player = str(input("[n] North [s] South [w] West [e] East [q]Exit\n", room['outside']))
# print(f'Hello, {player.name}')

player = Player("John", room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# directions = {"n":"n_to", "s": "s_to", "e": "e_to", "w": "w_to" }

# s2 player loop
while True: 
    #s3 player chooses north
    # print("Your current location: ", player.current_room.name, "\n")
    # print("Location's Description: ", player.current_room.description, "\n")
    print(player)
    print(player.current_room)

    choice = input("What do you want to do? move, take, or q to quit the game:  ")
    if choice == 'q':
        break
    elif choice == "move":
        move = input("Where do you want to go? n for north, s for south, e for east, w for west, or q to quit the game:  ")
        if move == 'q':
            break
        elif player.current_room.name == room["outside"].name and move == "n":
            player.current_room = room["outside"].n_to
        # print("Foyer", player.current_room)

        elif player.current_room.name == room['foyer'].name and move == "n":
            player.current_room = room['foyer'].n_to
    
        elif player.current_room.name == room['foyer'].name and move == 's':
            player.current_room = room['foyer'].s_to

        elif player.current_room.name == room['foyer'].name and move == 'e':
            player.current_room = room['foyer'].e_to

        elif player.current_room.name == room['overlook'].name and move == 's':
            player.current_room = room['overlook'].s_to

        elif player.current_room.name == room["narrow"].name and move == 'n':
            player.current_room = room['narrow'].n_to
    
        elif player.current_room.name == room["narrow"].name and move == 's':
            player.current_room = room['narrow'].s_to
    
        elif player.current_room.name == room["narrow"].name and move == 'w':
            player.current_room = room['narrow'].w_to    
        else:
            print("Incorrect input or you cannot you go there.")
            continue

    elif choice == 'take':
        item = input(
            f'What do you want to take? {player.current_room.items}> ').lower().strip()
        if item == 'q':
            break
        elif item in player.current_room.items:
            player.take(item)
        else:
            print("Incorrect input.")
            continue
    else:
        print("Incorrect input.")
        continue

    print("Your current location ", player.current_room.name, "\n")
    print("Location's Description: ", player.current_room.description, '\n')        
            

    


    # direction = directions[choice]
    # print(direction)

    # try: 
    #     player.room = getattr(player.room, direction)

    # except AttributeError:
    #     print("Sorry can't pass!")


    
