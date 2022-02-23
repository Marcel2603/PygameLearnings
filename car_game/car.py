import pygame


class Car(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.original_img = pygame.image.load("assets/car.jpg")
        self.image = self.original_img
        self.rect = self.image.get_rect(topleft=pos)
        self.start_pos = pos
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 1
        self.brake_speed = 0.05
        self.angle = 0
        self.rotation_speed = 1

    def accelerate(self):
        self.direction.x = self.speed

    def brake(self):
        self.direction.x -= self.brake_speed
        if self.direction.x < 0:
            self.direction.x = 0

    def rotate(self):
        """
        rotate image
        """
        self.image = pygame.transform.rotate(self.original_img, - self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.direction.rotate_ip(-self.angle)

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.accelerate()
        if keys[pygame.K_s]:
            self.brake()
        if keys[pygame.K_a]:
            self.direction.y = -1
            self.angle = max(self.angle + self.rotation_speed, -45)
        if keys[pygame.K_d]:
            self.direction.y = 1
            self.angle = min(self.angle - self.rotation_speed, 45)
        if keys[pygame.K_r]:
            self.reset(force=True)

    def reset(self, force=False):
        """
        just a temp method for resetting the car
        """
        x = self.rect.right
        if x > 1200 or force:
            self.rect.center = self.start_pos
            self.angle = 0
            self.direction = pygame.math.Vector2(0, 0)

    def update(self):
        self.get_input()
        self.rotate()
        self.rect.center += self.direction
        self.reset()
