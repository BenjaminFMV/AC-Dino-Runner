import pygame

from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.powerup_manager import PowerUpManager
from dino_runner.components.lifes.heaths import Heaths
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, RUNNING
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components import text_utils


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.heaths = Heaths()
        self.points = 0
        self.points_final = 0
        self.running = True
        self.death_count = 0

    def run(self):
        # Game loop: events - update - draw
        self.obstacle_manager.reset_obstacles()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def execute(self):
        while self.running:
            if not self.playing:
                self.show_menu()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
        self.screen.fill((255, 255, 255))

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self.game_speed, self.player)

    def draw(self):
        self.score()
        self.clock.tick(FPS)
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.heaths.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def score(self):
        self.points += 1
        self.points_final = self.points

        if self.points % 100 == 0:
            self.game_speed += 1

        text, text_rect = text_utils.get_score_element_beginning(self.points)
        self.screen.blit(text, text_rect)
        self.player.check_invincibility(self.screen)

    def print_menu_elements(self):
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            self.screen.blit(RUNNING[0], (half_screen_width - 40, half_screen_height - 140))
            text, text_rect = text_utils.get_centered_message('Press any key to start')
            self.screen.blit(text, text_rect)

        if self.death_count >= 1:
            self.screen.blit(RUNNING[0], (half_screen_width - 40, half_screen_height - 140))
            text, text_rect = text_utils.get_centered_message('Press any key to start')
            self.screen.blit(text, text_rect)
            text, text_rect = text_utils.get_score_element_final(self.points_final)
            self.screen.blit(text, text_rect)
            text, text_rect = text_utils.get_deaths_element_final(self.death_count)
            self.screen.blit(text, text_rect)
            self.points = 0
            self.running

    def show_menu(self):
       self.running = True

       white_color = (255, 255, 255)
       self.screen.fill(white_color)

       self.print_menu_elements()

       pygame.display.update()

       self.handle_key_events_on_menu()

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.run()
