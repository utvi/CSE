class Weapon(object):
    def __init__(self, name, handle):
        self.name = name
        self.handle_type = handle
        self.damage = 15


class Sword(Weapon):
    def __init__(self, name, blade_type, handle_type):
        super(Sword, self).__init__(name, handle_type)
        self.blade_type = blade_type

    def swing_forward(self):
        print("You swing forward.")

    def swing_left(self):
        print("You swing to your left.")

    def swing_right(self):
        print("You swing to your right.")


class IronSword(Sword):
    def __init__(self):
        super(IronSword, self).__init__("Iron sword", "iron", "one-handed")


class DiamondSword(Sword):
    def __init__(self):
        super(DiamondSword, self).__init__("Diamond sword", "Diamond", "two-handed")


class Bow(Weapon):
    def __init__(self, name, bow_type, damage=15):
        super(Bow, self).__init__(name, bow_type)
        self.damage = damage
        self.range = 15  # ft

    def shoot_forward(self):
        print("You shoot forward.")


class WoodBow(Bow):
    def __init__(self):
        super(WoodBow, self).__init__("Wood bow", "wood")
        self.damage = 15
        self.range = range


class DiamondBow(Bow):
    def __init__(self):
        super(DiamondBow, self).__init__("Diamond Bow", "diamond")
        self.damage = 20
        self.range = 20


class BattleAxe(Weapon):
    def __init__(self, name, head_type, handle_type):
        super(BattleAxe, self).__init__(name, head_type, handle_type)
        
