import pygame

from race import Race

pygame.init()
display = pygame.display.set_mode((1200, 700))
clock =  pygame.time.Clock()
race = Race(display)
run = True
while run:
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            run = False
            break

    display.fill('black')
    race.run()
    pygame.display.update()
    clock.tick(60)
pygame.quit()
