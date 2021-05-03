from random import randrange
import pygame


class Bubble:
    """This class contains information of a bubble moving through the game view.

    Attributes:
        radius: Radius of the bubble.
        x: Current X-coordinate.
        y: Current y-coordinate.
        _color: The bubble's color.
        key: The letter key that depends on color, needed for classification.
        _renderer: Renderer takes care of updating playing view.
    """

    def __init__(self, renderer):
        self.radius = 50
        self.x = -self.radius
        self.y = randrange(80, 300)  # make bubbles appear from random heights
        self._color = self.colors_list()[randrange(5)]
        self.key = self.define_key(self._color)
        self._renderer = renderer
        print("New bubble was initialized")

    def colors_list(self):
        """This method makes a list of RGB color codes.

        Returns:
            list: RGB color codes
        """

        red = (255, 0, 0)
        green = (0, 255, 0)
        blue = (0, 0, 255)
        white = (255, 255, 255)
        pink = (255, 0, 255)

        colors = [red, green, blue, white, pink]
        return colors

    def define_key(self, color):
        """This method defines the key that corresponds to the bubble's color.

        Args:
            color (tuple): the bubble's RGB color code

        Returns:
            int: key that corresponds to the bubble's color
        """

        # TODO: Change the color codes to natural language later (e.g. with a dict)
        if color == (255, 0, 0):
            return pygame.K_r
        elif color == (0, 255, 0):
            return pygame.K_g
        elif color == (0, 0, 255):
            return pygame.K_b
        elif color == (255, 255, 255):
            return pygame.K_w
        else:
            return pygame.K_p

    def move(self, amount):
        """Move the bubble

        Args:
            amount (int): how much and to which direction the bubble moves
        """
        self.x += amount

    def rerender(self):
        """Call the renderer to update game view.
        """
        self._renderer.redraw(self._color, self.x,
                              self.y, self.radius)
