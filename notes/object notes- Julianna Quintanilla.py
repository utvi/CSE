import Special_Random


# class WaterGun(object):
#    def __init__(self, capacity=5.2, distance=30, stock=False, ):
# These are things that the WaterGun has.
# All of these should be relevant to our program
#        self.capacity = capacity
#        self.range = distance
#        self.trigger = True
#        self.stock = stock
#        self.duration_of_pressure = 5

#    def shoot(self, time):
#        if self.trigger:
#            if self.duration_of_pressure <= 0:
#                print("There's no pressure!")
#            elif self.duration_of_pressure < time:
#                print("You run out of pressure after firing for %s seconds" % self.duration_of_pressure)
#                self.duration_of_pressure = 0
#            else:
#                print("You shoot for %s seconds" % time)
#                self.duration_of_pressure -= time
#        else:
#            print("There's no trigger!")

#    def pump_it_up(self):
#        self.duration_of_pressure = 5
#        print("You pump up the tank and back to full pressure")


# Initialize the objects
# my_water_gun = WaterGun(5.2, 40, True)
# your_water_gun = WaterGun(1.0, 1, False)
# wiebe_water_gun = WaterGun(999999999, 999999999, True)
# yahir_water_gun = WaterGun(0.1)

# Do stuff with the objects
# my_water_gun.shoot(5)
# my_water_gun.pump_it_up()
# my_water_gun.shoot(1)

# print(Special_Random.RandomWiebe.special_random())


# slingshot
class SlingShot(object):
    def __int__(self, capacity=1, distance=20, ):
        self.capacity = capacity
        self.range = distance
        self.band = True
        self.ammo = True
        self.power = 5
# the longer you hold the rubber band back the farther it
# goes but if you pull too hard it will snap but you will immediately fix it.
    def shoot(self, time):
        if self.band:
            if self.power <= 0:
                print("You need to pull the band back!")
            elif self.power < time:
                print("You run out of ammo after firing")

    def pull_band(self):
       self.power = 5
    print("You pull the band back as far as it will go")

# Initialize the objects

    my_slingshot = SlingShot(5.2, 40, True)
    your_slingshot = SlingShot(5.2, 40, True)
    wiebe_slingshot = SlingShot(5.2, 40, True)
