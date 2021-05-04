import pygame


class TextDisplayer:
    """This class takes care of drawing text elements on the game view.

    Attributes:
        _window: The window to draw on.
    """

    def __init__(self, window):
        self._window = window

    def draw_info(self):
        """Draw a short info text to the bottom of the game view.
        """

        info_text = "Try to make the bubble stop before it reaches the right edge."
        font = pygame.font.SysFont('ptmono', 20)
        self._window.blit(font.render(info_text, True, (0, 0, 0)), (210, 460))

    def draw_scores(self, current_score):
        """Draw score tracker to the top left corner of the game view.
        """

        score_text = "Current score: {}".format(current_score)
        font = pygame.font.SysFont('ptmono', 25)
        self._window.blit(font.render(score_text, True, (0, 0, 0)), (10, 10))

    def draw_game_over(self, current_score):
        """Draw the end text and final score
        """

        text1 = "Well done!"
        text2 = "You finished with {} points.".format(current_score)
        font1 = pygame.font.SysFont('ptmono', 35)
        font2 = pygame.font.SysFont('ptmono', 30)
        self._window.blit(font1.render(text1, True, (0, 0, 0)), (500, 200))
        self._window.blit(font2.render(text2, True, (0, 0, 0)), (370, 240))
