from random import randrange
import pygame


class Bubble:
    def __init__(self, renderer):
        self.radius = 50
        self.x = -self.radius
        self.y = randrange(80, 300)  # make bubbles appear from random heights
        self._color = self.randomize_color()[randrange(5)]
        self.key = self.define_key(self._color)
        self._renderer = renderer
        print("New bubble was initialized")

    def randomize_color(self):
        red = (255, 0, 0)
        green = (0, 255, 0)
        blue = (0, 0, 255)
        white = (255, 255, 255)
        pink = (255, 0, 255)

        colors = [red, green, blue, white, pink]
        return colors

    def define_key(self, color):
        # Change the color codes to natural language later (e.g. with a dict)
        if color == (255, 0, 0):
            return pygame.K_r
        elif color == (0, 255, 0):
            return pygame.K_g
        elif color == (0, 0, 255):
            return pygame.K_b
        elif color == (255, 255, 255):
            return pygame.K_w
        else:
            return pygame.K_p

    def move(self, amount):
        self.x += amount

    def rerender(self):
        self._renderer.redraw(self._color, self.x,
                              self.y, self.radius)
