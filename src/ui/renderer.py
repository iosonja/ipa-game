import pygame
from ui.text_displayer import TextDisplayer


class Renderer:
    """Renderer takes care of updating the game view according to any events.
    """

    def __init__(self, window, window_width, background_color):
        self._window = window
        self._window_width = window_width
        self._background_color = background_color
        self._text_displayer = TextDisplayer(self._window)

    def redraw(self, bubble, buttons, score, active_button, answer_button):
        """Update the playing view when the game is still on.

        Attributes:
            bubble (Bubble): The bubble that is currently displayed on screen.
        """

        self._window.fill(self._background_color)
        self._window.blit(bubble.symbol_image, (bubble.x, bubble.y))
        self._text_displayer.draw_scores(score)
        for button in buttons:
            self._window.blit(button.get_image(), (button.x, button.y))
            button.update_collision_box()
        self._window.blit(active_button.get_image(),
                          (active_button.x, active_button.y))
        self._show_answer_element(bubble, answer_button)

        pygame.display.update()

    def show_end_banner(self, score):
        """Display the Game Over -view.
        """

        self._window.fill(self._background_color)
        self._text_displayer.draw_game_over(score)

    def display_nickname_field(self, nickname):
        input_rect = pygame.Rect(500, 250, 200, 30)
        pygame.draw.rect(self._window, (0, 0, 0), input_rect, 1)
        self._text_displayer.draw_nickname(nickname)
        pygame.display.update()

    def _show_answer_element(self, bubble, answer_button):
        pygame.draw.rect(self._window, (0, 0, 0), answer_button, 1)
        if bubble.display_answer:
            self._text_displayer.reveal_answer(bubble.key)
        else:
            self._text_displayer.draw_answer_text()