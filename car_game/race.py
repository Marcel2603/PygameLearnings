import pygame.sprite

from car import Car


class Race:
    def __init__(self, surface):
        self.display = surface
        self.cars = pygame.sprite.Group(Car((400, 400)))

    def run(self):
        self.cars.update()
        self.cars.draw(self.display)
