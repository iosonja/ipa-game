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
        symbols = {'src/assets/affricate0.png': pygame.K_a,
                   'src/assets/approximant0.png': pygame.K_m,
                   'src/assets/fricative0.png': pygame.K_f,
                   'src/assets/nasal0.png': pygame.K_n,
                   'src/assets/plosive0.png': pygame.K_p}

        self.x = -50  # half of an image's width
        self.y = randrange(80, 300)  # make bubbles appear from random heights
        self.symbol = list(symbols.keys())[randrange(5)]
        self.key = symbols.get(self.symbol)
        self.symbol_image = pygame.image.load(self.symbol)
        self._renderer = renderer

        # The following doesn't work, it prints everything after game has ended
        print("New bubble was created, press {} to make a new one!".format(
            chr(self.key).upper()))

    def move(self, amount):
        """Move the bubble

        Args:
            amount (int): how much and to which direction the bubble moves
        """
        self.x += amount
