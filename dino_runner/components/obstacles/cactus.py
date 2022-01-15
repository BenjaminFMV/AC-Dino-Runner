import random
from dino_runner.components.obstacles.obstacle import Obstacle


class Cactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 7)
        super().__init__(image, self.type)
        if self.type == 0:
            self.rect.y = 325
        elif self.type == 1:
            self.rect.y = 325
        elif self.type == 2:
            self.rect.y = 325
        elif self.type == 6:
            self.rect.y = 250
        elif self.type == 7:
            self.rect.y = 250
        else:
            self.rect.y = 300
