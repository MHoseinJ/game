from src.functions import find_object
from src.script import Script
from random import randint
from src.variables import WIDTH, HEIGHT, BLOCK_SIZE

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

            self.game_object.set_pos(self.pos[0] * BLOCK_SIZE, self.pos[1] * BLOCK_SIZE)
            self.is_available = True
