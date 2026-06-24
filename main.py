import pygame
from src import functions
from src import variables

variables.SCREEN: Surface = functions.init(variables.WIDTH, variables.HEIGHT, variables.TITLE)

running = True

while running:
    variables.SCREEN.fill(variables.COLORS["black"])

    keys = functions.get_events(pygame.event.get())

    if "quit" in keys:
        running = False
