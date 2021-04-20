import pygame


class Bubble:
    def __init__(self, x, y, radius, color, renderer):
        self.x_position = x
        self.y_position = y
        self._radius = radius
        self._color = color
        self._renderer = renderer

        if color == (255, 0, 0):
            self.key = pygame.K_r
        elif color == (0, 255, 0):
            self.key = pygame.K_g
        else:
            self.key = pygame.K_b

    def move(self, amount):
        self.x_position += amount

    def rerender(self):
        self._renderer.redraw(self._color, self.x_position, self.y_position, self._radius)
