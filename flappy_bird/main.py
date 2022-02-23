import pygame

from flappy_game import Game

pygame.init()
pygame.font.init()
display = pygame.display.set_mode((1200, 700))
main_font = pygame.font.SysFont("comicsans", 44)

run = True
game = Game(display, main_font)
clock = pygame.time.Clock()
while run:
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            run = False
            break

    display.fill('black')
    status = game.run()
    if not status:
        run = False
        break
    pygame.display.update()
    clock.tick(60)
pygame.quit()
