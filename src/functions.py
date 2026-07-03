from src.log import log, Type
from src.gameobject import GameObject
from src.variables import GAMEOBJECTS, KEYS
import pygame

def init(width: int, height: int, block_size: int, title: str):

    pygame.init()

    screen = pygame.display.set_mode([width * block_size, height * block_size])
    pygame.display.set_caption(title)

    return screen

def get_events(events) -> list[str]:

    keys_down = []

    for event in events:
        if (event.type == pygame.QUIT):
            return ["quit"]
        if (event.type == pygame.KEYDOWN):
            keys_down.append(pygame.key.name(event.key))

    return keys_down

def call_start(scripts):

    for script in scripts:
        script.start()

def call_update(scripts, dt):
    
    for script in scripts:
        script.update(dt)

def find_object(name: str, objects: list[GameObject] = GAMEOBJECTS) -> GameObject:
    for object in objects:
        if object.get_name() == name:
            return object

    return GameObject()
