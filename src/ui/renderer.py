import pygame
from ui.text_displayer import TextDisplayer


class Renderer:
    """Renderer takes care of updating the game view according to any events.

    Attributes:
        _window: The window that displays the user interface.
        _window_width: The width of the window = bubble's travel distance.
        _background_color: The base color of the UI window.
        _text_displayer: An object that takes care of rendering text.
        _answer_toggler: An area that either reveals or hides the correct
        answer.
    """

    def __init__(self, window, window_width, background_color):
        self._window = window
        self._window_width = window_width
        self._background_color = background_color
        self._text_displayer = TextDisplayer(self._window)
        self._answer_area = pygame.rect.Rect(1000, 0, 200, 40)

    def get_answer_area(self):
        return self._answer_area

    def reset_view(self):
        """Cover everything in the window with the background color.
        """

        self._window.fill(self._background_color)

    def redraw(self, bubble, buttons, score, active_button):
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
        self._show_answer_element(bubble)

        pygame.display.update()

    def show_end_banner(self, score):
        """Display the Game Over -view.
        """

        self._window.fill(self._background_color)
        self._text_displayer.draw_game_over(score)

    def display_nickname_field(self, nickname):
        """Render the nickname section, call text displayer to render the texts.

        Args:
            nickname (str): The currently typed version of a nickname. The
            ready version of which will be inserted in the scores database.
        """

        input_rect = pygame.Rect(500, 280, 200, 30)
        pygame.draw.rect(self._window, (0, 0, 0), input_rect, 1)
        self._text_displayer.draw_nickname(nickname)
        pygame.display.update()

    def _show_answer_element(self, bubble):
        """Render a rectangle in the top right corner. Depending on the state
        of bubble's reveal_answer attribute, ask text displayer to show
        either bubble's key or a static text.


        Args:
            bubble (Bubble): The bubble that's currently in the window.
        """

        pygame.draw.rect(self._window, (0, 0, 0), self._answer_area, 1)
        if bubble.display_answer:
            text = bubble.key
        else:
            text = "Show the answer"
        self._text_displayer.draw_answer_text(text)

    def show_top_scores(self, top_scores):
        """Prepare the top scores -view

        Args:
            top_scores (list): List of five tuples containing nicknames and scores.
        """
        self.reset_view()
        self._text_displayer.draw_top_scores(top_scores)
        pygame.display.update()
