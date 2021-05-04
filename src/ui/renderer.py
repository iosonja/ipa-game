import pygame
from ui.text_displayer import TextDisplayer


class Renderer:
    """Renderer takes care of updating the game view according to any events.
    """

    def __init__(self, window, width, background_color, score_tracker):
        self._window = window
        self._width = width
        self._background_color = background_color
        self._score_tracker = score_tracker
        self._text_displayer = TextDisplayer(self._window, self._width)

    def redraw(self, bubble):
        """Update the playing view when the game is still on.

        Attributes:
            bubble (Bubble): The bubble that is currently displayed on screen.
        """

        self._window.fill(self._background_color)
        self._window.blit(bubble.symbol_image, (bubble.x, bubble.y))
        pygame.draw.line(self._window, (0, 0, 0),
                         (0, 450), (self._width, 450), 1)
        self._text_displayer.draw_info()
        self._text_displayer.draw_scores(self._score_tracker.current_score)
        pygame.display.update()

    def show_end_banner(self):
        """Display the Game Over -view.
        """

        self._window.fill(self._background_color)
        self._text_displayer.draw_game_over(self._score_tracker.current_score)
        pygame.display.update()
