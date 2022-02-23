import random

import pygame.sprite

from bird import Bird
from game_info import GameInfo
from pipe import build_pipe

BACKGROUND_PATH = "assets/background.png"


class Game:
    def __init__(self, display: pygame.Surface, main_font: pygame.font.SysFont, pipe_space=300):
        self.main_font = main_font
        self.display = display
        self.max_height = display.get_height()
        self.max_width = display.get_width()
        self.background_img = pygame.transform.smoothscale(
            pygame.image.load(BACKGROUND_PATH),
            (self.max_width, self.max_height)
        )
        self.pipeline_creation_threshold = self.max_width - pipe_space

        self.game_info = GameInfo()
        self.pipes = pygame.sprite.Group()
        self.birds = pygame.sprite.Group(Bird((100, 100), self.max_height, self.pipes, self.game_info))

    def run(self):
        run = True
        self._create_pipelines()
        self._update_game()
        self._draw_game()
        if not self.game_info.alive:
            run = self._finish_game()
        return run
    
    def _update_game(self):
        if self.game_info.alive:
            self.birds.update()
            self.pipes.update()

    def _draw_game(self):
        self.display.blit(self.background_img, (0, 0))
        self.birds.draw(self.display)
        self.pipes.draw(self.display)
        self._draw_score()
        # if not self.game_info.alive:
        #     run = self._finish_game()

    def _create_pipelines(self):
        if len(self.pipes) == 0:
            self._build_random_pipe()
        else:
            last_pipe = 0
            for pipe in self.pipes.sprites():
                last_pipe = max(pipe.rect.right, last_pipe)
            if last_pipe < self.pipeline_creation_threshold:
                self._build_random_pipe()

    def _build_random_pipe(self):
        minimum_length = 50
        available_length = self.max_height - minimum_length
        space = random.randint(100, 250)  # min 100 max 250
        top_length = random.randint(minimum_length, available_length - space)  # min 100 max available - space
        build_pipe(self.pipes, self.max_width, self.max_height - 3, top_length, space, self.game_info)

    def _reset(self):
        self.game_info.reset()
        self.pipes = pygame.sprite.Group()
        self.birds = pygame.sprite.Group(Bird((100, 100), self.max_height, self.pipes, self.game_info))

    def _draw_score(self):
        score = int(self.game_info.passed_pipes / 2)
        message = f'Score: {score}'
        render = self.main_font.render(message, 1, 'black')
        self.display.blit(render, (self.display.get_width() - render.get_width(), 0))

    def _finish_game(self) -> bool:
        score = int(self.game_info.passed_pipes / 2)
        message = f'Game end! You have scored {score} Points!'
        retry_message = "Press any key to play again!"
        display_height = self.display.get_height() / 2
        display_width = self.display.get_width() / 2
        game_message = self.main_font.render(message, 1, 'black')
        retry_render = self.main_font.render(retry_message, 1, 'black')
        self.display.blit(game_message, (display_width - game_message.get_width() / 2,
                                         display_height - game_message.get_height() / 2))
        self.display.blit(retry_render, (display_width - retry_render.get_width() / 2,
                                         display_height + game_message.get_height() - retry_render.get_height() / 2))
        pygame.display.flip()
        run = True
        while not self.game_info.alive and run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
                if event.type == pygame.KEYDOWN:
                    self._reset()
                    break
        return run
