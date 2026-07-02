from src.functions import find_object
from src.script import Script
from random import randint
from src.variables import WIDTH, HEIGHT

class Apple(Script):

    def start(self):
        self.is_available = False
        self.game_object = find_object("apple")
        self.pos = [0,0]

    def update(self, dt):
        
        if not self.is_available:
            x = randint(0, WIDTH - 1)
            y = randint(0, HEIGHT - 1)

            self.pos = [x, y]

            self.game_object.set_pos(self.pos[0], self.pos[1])
