import pygame


class Renderer:
    def __init__(self, window, background_color):
        self._window = window
        self._background_color = background_color

    def redraw(self, bubble_color, x_bubble, y_bubble, bubble_radius):
        self._window.fill(self._background_color)
        pygame.draw.circle(self._window, bubble_color, (x_bubble,
                                                        y_bubble), bubble_radius)
        pygame.display.update()
