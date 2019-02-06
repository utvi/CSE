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
                       "the south is Mr. Wiebe's room",
        'PATHS': {
            'SOUTH': "R19A",
            'EAST': "ART_BUILDING",
            'WEST': "HALLWAY"
        }
    },
    'ART_BUILDING': {
        'NAME': "Art Building",
        'DESCRIPTION': "There are paintings covering the walls."
                       "To the west is The Parking Lot",
        'PATHS': {
            'WEST': "PARKING_LOT"
        }
    },
    'HALLWAY': {
        'NAME': "Main Hallway",
        'DESCRIPTION': "This is the main hallway."
                       "The Parking Lot is to the east,"
                       "the quad is to the south, the gym is to the west"
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
        'DESCRIPTION': "This is the library. Books cover the walls"
                       "and a little dog with glasses softly barks at you"
                       "when you make too much noise. There's a path to"
                       "the south back to the Main Hallway and a suspicious"
                       "door to the north.",
        'PATHS': {
            'SOUTH': "HALLWAY",
            'NORTH': "SUSPICIOUS_ROOM"
        }
    },
    'SUSPICIOUS_ROOM': {}

}

# Other variables
current_node = world_map['R19A']
directions = {'NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN'}
playing = True

# Controller
while playing:
    print(current_node["NAME"])
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
