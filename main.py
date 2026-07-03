from src.scripts.background import Background
from src.scripts.apple import Apple
from src.render import render_gameobjects
from src.scripts.snake import Snake
import pygame
from src import functions
from src import variables
import time

# init screen
variables.SCREEN = functions.init(variables.WIDTH, variables.HEIGHT, variables.BLOCK_SIZE, variables.TITLE)

running = True

variables.SCRIPTS.append(Background())
variables.SCRIPTS.append(Snake())
variables.SCRIPTS.append(Apple())

# call start
functions.call_start(variables.SCRIPTS)

while running:

    # the start of the frame
    start = time.perf_counter()
    # fill screen
    variables.SCREEN.fill(variables.COLORS["black"])

    # proccessing keys
    variables.KEYS = functions.get_events(pygame.event.get())
    
    if "quit" in variables.KEYS:
        running = False
    
    delta_time = time.perf_counter() - start

    functions.call_update(variables.SCRIPTS, delta_time)

    # draw things
    render_gameobjects(variables.SCREEN)
    
    # draw everything pending on surface
    pygame.display.flip()

    time.sleep(0.1)
