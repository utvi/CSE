class Weapon(object):
    def __init__(self, name, handle, damage):
        self.name = name
        self.handle_type = handle
        self.damage = damage


class Sword(Weapon):
    def __init__(self, name, blade_type, handle_type, damage):
        super(Sword, self).__init__(name, handle_type, damage)
        self.blade_type = blade_type


class IronSword(Sword):
    def __init__(self):
        super(IronSword, self).__init__("Iron sword", "iron", "one-handed", "10")


class DiamondSword(Sword):
    def __init__(self):
        super(DiamondSword, self).__init__("Diamond sword", "Diamond", "two-handed", "25")


class Bow(Weapon):
    def __init__(self, name, bow_type, damage):
        super(Bow, self).__init__(name, bow_type, damage)
        self.range = 15  # ft


class WoodBow(Bow):
    def __init__(self):
        super(WoodBow, self).__init__("Wood bow", "wood", "15")
        self.range = range


class DiamondBow(Bow):
    def __init__(self):
        super(DiamondBow, self).__init__("Diamond Bow", "diamond", "25")
        self.range = 20


class BattleAxe(Weapon):
    def __init__(self, name, head_type, handle_type, damage):
        super(BattleAxe, self).__init__(name, head_type, damage)
        self.handle_type = handle_type


class IronBattleAxe(BattleAxe):
    def __init__(self):
        super(IronBattleAxe, self).__init__("Iron Battle Axe", "Iron", "One-handed", 20)


class DiamondBattleAxe(BattleAxe):
    def __init__(self):
        super(DiamondBattleAxe, self).__init__("Diamond Battle Axe", "Diamond", "One-handed", 30)


class LegendaryBattleAxe(BattleAxe):
    def __init__(self):
        super(LegendaryBattleAxe, self).__init__("Legendary Battle Axe", "Ancient Metal", "One-handed", 40)


class Taser(Weapon):
    def __init__(self, name, handle_type, damage):
        super(Taser, self).__init__(name, handle_type, damage)


class TaserGun(Taser):
    def __init__(self):
        super(TaserGun, self). __init__("Taser Gun", "One-handed", 90)


class Spray(Weapon):
    def __init__(self, name, handle_type, damage):
        super(Spray, self).__init__(name, handle_type, damage)


class PepperSpray(Spray):
    def __init__(self):
        super(PepperSpray, self).__init__("Pepper Spray", "One-handed", "20")


class AntiWeebSpray(Spray):
    def __init__(self):
        super(AntiWeebSpray, self).__init__("Anti-Weeb Spray", "One-handed", "50")


class AntiWiebeSpray(Spray):
    def __init__(self):
        super(AntiWiebeSpray, self).__init__("Anti-Wiebe Spray", "One-handed", "99")


class Item(object):
    def __init__(self, name):
        self.name = name


class DogTreat(Item):
    def __init__(self, name):
        super(DogTreat, self).__init__(name)


class GreenTreat(DogTreat):
    def __init__(self):
        super(GreenTreat, self).__init__("Green Treat")


class BrownTreat(DogTreat):
    def __init__(self):
        super(BrownTreat, self).__init__("Brown Treat")


class DogToy(Item):
    def __init__(self, name):
        super(DogToy, self).__init__(name)


class HardToy(DogToy):
    def __init__(self):
        super(HardToy, self).__init__("Hard Dog Toy")


class SoftToy(DogToy):
    def __init__(self):
        super(SoftToy, self).__init__("Soft Dog Toy")


class Pillow(Item):
    def __init__(self, name):
        super(Pillow, self).__init__(name)


class LiamPillow(Pillow):
    def __init__(self):
        super(LiamPillow, self).__init__("Liam Neeson Pillow")


class PepePillow(Pillow):
    def __init__(self):
        super(PepePillow, self).__init__("Pepe the Frog Pillow")


class NeilPillow(Pillow):
    def __init__(self):
        super(NeilPillow, self).__init__("Neil deGrasse Tyson Pillow")


class Armor(object):
    def __init__(self, name, protection):
        self.name = name
        self.protection = protection


class Leather(Armor):
    def __init__(self):
        super(Leather, self).__init__("leather armor", 30)


class Iron(Armor):
    def __init__(self):
        super(Iron, self).__init__("Iron Armor", 50)


class Diamond(Armor):
    def __init__(self):
        super(Diamond, self).__init__("Diamond Armor", 80)


class Legendary(Armor):
    def __init__(self):
        super(Legendary, self).__init__("Legendary Armor", 100)
