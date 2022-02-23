import pygame

from dino_game import Game

pygame.init()
display = pygame.display.set_mode((1200, 700))

run = True
game = Game(display)
while run:
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            run = False
            break

    display.fill('black')
    running = game.run()
    pygame.display.update()
    if not running:
        game.end()
pygame.quit()
