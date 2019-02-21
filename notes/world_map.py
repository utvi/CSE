class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None, description=""):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.description = description


# Option 1
R19A = Room("R19A")
parking_lot = Room('The Parking Lot', None, R19A,)

R19A.north = parking_lot
parking_lot.south = R19A

# Option 2
# Put Them Away
# R19A = Room("R19A", 'parking_lot')

art_building = Room('Art Building', None, parking_lot)

art_building.west = parking_lot

hallway = Room('The Hallway', None, parking_lot)

hallway.east = parking_lot
