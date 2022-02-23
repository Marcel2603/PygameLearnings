import pygame.sprite

from game_info import GameInfo

IMAGE_PATH = "assets/pipe.png"


class Pipe(pygame.sprite.Sprite):

    def __init__(self, start_pos, length, game_info, top=False, bottom=False):
        super().__init__()
        self.image = pygame.Surface((50, length))
        self.image.fill('green')
        self.speed = 2
        self.game_info = game_info
        if top:
            self.rect = self.image.get_rect(topleft=start_pos)
        elif bottom:
            self.rect = self.image.get_rect(bottomleft=start_pos)

    def update(self):
        if self.rect.right < 0:
            self.game_info.passed_pipes += 1
            self.kill()
        self.rect.left -= self.speed


def build_pipe(group: pygame.sprite.Group, start_x, max_height, top_length, space, game_info: GameInfo):
    top_pipe = Pipe((start_x, 0), top_length, game_info, top=True)
    bottom_length = max_height - top_length - space
    bottom_pipe = Pipe((start_x, max_height), bottom_length, game_info, bottom=True)
    group.add(top_pipe, bottom_pipe)
