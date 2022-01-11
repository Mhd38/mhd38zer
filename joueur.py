import core
import random
import pygame
from pygame.math import Vector2

class Joueur :

    def __init__(self):
        self.couleur =(random.randint(0, 200), random.randint(0, 20), random.randint(0, 200))
        self.x = random.randint(100, 400)
        self.y = random.randint(100, 400)
        self.vitesse = 4
        self.masse = 20

    def move(self):
        "Bilan des forces"


