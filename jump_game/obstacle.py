import pygame


class Obstacle(pygame.sprite.Sprite):

    def __init__(self, start_pos):
        super().__init__()
        self.image = pygame.image.load("assets/cactus.png")
        self.rect = self.image.get_rect(bottomleft=start_pos)
        self.speed = 2

    def update(self):
        if self.rect.bottomright[0] <= 0:
            self.kill()
        self.rect.x -= self.speed

    def stop(self):
        self.speed = 0
