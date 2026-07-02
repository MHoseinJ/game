from src.scripts.snake import Snake
import pygame
from src import functions
from src import variables
import time

# init screen
variables.SCREEN = functions.init(variables.WIDTH, variables.HEIGHT, variables.BLOCK_SIZE, variables.TITLE)

running = True

variables.SCRIPTS.append(Snake())

# call start
functions.call_start(variables.SCRIPTS)

while running:

    # the start of the frame
    start = time.perf_counter()
    # fill screen
    variables.SCREEN.fill(variables.COLORS["black"])

    # proccessing keys
    keys = functions.get_events(pygame.event.get())

    if "quit" in keys:
        running = False
    
    delta_time = time.perf_counter() - start

    functions.call_update(variables.SCRIPTS, delta_time)

    # draw everything pending on surface
    pygame.display.flip()
