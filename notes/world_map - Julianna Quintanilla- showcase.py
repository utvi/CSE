class Item(object):
    def __init__(self, name):
        self.name = name


class Weapon(object):
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


class Armor(object):
    def __init__(self, name, protection):
        self.name = name
        self.protection = protection


class Character(object):
    def __init__(self, name, health, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
            print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)


class Player(object):
    def __init__(self, starting_location):
        self.health = 100
        self.current_location = starting_location
        self.inventory = []
        self.damage = 10

    def move(self, new_location):
        """This method moves a character to anew location

        :param new_location: The variable containing a room object
        """
        self.current_location = new_location


class Room(object):
    def __init__(self, name, north=None, south=None, east=None, west=None,
                 up=None, down=None, description="", character=None, items=[]):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.description = description
        self.character = character
        self.items = items

# Items


pan = Weapon("Frying Pan", 5)
sword1 = Weapon("Sword", 15)
sword2 = Weapon("Orc Sword", 5)
sword3 = Weapon("Iron Sword", 10)
sword4 = Weapon("Diamond Sword", 25)
bow1 = Weapon("Wood Bow", 15)
bow2 = Weapon("Diamond Bow", 25)
battle_axe1 = Weapon("Iron Battle Axe", 20)
battle_axe2 = Weapon("Diamond Battle Axe", 30)
battle_axe3 = Weapon("Legendary Battle Axe", 40)
taser_gun1 = Weapon("Taser Gun", 90)
spray1 = Weapon("Pepper Spray", 20)
spray2 = Weapon("Anti-Weeb Spray", 50)
spray3 = Weapon("Anti-Wiebe Spray", 300)
special1 = Weapon("Moth Claws", 900)
special2 = Weapon("Hee Hee", 10)
dog_treat1 = Item("Green Treat")
dog_treat2 = Item("Brown Treat")
dog_toy1 = Item("Hard Dog Toy")
dog_toy2 = Item("Soft Dog Toy")
pillow1 = Item("Liam Neeson Pillow Body Pillow")
pillow2 = Item("Danny DeVito Body Pillow")
pillow3 = Item("Bob Ross Pillow Body Pillow")
armor1 = Armor("Leather Armor", 30)
armor2 = Armor("Iron Armor", 50)
armor3 = Armor("Diamond Armor", 80)
armor4 = Armor("Legendary Armor", 100)
armor5 = Armor("Wiebe Armor", 150)
armor6 = Armor("Egg Shell", 25)
# characters
npc1 = Character("Juli", 9001, battle_axe3, armor4)
npc2 = Character("Mothman", 900, special1, None)
npc3 = Character("Michael Jackson", 40, special2, None)
npc4 = Character("King Wiebe", 600, taser_gun1, armor5)
npc5 = Character("Eggman", 100, sword1, armor6)
# rooms
# Put Them Away
# R19A = Room("R19A", 'parking_lot')
R19A = Room("R19A", 'Parking Lot', None, None, None, None, None,
            "This is R19A, Mr.Wiebe's classroom. Despite it being time for class, "
            "nobody is in here including Mr.Wiebe. You wonder where everybody could be. "
            "To the Parking lot is through the door to the North.")
parking_lot = Room("Parking Lot", None, 'R19A', 'Art Building', 'Hallway', None, None,
                   "There are cars parked here. To the south is Mr. Wiebe's room."
                   " To the west is the Main hallway and to the east is the art building.")
art_building = Room("Art Building", None, 'Parking Lot', None, None, None, None,
                    "There are paintings covering the walls, To the west is the Parking Lot.")
hallway = Room("Hallway", 'Library', 'Quad', 'Parking Lot', 'Gym', None, None,
               "This is the main hallway. The Parking Lot is to the east." 
               "The Quad is to the south. The Gym is to the west. The Library is to the north.")
library = Room("Library", 'Suspicious Room', 'Hallway', None, None, None, None,
               "This is the library. Books cover the walls. "
               "There's a path to the south back to the Main Hallway "
               "and a suspicious door to the north.")
suspicious_room = Room("Suspicious Room", None, 'Library', None, None, 'Kings Room', None,
                       "This is a suspicious room. There is a path the the south leading back "
                       "to the Library, and there is a ladder leading up to a hatch to another room.",
                       npc3)
kings_room = Room("Kings Room", None, None, None, None, None, 'Suspicious Room', )
quad = Room("Quad", 'Hallway', 'Cafeteria', 'East Building', 'West Building', None, None,
            "This is the quad. It is an open space at the center of the school. There is "
            "a path to the north leading to the Hallway, a path to the south leading to the cafeteria, "
            "a path to the east leading to the East Building, and a path to the west leading "
            "to the West Building")
gym = Room("Gym", None, 'West Building', 'Hallway', None, None, None,
           "This is the Gym. There's nobody in here and all of the lights are off. "
           "There is a path to the south leading to the West Building and a path to the "
           "west leading back to the hallway.")
west_building = Room("West Building", 'Gym', 'West Field', 'Quad', 'Restroom', None, None,
                     "This is the West Building. A large building with a tall ceiling and many "
                     "classrooms lining the walls. There is a north path to the gym, a south "
                     "path to the West Field, an east path to the Quad, and a west path "
                     "to the West Field.")
restroom = Room("Restroom", None, None, 'West Building', None, None, None,
                "This is the west building Restroom. There are cockroaches running "
                "across the floor and all of the stalls are in very poor condition. "
                "There's a path to the east back to the West Building.")
west_field = Room("West Field", 'West Building', None, None, None, None, None,
                  "This is the west field. All of the grass is dead leaving a long wide "
                  "field of brown. To the north is the West Building.")
cafeteria = Room("Cafeteria", 'Quad', None, None, None, None, None,
                 "This is the cafeteria. Usually lunch would be served here but the room is "
                 "empty. There is a door to the south leading outside to the quad.")
east_building = Room("East Building", None, 'science Building', None, 'Quad', 'East Building Upstairs', None,
                     "This is the East Building. It's a two story building with very few classrooms. "
                     "There is a door leading back to the quad, there are stairs leading up to the second "
                     "story, and there is a door going out to the science building.")
east_building_upstairs = Room("East Building Upstairs", None, None, None, None, None, 'East Building'
                              "This is the upstairs of the East Building.")
science_building = Room("Science Building", "East Building", None, None, None, None, None,
                        "This is the science building. There is a path to the ")

restroom.character = npc3
R19A.north = parking_lot
parking_lot.south = R19A
parking_lot.east = art_building
parking_lot.west = hallway
art_building.west = parking_lot
hallway.north = library
hallway.south = quad
hallway.east = parking_lot
hallway.west = gym
library.north = suspicious_room
suspicious_room.south = library
suspicious_room.up = kings_room
kings_room.down = suspicious_room
gym.south = west_building
west_building.west = restroom
west_building.north = gym
restroom.east = west_building

# DO NOT TOUCH

player = Player(R19A)

c1 = Character("Orc1", 100, sword1, None)
c2 = Character("Orc2", 100, sword2, None)
c1.attack(c2)
c2.attack(c1)

playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']

while playing:
    print(player.current_location.name)
    print(player.current_location.description)
#    print(player.current_location.character)
    command = input(">_")

    if command in short_directions:
        pos = short_directions.index(command.lower())
        command = directions[pos]

    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.lower() in directions:
        try:
            # Command = 'North'
            room_object = getattr(player.current_location, command)
            # room_var = globals(){room_object]
            player.move(room_object)
        except KeyError:
            print("This key does not exist")
        except AttributeError:
            print("I can't go that way.")
    else:
        print("Command not recognized.")
