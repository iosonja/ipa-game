import pygame
from ui.text_displayer import TextDisplayer


class Renderer:
    """Renderer takes care of updating the game view according to any events.
    """

    def __init__(self, window, width, background_color):
        self._window = window
        self._width = width
        self._background_color = background_color
        self._text_displayer = TextDisplayer(self._window)

        self._buttonwidth = 90
        self._buttonheight = 30
        self._rectangle_x = 175
        self._rectangle_y = 134
        self._rectangle = pygame.rect.Rect(self._rectangle_x, self._rectangle_y, self._buttonwidth, self._buttonheight)


    def redraw(self, bubble, score):
        """Update the playing view when the game is still on.

        Attributes:
            bubble (Bubble): The bubble that is currently displayed on screen.
        """

        self._window.fill(self._background_color)
        self._window.blit(bubble.symbol_image, (bubble.x, bubble.y))
        pygame.draw.line(self._window, (0, 0, 0),
                         (0, 450), (self._width, 450), 1)
        self._text_displayer.draw_info()
        self._text_displayer.draw_scores(score)
        pygame.draw.rect(self._window, (0, 0, 0), self._rectangle)
        pygame.display.update()

    def show_end_banner(self, score):
        """Display the Game Over -view.
        """

        self._window.fill(self._background_color)
        self._text_displayer.draw_game_over(score)
        pygame.display.update()

    def handle_dragging(self):
        if self._rectangle.collidepoint(pygame.mouse.get_pos()):
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self._rectangle_x = mouse_x - self._buttonwidth / 2
            self._rectangle_y = mouse_y - self._buttonheight / 2
            print(self._rectangle_x, self._rectangle_y)
            self._rectangle = pygame.rect.Rect(self._rectangle_x, self._rectangle_y, self._buttonwidth, self._buttonheight)