class Dinosaur:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power  

    def dinosaur_attack(self, robot):
        robot.health -= self.attack_power