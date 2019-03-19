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
                 up=None, down=None, description="", character="", items=[]):
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
spray3 = Weapon("Anti-Wiebe Spray", 200)
dog_treat1 = Item("Green Treat")
dog_treat2 = Item("Brown Treat")
dog_toy1 = Item("Hard Dog Toy")
dog_toy2 = Item("Soft Dog Toy")
pillow1 = Item("Liam Neeson Pillow Body Pillow")
pillow2 = Item("Pepe The Frog Pillow")
pillow3 = Item("Bob Ross Pillow Body Pillow")
armor1 = Armor("Leather Armor", 30)
armor2 = Armor("Iron Armor", 50)
armor3 = Armor("Diamond Armor", 80)
armor4 = Armor("Legendary Armor", 100)
# characters
npc1 = Character("Juli", 200, battle_axe3, armor4)

# rooms

# Option 1
R19A = Room("R19A")
art_building = Room("Art Building")
hallway = Room("Hallway")
parking_lot = Room('The Parking Lot', None, R19A, art_building, hallway, None, None,
                   "There are cars parked here. To the south is Mr. Wiebe's room."
                   " To the west is the Main hallway and to the east is the art building.")

R19A.north = parking_lot
parking_lot.south = R19A

# Option 2
# Put Them Away
# R19A = Room("R19A", 'parking_lot')

art_building = Room('Art Building', None, parking_lot, None, None, None, None,
                    "There are paintings covering the walls. "
                    "To the west is The Parking Lot")

art_building.west = parking_lot
library = Room("Library")
quad = Room("Quad")
gym = Room("Gym")
hallway = Room('The Hallway', library, quad, parking_lot, gym, None, None,
               "This is the main hallway.The Parking Lot is to the east,"
               " the quad is to the south, the gym is to the west"
               " and the library is to the north.")

hallway.north = library
hallway.south = quad
hallway.east = parking_lot
hallway.east = gym

library = Room('Library', 'suspicious_room', 'library', None, None, None, None,
               "This is the library. Books cover the walls. "
               "There's a path to the south back to the Main Hallway "
               "and a suspicious door to the north.",)


player = Player(R19A)

c1 = Character("Orc1", 100, sword, None)
c2 = Character("Orc2", 100, sword2, None)
c1.attack(c2)
c2.attack(c1)

playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']

while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    command = input(">_")
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
