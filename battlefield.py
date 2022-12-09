from robot import Robot
from dinosaur import Dinosaur


class Battlefield:

    def __init__ (self): # Don't need to add variable when calling other classes ex. Robot class and Dinosaur class
        self.robot_one = Robot("Steve the Robot", 100)
        self.dinosaur_one = Dinosaur("Ralphy the Dinosaur", 100, 20) 

    def run_game(self): # controller functions to call all the other main functions
        self.display_welcome()
        self.battle_phase()
        self.display_winner()
        

    def display_welcome(self):
        print("\nWelcome to a battle for the ages\nOnly one side can win")

    def battle_phase(self): # write to solve for stopping attacks when health is zero, righ now robot still attack with -5 health
        while self.robot_one.health > 0 and self.dinosaur_one.health > 0:
            if self.robot_one.health <= 0:
                break
            else:
                self.robot_one.attack(self.dinosaur_one)
            if self.dinosaur_one.health <= 0:
                break
            else:
                self.dinosaur_one.attack(self.robot_one)
            

    def display_winner(self):
        pass
