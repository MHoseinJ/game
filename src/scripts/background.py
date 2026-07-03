from src.gameobject import GameObject
import src.variables as variables
from src.functions import find_object
from src.script import Script


class Background(Script):

    def start(self):
        self.parent = find_object("background")
        self.childs = self.parent.get_childs()

        for i in range(variables.WIDTH):
            for j in range(variables.HEIGHT):
                color = variables.COLORS["black"]
                if i % 2 == 0 and j % 2 == 0 or i % 2 != 0 and j % 2 != 0:
                    color = variables.COLORS["dark_bg"]
                else:
                    color = variables.COLORS["light_bg"]
                object = GameObject("piece", i * variables.BLOCK_SIZE, j * variables.BLOCK_SIZE, color, variables.BLOCK_SIZE, variables.BLOCK_SIZE, [])

                self.childs.append(object)
