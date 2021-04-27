import pygame
from ui.textbox import Textbox


class Renderer:
    def __init__(self, window, width, background_color, scores):
        self._window = window
        self._width = width
        self._background_color = background_color
        self._scores = scores

    def redraw(self, bubble_color, x_bubble, y_bubble, bubble_radius):
        self._window.fill(self._background_color)
        pygame.draw.circle(self._window, bubble_color, (x_bubble,
                                                        y_bubble), bubble_radius)
        textbox = Textbox(self._window, self._width, self._scores)
        textbox.add_text()
        pygame.display.update()
