import pygame

from game_info import GameInfo
IMAGE_PATH = "assets/bird.png"


class Bird(pygame.sprite.Sprite):
    def __init__(self, pos, max_height, pipes: pygame.sprite.Group, game_info: GameInfo):
        super().__init__()
        self.original_image = pygame.image.load(IMAGE_PATH).convert_alpha()
        self.image = self.original_image
        self.rect = self.image.get_rect(center=pos)
        self.max_height = max_height
        self.pipes = pipes
        self.game_info = game_info
        self.direction = pygame.math.Vector2(0, 0)
        self.jump_speed = 1
        self.gravity = 0.2
        self.angle = 0
        self.rotate_speed = 1

    def update(self) -> None:
        self._get_input()
        self._check_top_hit()
        self._apply_gravity()
        self._check_health()
        self.rect.center += self.direction

    def _get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.direction.y -= self.jump_speed
            self._rotate(up=True)

    def _apply_gravity(self):
        self.direction.y += self.gravity
        self._rotate(down=True)

    def _check_top_hit(self):
        next_pos = self.rect.top + self.direction.y
        if next_pos < 0:
            self.direction.y = 0

    def _check_health(self):
        if self.rect.top > self.max_height:
            self.game_info.alive = False
        for pipe in self.pipes.sprites():
            if pipe.rect.colliderect(self.rect):
                self.game_info.alive = False

    def _rotate(self, up=False, down=False):
        max_angle = 90
        if up:
            self.angle += self.rotate_speed
        elif down and self.direction.y > 0:
            self.angle -= self.rotate_speed / 3
        if abs(self.angle) < max_angle:
            self.image = pygame.transform.rotate(self.original_image, self.angle)
            self.rect = self.image.get_rect(center=self.rect.center)
