from src.script import Script
from src.functions import find_object

class Snake(Script):

    def start(self):
        self.apple = find_object("apple")
        self.parts = []

    def update(self, dt):
        pass
