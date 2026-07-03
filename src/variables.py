from enum import Enum
from src.gameobject import GameObject

WIDTH  = 20
HEIGHT = 20

BLOCK_SIZE = 30

TITLE = "game python"

SCREEN = 0

COLORS = {
    "black": (0,0,0),
    "white": (255,255,255),
    "light_bg": (80, 255, 100),
    "dark_bg": (50, 150, 60),
    "apple": (250, 10, 0),
    "snake": (180, 50, 100)
}

SCRIPTS = [

]

GAMEOBJECTS = [
    # background
    GameObject("background", 0, 0, COLORS["black"], 0, 0, []),
    
    # apple
    GameObject("apple", 0, 0, COLORS["apple"], BLOCK_SIZE, BLOCK_SIZE, []),

    # snake
    GameObject("snake", 0, 0, COLORS["black"], 0, 0, []),
]

# you can change these values according to pygame key codes
class DIRECTIONS(Enum):
    TOP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"

KEYS = []
