import pygame


class Textbox:
    def __init__(self, window, width, score_tracker):
        self.score_font = pygame.font.SysFont('ptmono', 25)
        self.info_font = pygame.font.SysFont('ptmono', 20)
        self._window = window
        self._width = width
        self._score_tracker = score_tracker
        pygame.draw.line(self._window, (0, 0, 0),
                         (0, 450), (self._width, 450), 1)

    def add_text(self):
        text1 = "Try to make the bubble stop before it reaches the right edge."
        score_text = "Current score: {}".format(
            self._score_tracker.current_score)

        self._window.blit(self.score_font.render(
            score_text, True, (0, 0, 0)), (10, 10))
        self._window.blit(self.info_font.render(
            text1, True, (0, 0, 0)), (210, 460))
