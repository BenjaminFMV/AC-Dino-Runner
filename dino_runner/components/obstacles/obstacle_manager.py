import pygame.time
#import random

#from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import CACTUS#, BIRD


class ObstacleManager:

    def __init__(self):
        self.obstacles = []
        #self.number = random.randint(0, 1)

    def update(self, game):
        if len(self.obstacles) == 0:
            #if self.number == 0:
            self.obstacles.append(Cactus(CACTUS))
            #if self.number == 1:
                #self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(500)
                game.playing = False
                game.death_count += 1
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
