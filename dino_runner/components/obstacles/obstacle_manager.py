import pygame

from dino_runner.components.lifes.heaths import Heaths
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import OBSTACLES


class ObstacleManager:

    def __init__(self):
        self.obstacles = []
        self.heaths = Heaths()

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(OBSTACLES))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.shield:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                else:
                    self.obstacles.remove(obstacle)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
