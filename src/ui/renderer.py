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

        self._button_image = pygame.image.load(
            'src/assets/button_images/affricate.png')
        self._button_x = 10
        self._button_y = 400
        self._collision_box = pygame.rect.Rect(
            self._button_x, self._button_y, 200, 50)

    def redraw(self, bubble, buttons, score):
        """Update the playing view when the game is still on.

        Attributes:
            bubble (Bubble): The bubble that is currently displayed on screen.
        """

        self._window.fill(self._background_color)
        self._window.blit(bubble.symbol_image, (bubble.x, bubble.y))
        pygame.draw.line(self._window, (0, 0, 0),
                         (0, 450), (self._window_width, 450), 1)
        self._text_displayer.draw_info()
        self._text_displayer.draw_scores(score)
        for button in buttons:
            self._window.blit(button.get_image(), (button.x, button.y))
            button.update_collision_box()
        pygame.display.update()

    def show_end_banner(self, score):
        """Display the Game Over -view.
        """

        self._window.fill(self._background_color)
        self._text_displayer.draw_game_over(score)
        pygame.display.update()

    def handle_dragging(self, button):
        if button.collision_box.collidepoint(pygame.mouse.get_pos()):
            mouse_x, mouse_y = pygame.mouse.get_pos()
            button.x = mouse_x - 50
            button.y = mouse_y - 25

    def return_button_to_starting_point(self):
        button.x = 10
        button.y = 400
