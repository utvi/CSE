class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None, up=None, down=None, description=""):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.description = description


# Option 1
R19A = Room("R19A")
art_building = Room("Art Building")
hallway = Room("Hallway")
parking_lot = Room('The Parking Lot', None, R19A, art_building, hallway, None, None)

R19A.north = parking_lot
parking_lot.south = R19A

# Option 2
# Put Them Away
# R19A = Room("R19A", 'parking_lot')

art_building = Room('Art Building', None, parking_lot)

art_building.west = parking_lot
library = Room("Library")
quad = Room("Quad")
gym = Room("Gym")
hallway = Room('The Hallway', library, quad, parking_lot, gym, None, None,)

hallway.north = library
hallway.south = quad
hallway.east = parking_lot
hallway.east = gym
