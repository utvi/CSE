world_map = {
    'R19A': {
        'NAME': "Wiebe's Classroom",
        'DESCRIPTION': "This is the classroom that you are in right "
                       "now. It has two exits to the north side.",
        'PATHS': {
            'NORTH': "PARKING_LOT"
        }
    },
    'PARKING_LOT': {
        'NAME': "The Parking Lot",
        'DESCRIPTION': "There are cars parked here. To "
                       "the south is Mr. Wiebe's room. To the west is the "
                       "Main hallway and to the east is the art building.",
        'PATHS': {
            'SOUTH': "R19A",
            'EAST': "ART_BUILDING",
            'WEST': "HALLWAY"
        }
    },
    'ART_BUILDING': {
        'NAME': "Art Building",
        'DESCRIPTION': "There are paintings covering the walls. "
                       "To the west is The Parking Lot",
        'PATHS': {
            'WEST': "PARKING_LOT"
        }
    },
    'HALLWAY': {
        'NAME': "Main Hallway",
        'DESCRIPTION': "This is the main hallway."
                       "The Parking Lot is to the east, "
                       "the quad is to the south, the gym is to the west "
                       "and the library is to the north.",
        'PATHS': {
            'NORTH': "LIBRARY",
            'EAST': "PARKING_LOT",
            'SOUTH': "QUAD",
            'WEST': "GYM",
        }
    },
    'LIBRARY': {
        'NAME': "The Library",
        'DESCRIPTION': "This is the library. Books cover the walls. "
                       "There's a path to the south back to the Main "
                       "Hallway and a suspicious door to the north.",
        'PATHS': {
            'SOUTH': "HALLWAY",
            'NORTH': "SUSPICIOUS_ROOM"
        }
    },
    'SUSPICIOUS_ROOM': {
        'NAME': "Suspicious Room",
        'DESCRIPTION': "You are in a small brown room with a "
                       "hatch up on the roof. You wonder how anybody "
                       "could get up there.",
        'PATHS': {
            'UP': "KING_ROOM",
            'SOUTH': "LIBRARY"
        }
    },
    'KING_ROOM': {
        'NAME': "King Wiebe's Secret Room",
        'DESCRIPTION': "You are in a large and lavish room, "
                       "Before you is King Wiebe, the all mighty immortal leader "
                       "and his henchman Eggman.",
        'PATHS': {
            'DOWN': "SUSPICIOUS_ROOM"
        }
    },
    'GYM': {
        'NAME': "Gym",
        'DESCRIPTION': "You are in the gym. Most of the ceiling lights are off "
                       "besides a couple of them. A basketball is on the floor and only one "
                       "basket is down. To the east is the main hall and to the south "
                       "is the west building.",
        'PATHS': {
            'EAST': "HALLWAY",
            'SOUTH': "WEST_BUILDING"
        }
    },
    'WEST_BUILDING': {
        'NAME': "The West Building",
        'DESCRIPTION': "The west building is filled with classrooms. There's one unlocked "
                       "bathroom to the west.",
        'PATHS': {
            'WEST': "Bathroom"
        }
    }

}

# Other variables
current_node = world_map['R19A']
directions = {'NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN'}
playing = True

# Controller
while playing:
    print(current_node["NAME"])
    print(current_node["DESCRIPTION"])
    command = input(">_")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.upper() in directions:
        try:
            room_name = current_node['PATHS'][command.upper()]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go that way.")
    else:
        print("Command not recognized.")
