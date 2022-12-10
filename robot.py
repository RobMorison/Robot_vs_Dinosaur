from weapon import Weapon



class Robot:

    def __init__ (self, name,health):
        self.name = name
        self.health = health
        self.active_weapon = Weapon("Hammer", 35)

    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        if dinosaur.health <= 0:
            print(f'\n{self.name} attacked {dinosaur.name} with {self.active_weapon.name} he has 0 health remaining')
        else:
            print(f'\n{self.name} attacked {dinosaur.name} with {self.active_weapon.name} he has  {dinosaur.health} health remaining')