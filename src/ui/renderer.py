import pygame


class Textbox:
    def __init__(self, window):
        self.font = pygame.font.SysFont('Arial', 20)
        self._window = window
        self.rect = pygame.draw.rect(self._window, (0,0,0), (0, 0, 1000, 100), 1)

    def add_text(self):
        text1 = """Welcome! Try to make the bubble stop before it reaches the right edge. In the current version of the game,"""
        text2 = """the stopping can be done by pressing R on your keyboard if the bubble is red, G if green and B if blue."""
        text3 = "You can close the game by pressing X."
        self._window.blit(self.font.render(text1, True, (0,0,0)), (10, 10))
        self._window.blit(self.font.render(text2, True, (0,0,0)), (10, 30))
        self._window.blit(self.font.render(text3, True, (0,0,0)), (10, 50))


class Renderer:
    def __init__(self, window, background_color):
        self._window = window
        self._background_color = background_color

    def redraw(self, bubble_color, x_bubble, y_bubble, bubble_radius):
        self._window.fill(self._background_color)
        pygame.draw.circle(self._window, bubble_color, (x_bubble,
                                                        y_bubble), bubble_radius)
        textbox = Textbox(self._window)
        textbox.add_text()
        pygame.display.update()
