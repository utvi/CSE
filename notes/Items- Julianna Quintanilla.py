class Weapon(object):
    def __init__(self, name, handle, blade):
        self.name = name
        self.handle_type = handle
        self.blade_type = blade
        self.damage = 15


class Sword(Weapon):
    def __init__(self, name, blade_type, handle_type):
        super(Sword, self).__init__(name, blade_type, handle_type)

    def swing_forward(self):
        print("You swing forward.")

    def swing_left(self):
        print("You swing to your left.")

    def swing_right(self):
        print("You swing to your right.")


class iron_sword(Sword):
    def __init__(self):
        super(iron_sword, self).__init__("Iron sword", "iron", "one-handed")


class diamond_sword(Sword):
    def __init__(self):
        super(diamond_sword, self).__init__("Diamond sword", "Diamond", "two-handed")


class Bow(Weapon):
    def __init__(self, name, bow_type, damage=15):
        super(Bow, self).__init__(name, bow_type)
        self.damage = damage

    def shoot_forward(self):
        print("You shoot forward.")


class wood_bow(Bow):
    def __init__(self):
        super(wood_bow, self).__init__("Wood bow", "wood")
        self.damage = 15


class diamond_bow(Bow):
    def __init__(self):
        super(diamond_bow, self).__init__("Diamond Bow", "diamond")
        self.damage = 20


