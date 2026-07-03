from src.scripts.apple import Apple
from src.log import log, Type
from typing import cast
from src.gameobject import GameObject
import src.variables as variables
from src.script import Script
from src.functions import find_object, find_script

class Snake(Script):

    def start(self):
        self.apple = find_object("apple")
        self.apple_script = cast(Apple, find_script("Apple"))
        self.snake = find_object("snake")
        # self.parts = [(int(WIDTH / 2), int(HEIGHT / 2))]
        self.parts: list[GameObject] = self.snake.get_childs()
        self.parts.append(GameObject("part", int(variables.WIDTH / 2) * variables.BLOCK_SIZE, int(variables.HEIGHT / 2) * variables.BLOCK_SIZE, variables.COLORS["snake"], variables.BLOCK_SIZE, variables.BLOCK_SIZE, []))
        self.velocity = (0, 1)
        self.direction = variables.DIRECTIONS.TOP

    def update(self, dt):
        keys_down = variables.KEYS
        
        if len(keys_down):

            match keys_down[-1]:
                case variables.DIRECTIONS.TOP.value:
                    if not self.direction == variables.DIRECTIONS.DOWN:
                        self.direction = variables.DIRECTIONS.TOP
                        self.velocity = (0, -1)
                        
                case variables.DIRECTIONS.DOWN.value:
                    if not self.direction == variables.DIRECTIONS.TOP:
                        self.direction = variables.DIRECTIONS.DOWN
                        self.velocity = (0, 1)
                        
                case variables.DIRECTIONS.LEFT.value:
                    if not self.direction == variables.DIRECTIONS.RIGHT:
                        self.direction = variables.DIRECTIONS.LEFT
                        self.velocity = (-1, 0)
                        
                case variables.DIRECTIONS.RIGHT.value:
                    if not self.direction == variables.DIRECTIONS.LEFT:
                        self.direction = variables.DIRECTIONS.RIGHT
                        self.velocity = (1, 0)

        # check if colided to wall or it self
        if self.parts[-1].x > (variables.WIDTH - 1) * variables.BLOCK_SIZE or self.parts[-1].x < 0 or self.parts[-1].y > (variables.HEIGHT - 1) * variables.BLOCK_SIZE or self.parts[-1].y < 0:
            log(Type.INFO, "you hit wall! saving score")
            save_score(len(self.snake.get_childs()))
            exit()
        for part in self.parts[:-1]:
            if self.parts[-1].x == part.x and self.parts[-1].y == part.y:
                log(Type.INFO, "you hit yourself! saving score")
                save_score(len(self.snake.get_childs()))
                exit()
        
        # add head            
        self.parts.append(GameObject("part", self.parts[-1].x + self.velocity[0] * variables.BLOCK_SIZE, self.parts[-1].y + self.velocity[1] * variables.BLOCK_SIZE, variables.COLORS["snake"], variables.BLOCK_SIZE, variables.BLOCK_SIZE, []))

        # check if head colided with apple
        if self.parts[-1].x == self.apple.x and self.parts[-1].y == self.apple.y:
            # it's colided
            self.apple_script.is_available = False
            
        else:
            # no it didn't colided
            self.parts.pop(0)

def save_score(score: int):
    with open("score.txt", "w") as f:
        f.write(str(score))
