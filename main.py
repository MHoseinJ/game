import pygame
from src import functions
from src import variables
from src.scripts.snake import Snake

scripts = [
    Snake()
]

for script in scripts:
    script.start()


variables.SCREEN: Surface = functions.init(variables.WIDTH, variables.HEIGHT, variables.TITLE)

running = True

while running:
    variables.SCREEN.fill(variables.COLORS["black"])

    keys = functions.get_events(pygame.event.get())

    if "quit" in keys:
        running = False

    
