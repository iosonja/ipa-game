from random import randrange
import pygame


class Bubble:
    def __init__(self, renderer):
        colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

        self.x = 0
        self.y = 50 + randrange(300)  # make bubbles appear from random heights
        self.radius = 50
        self._color = colors[randrange(3)]
        self._renderer = renderer
        self.is_moving = True

        if self._color == (255, 0, 0):
            self.key = pygame.K_r
        elif self._color == (0, 255, 0):
            self.key = pygame.K_g
        else:
            self.key = pygame.K_b

    def move(self, amount):
        self.x += amount

    def rerender(self):
        self._renderer.redraw(self._color, self.x,
                              self.y, self.radius)
