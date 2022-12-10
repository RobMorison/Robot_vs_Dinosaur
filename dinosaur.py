class Dinosaur:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power  

    def attack(self, robot):
        robot.health -= self.attack_power
        if robot.health <= 0:
            print(f'\n{self.name} attacked leaving {robot.name} with 0 health remaining')
        else:
            print(f'\n{self.name} attacked leaving {robot.name} with {robot.health} health remaining')