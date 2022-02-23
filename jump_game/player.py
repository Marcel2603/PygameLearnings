from enum import Enum

import pygame.sprite


class PlayerSkin(Enum):
    DEFAULT = "assets/triceratops.png"
    TRICERATOPS = "assets/triceratops.png"
    VELOCIRAPTOR = "assets/velociraptor.png"


class Player(pygame.sprite.Sprite):

    def __init__(self, start_pos, obstacle_sprites, skin=PlayerSkin.DEFAULT):
        super().__init__()
        self.image = pygame.image.load(skin.value)
        self.rect = self.image.get_rect(bottomright=start_pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.jump_speed = 20
        self.gravity = 0.3
        self.base_line = start_pos[1]
        self.obstacle_sprites = obstacle_sprites
        self.is_floor = True

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.is_floor:
            self.direction.y = - self.jump_speed

    def apply_gravity(self):
        if not self.is_floor:
            self.direction.y += self.gravity

    def check_base_line(self):
        y = self.rect.bottom
        if y == self.base_line:
            self.is_floor = True
        elif y > self.base_line:
            self.direction.y = 0
            self.rect.bottom = self.base_line
        else:
            self.is_floor = False

    def collide(self):
        for sprite in self.obstacle_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                self.kill()

    def update(self):
        self.get_input()
        self.apply_gravity()
        self.check_base_line()
        self.rect.bottomright += self.direction
        self.collide()
