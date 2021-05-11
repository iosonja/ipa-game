from random import randrange
import pygame


class Bubble:
    """This class contains information of a bubble moving through the game view.

    Attributes:
        x: Current X-coordinate.
        y: Current y-coordinate.
        symbol: Path to a file where the symbol is depicted
        key: The letter key that depends on the symbol, needed for classification.
        symbol_image: Surface data of the symbol image.
        _renderer: Renderer takes care of updating playing view.
    """

    def __init__(self, symbol_tracker):
        self.x = -50  # half of an image's width
        self.y = randrange(80, 300)  # make bubbles appear from random heights
        self.symbol = symbol_tracker.give_random_symbol_file()
        self.key = symbol_tracker.give_key()
        self.symbol_image = pygame.image.load(self.symbol)

        # The following doesn't work, it prints everything after game has ended
        print("New bubble was created, press {} to make a new one!".format(
            chr(self.key).upper()))

    def move(self, amount):
        """Move the bubble

        Args:
            amount (int): how much and to which direction the bubble moves
        """
        self.x += amount
