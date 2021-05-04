import pygame


class TextDisplayer:
    def __init__(self, window, width):
        self._window = window
        self._width = width

    def draw_info(self):
        info_text = "Try to make the bubble stop before it reaches the right edge."
        font = pygame.font.SysFont('ptmono', 20)
        self._window.blit(font.render(info_text, True, (0, 0, 0)), (210, 460))

    def draw_scores(self, current_score):
        score_text = "Current score: {}".format(current_score)
        font = pygame.font.SysFont('ptmono', 25)
        self._window.blit(font.render(score_text, True, (0, 0, 0)), (10, 10))

    def draw_game_over(self, current_score):
        text1 = "Well done!"
        text2 = "You finished with {} points.".format(current_score)
        font1 = pygame.font.SysFont('ptmono', 35)
        font2 = pygame.font.SysFont('ptmono', 30)
        self._window.blit(font1.render(text1, True, (0, 0, 0)), (500, 200))
        self._window.blit(font2.render(text2, True, (0, 0, 0)), (370, 240))