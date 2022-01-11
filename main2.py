import core
import pygame
import joueur
import random
from pygame.math import Vector2
import creep
import mohamed


def setup():
    print("---setup-----start")
    core.fps = 30
    core.WINDOW_SIZE = [1300, 940]
    core.memory("nbrcreep", 200)
    core.memory("listcreep", [])

    for i in range(0, core.memory("nbrcreep")):
        core.memory("listcreep").append(creep.Creep(core.WINDOW_SIZE[0], core.WINDOW_SIZE[1]))
    print("---setup-------end")


def run():
    core.cleanScreen()
    for c in core.memory("listcreep"):
        c.show(core.screen)


core.main(setup, run)
