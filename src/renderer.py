import pygame


class Renderer:
    def __init__(self, window, width, background_color):
        self._WINDOW = window
        self._SCREEN_WIDTH = width
        self._BACKGROUND_COLOR = background_color

    def redraw(self, x_bubble, y_bubble, radius):
            self._WINDOW.fill(self._BACKGROUND_COLOR)
            pygame.draw.circle(self._WINDOW, (144, 122, 214), (x_bubble,
                            y_bubble), radius)
            pygame.display.update()