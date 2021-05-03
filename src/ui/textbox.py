import pygame


class Textbox:
    def __init__(self, window, width, score_tracker):
        self.font = pygame.font.SysFont('Arial', 20)
        self._window = window
        self._width = width
        self._score_tracker = score_tracker
        self.rect = pygame.draw.rect(
            self._window, (0, 0, 0), (0, 410, self._width, 100), 1)

    def add_text(self):
        text1 = """Welcome! Try to make the bubble stop before it reaches the right edge. In the current version of the game, the stopping"""
        text2 = """can be done by pressing R on your keyboard if the bubble is red, G if green, B if blue, W if white and P if pink."""
        text3 = "You can close the game by pressing X."
        score_text = "Current score: {}".format(self._score_tracker.current_score)

        self._window.blit(self.font.render(text1, True, (0, 0, 0)), (10, 420))
        self._window.blit(self.font.render(text2, True, (0, 0, 0)), (10, 440))
        self._window.blit(self.font.render(text3, True, (0, 0, 0)), (10, 460))
        self._window.blit(self.font.render(
            score_text, True, (0, 0, 0)), (10, 10))
