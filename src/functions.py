import pygame

def init(width: int, height: int, title: str):

    pygame.init()

    screen = pygame.display.set_mode([width, height])
    pygame.display.set_caption(title)

    return screen

def get_events(events):

    keys_down = []

    for event in events:
        if (event.type == pygame.QUIT):
            return ["quit"]
        if (event.type == pygame.KEYDOWN):
            keys_down.append(pygame.key.name(event.key))

    return keys_down
