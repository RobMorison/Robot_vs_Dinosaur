from weapon import Weapon


class Robot:
    def __init__ (self, name, health):
        self.name = name
        self.health = health
        self.active_weapon = Weapon("Plasma Blaster", 35)

    def robot_attack(self, dinosaur):
        self.active_weapon -= dinosaur.health
        