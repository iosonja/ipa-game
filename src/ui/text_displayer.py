import pygame


class TextDisplayer:
    """This class takes care of drawing text elements on the game view.

    Attributes:
        _window: The window that displays the user interface.
        _typeface: The typeface that will be used in all texts. Font varies.
    """

    def __init__(self, window):
        self._window = window
        self._typeface = 'ptmono'

    def draw_scores(self, current_score):
        """Draw score tracker to the top left corner of the game view.

        Args:
            current_score (int): The score to be drawn.
        """

        score_text = "Current score: {}".format(current_score)
        font = pygame.font.SysFont(self._typeface, 25)
        self._window.blit(font.render(score_text, True, (0, 0, 0)), (10, 10))

    def draw_game_over(self, current_score):
        """Draw the end text and final score.

        Args:
            current_score (int): The final score to be drawn.
        """

        text1 = "Well done!"
        text2 = "You finished with {} points.".format(current_score)
        font1 = pygame.font.SysFont(self._typeface, 35)
        font2 = pygame.font.SysFont(self._typeface, 30)
        self._window.blit(font1.render(text1, True, (0, 0, 0)), (500, 140))
        self._window.blit(font2.render(text2, True, (0, 0, 0)), (370, 180))

    def draw_nickname(self, nickname):
        """Draw instructions and nickname.

        Args:
            nickname (str): current version of nickname
        """

        text = "Enter nickname:"
        font = pygame.font.SysFont(self._typeface, 20)
        self._window.blit(font.render(text, True, (0, 0, 0)), (510, 251))
        self._window.blit(font.render(nickname, True, (0, 0, 0)), (502, 281))

    def draw_answer_text(self, text):
        """Draw text in the answer displaying area.

        Args:
            text (str): Either static text or the correct answer.
        """

        font = pygame.font.SysFont(self._typeface, 20)
        self._window.blit(font.render(text, True, (0, 0, 0)), (1005, 5))

    def draw_top_scores(self, scores):
        """Draw title and 5 top scores.

        Args:
            scores (list): List of five tuples containing nicknames and scores.
        """

        font = pygame.font.SysFont(self._typeface, 30)
        self._window.blit(font.render(
            "Top Scores", True, (0, 0, 0)), (500, 150))
        for i in range(5):
            name_string = str(i + 1) + " " + scores[i][0]
            score_string = str(scores[i][1]) + " points"
            self._window.blit(font.render(name_string, True,
                              (0, 0, 0)), (310, (200 + (i * 30))))
            self._window.blit(font.render(score_string, True,
                              (0, 0, 0)), (630, (200 + (i * 30))))
