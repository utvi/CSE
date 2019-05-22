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


class Pan(Weapon):
    def __init__(self, damage):
        super(Pan, self).__init__("Frying Pan", damage)


class AntiWiebeSpray(Weapon):
    def __init__(self, damage):
        super(AntiWiebeSpray, self).__init__("Anti-Wiebe Spray", damage)


class WoodSword(Weapon):
    def __init__(self, damage):
        super(WoodSword, self).__init__("Wooden Sword", damage)


class OrcSword(Weapon):
    def __init__(self, damage):
        super(OrcSword, self).__init__("Orc Sword", damage)


class IronSword(Weapon):
    def __init__(self, damage):
        super(IronSword, self).__init__("Iron Sword", damage)


class DiamondSword(Weapon):
    def __init__(self, damage):
        super(DiamondSword, self).__init__("Diamond Sword", damage)


class WoodBow(Weapon):
    def __init__(self, damage):
        super(WoodBow, self).__init__("Wood Bow", damage)


class DiamondBow(Weapon):
    def __init__(self, damage):
        super(DiamondBow, self).__init__("Diamond Bow", damage)


class IronBattleAxe(Weapon):
    def __init__(self, damage):
        super(IronBattleAxe, self).__init__("Iron Battle Axe", damage)


class DiamondBattleAxe(Weapon):
    def __init__(self, damage):
        super(DiamondBattleAxe, self).__init__("Diamond Battle Axe", damage)


class LegendaryBattleAxe(Weapon):
    def __init__(self, damage):
        super(LegendaryBattleAxe, self).__init__("Legendary Battle Axe", damage)


class TaserGun(Weapon):
    def __init__(self, damage):
        super(TaserGun, self).__init__("Taser Gun", damage)


class PepperSpray(Weapon):
    def __init__(self, damage):
        super(PepperSpray, self).__init__("Pepper Spray", damage)


class AntiWeebSpray(Weapon):
    def __init__(self, damage):
        super(AntiWeebSpray, self).__init__("Anti Weeb Spray", damage)


class MothClaws(Weapon):
    def __init__(self, damage):
        super(MothClaws, self).__init__("MothClaws", damage)


class HeeHee(Weapon):
    def __init__(self, damage):
        super(HeeHee, self).__init__("Hee Hee", damage)


pan1 = Pan(5)
Wood_Sword = WoodSword(15)
Orc_Sword = OrcSword(5)
Iron_Sword = IronSword(10)
Diamond_Sword = DiamondSword(25)
Wood_Bow = WoodBow(15)
Diamond_Bow = DiamondBow(25)
Iron_Battle_Axe = IronBattleAxe(20)
Diamond_Battle_Axe = DiamondBattleAxe(30)
Legendary_Battle_Axe = LegendaryBattleAxe(40)
Taser_Gun = TaserGun(90)
Pepper_Spray = PepperSpray(20)
Anti_Weeb_Spray = AntiWeebSpray(50)
Anti_Wiebe_Spray = AntiWiebeSpray(300)
Moth_Claws = MothClaws(900)
Hee_Hee = HeeHee(10)


class GreenBall(Item):
    def __init__(self):
        super(GreenBall, self).__init__("Green Ball")


class RedBall(Item):
    def __init__(self):
        super(RedBall, self).__init__("Red Ball")


class Bread(Item):
    def __init__(self):
        super(Bread, self).__init__("Bread")


class ToyTrain(Item):
    def __init__(self):
        super(ToyTrain, self).__init__("Toy Train")


class LiamNeesonBodyPillow(Item):
    def __init__(self):
        super(LiamNeesonBodyPillow, self).__init__("Liam Neeson Body Pillow")


class ShrekPillow(Item):
    def __init__(self):
        super(ShrekPillow, self).__init__("Shrek Pillow")


class BobRossBodyPillow(Item):
    def __init__(self):
        super(BobRossBodyPillow, self).__init__("Bob Ross Body Pillow")


Green_Ball = GreenBall
Red_Ball = RedBall
Bread1 = Bread
Toy_Train = ToyTrain
Liam_NeesonBody_Pillow = LiamNeesonBodyPillow
Shrek_Pillow = ShrekPillow
Bob_Ross_Body_Pillow = BobRossBodyPillow


class LeatherArmor(Armor):
    def __init__(self, protection):
        super(LeatherArmor, self).__init__("Leather Armor", protection)


class IronArmor(Armor):
    def __init__(self, protection):
        super(IronArmor, self).__init__("Iron Armor", protection)


class DiamondArmor(Armor):
    def __init__(self, protection):
        super(DiamondArmor, self).__init__("Diamond Armor", protection)


class LegendaryArmor(Armor):
    def __init__(self, protection):
        super(LegendaryArmor, self).__init__("Legendary Armor", protection)


class WiebeArmor(Armor):
    def __init__(self, protection):
        super(WiebeArmor, self).__init__("Wiebe Armor", protection)


class EggShell(Armor):
    def __init__(self, protection):
        super(EggShell, self).__init__("Egg Shell", protection)


Leather_Armor = LeatherArmor(30)
Iron_Armor = IronArmor(50)
Diamond_Armor = DiamondArmor(80)
Legendary_Armor = LegendaryArmor(100)
Wiebe_Armor = WiebeArmor(150)
Egg_Shell = EggShell(25)
# characters
Juli1 = Character("Juli", 200, Legendary_Battle_Axe, Legendary_Armor)
Mothman1 = Character("Mothman", 900, Moth_Claws, None)
Michael_Jackson = Character("Michael Jackson", 40, Hee_Hee, None)
King_Wiebe = Character("King Wiebe", 600, Taser_Gun, Wiebe_Armor)
Eggman1 = Character("Eggman", 100, Wood_Sword, Egg_Shell)
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
                       "to the Library, and there is a ladder leading up to a hatch to another room.")
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
                "There's a path to the east back to the West Building.", 'Michael Jackson', )
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

restroom.character = Michael_Jackson
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

c1 = Character("Orc1", 100, Wood_Sword, None)
c2 = Character("Orc2", 100, Orc_Sword, None)
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
