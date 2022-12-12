from weapon import Weapon



class Robot:

    def __init__ (self, name,health): # Have to instantiate all three weapons, robot is physically holding three weapons now
        self.weapon_one = Weapon("Hammer", 35)
        self.weapon_two = Weapon("Plasma Laser", 25)
        self.weapon_three = Weapon("Blow Dart", 10)
        self.name = name
        self.health = health
        

    def attack(self, dinosaur):
        
        self.succesful_attack = False
        while self.succesful_attack == False:
            self.active_weapon = input(f'Select {self.name} weapon, {self.weapon_one.name}, {self.weapon_two.name}, {self.weapon_three.name}: ') # need to put second input question in to break else loop
            if self.active_weapon == "Hammer":
                dinosaur.health -= self.weapon_one.attack_power #had to rewrite code to specifically call attack power for the specic weapon called
                self.succesful_attack = True
            elif self.active_weapon == "Plasma Laser":
                dinosaur.health -= self.weapon_two.attack_power
                self.succesful_attack = True
            elif self.active_weapon == "Blow Dart":
                dinosaur.health -= self.weapon_three.attack_power
                self.succesful_attack = True
            else:
                print("Unknown weapon, please pick again")

        if dinosaur.health <= 0:
            print(f'\n{self.name} attacked {dinosaur.name} with {self.active_weapon} he has 0 health remaining')
        else:
            print(f'\n{self.name} attacked {dinosaur.name} with {self.active_weapon} he has  {dinosaur.health} health remaining')