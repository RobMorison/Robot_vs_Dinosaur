from robot import Robot
from dinosaur import Dinosaur


class Battlefield:

    def __init__ (self):
        self.robot_one = Robot("Steve", 100)
        self.dinosaur_one = Dinosaur("Ralphy", 100, 20) 

    def run_game(self): # controller functions to call all the other main functions
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
        

    def display_welcome(self):
        print("\nWelcome to a battle for the ages\nOnly one side can win")

    def battle_phase(self):
        while self.robot_one.health > 0 and self.dinosaur_one.health >0:
            self.robot_one.attack(self.dinosaur_one)
            
            self.dinosaur_one.attack(self.robot_one)
            

    def display_winner(self):
        pass
