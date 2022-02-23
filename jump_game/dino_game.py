import pygame

from obstacle import Obstacle
from player import Player, PlayerSkin


class Game:

    def __init__(self, surface: pygame.Surface):
        self.display = surface
        self.background = pygame.image.load("assets/background.jpg")
        self.obstacles = pygame.sprite.Group()
        self.players = pygame.sprite.Group(Player((200, 572), self.obstacles, skin=PlayerSkin.VELOCIRAPTOR))

    def run(self):
        # actions
        if len(self.obstacles) == 0:
            self.obstacles.add(Obstacle((1000, 572)))
        game_running = True
        if len(self.players) == 0:
            game_running = False
        self.draw_game()
        return game_running

    def draw_game(self):
        self.players.update()
        self.obstacles.update()

        self.display.blit(self.background, (0, 0))
        self.players.draw(self.display)
        self.obstacles.draw(self.display)

    def end(self):
        for sprite in self.obstacles.sprites():
            sprite.stop()
