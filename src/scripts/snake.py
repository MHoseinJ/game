from src.log import log, Type
from src.gameobject import GameObject
import src.variables as variables
from src.script import Script
from src.functions import find_object

class Snake(Script):

    def start(self):
        self.apple = find_object("apple")
        self.snake = find_object("snake")
        # self.parts = [(int(WIDTH / 2), int(HEIGHT / 2))]
        self.parts: list[GameObject] = self.snake.get_childs()
        self.parts.append(GameObject("part", int(variables.WIDTH / 2), int(variables.HEIGHT / 2), variables.COLORS["snake"], variables.BLOCK_SIZE, variables.BLOCK_SIZE, []))
        self.velocity = (0, 1)
        self.direction = variables.DIRECTIONS.TOP

    def update(self, dt):
        keys_down = variables.KEYS
        
        if len(keys_down):
            print(keys_down[-1] + "ridam dahanet")
            match keys_down[-1]:
                case variables.DIRECTIONS.TOP.value:
                    self.direction = variables.DIRECTIONS.TOP
                    self.velocity = (0, 1)
                case variables.DIRECTIONS.DOWN.value:
                    self.direction = variables.DIRECTIONS.DOWN
                    self.velocity = (0, -1)
                case variables.DIRECTIONS.LEFT.value:
                    self.direction = variables.DIRECTIONS.LEFT
                    self.velocity = (-1, 0)
                case variables.DIRECTIONS.RIGHT.value:
                    self.direction = variables.DIRECTIONS.RIGHT
                    self.velocity = (1, 0)
            print(keys_down[-1])

        # add head            
        self.parts.append(GameObject("part", self.parts[-1].x + self.velocity[0], self.parts[-1].y + self.velocity[1], variables.COLORS["snake"], variables.BLOCK_SIZE, variables.BLOCK_SIZE, []))

        # check if head colided with apple
        if self.parts[-1].x == self.apple.x and self.parts[-1].y == self.apple.y:
            # it's colided
            pass
        else:
            # no it didn't colided
            self.parts.pop(0)

        log(Type.WARN, str(self.parts[-1].y))
        log(Type.WARN, str(self.parts[-1].x))
        log(Type.INFO, str(len(self.parts)))
