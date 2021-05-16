from random import randrange
import pygame


class Bubble:
    """This class contains information of a bubble moving through the game view.

    Attributes:
        x: Current X-coordinate.
        y: Current Y-coordinate.
        symbol: Path to the image file where the symbol is depicted.
        symbol_image: Surface data of the symbol image.
        key: The name of the class the symbol is a member of.
        collision_box: A rectangle area that is used for checking if the bubble
        is touching a button.
        display_answer: A boolean determining whether the bubble's key should
        be displayed on the screen.
    """

    def __init__(self, symbol_tracker):
        self.x = -50  # half of an image's width
        self.y = randrange(80, 300)  # make bubbles appear from random heights
        self.symbol = symbol_tracker.give_random_symbol_file()
        self.symbol_image = pygame.image.load(self.symbol)
        self.key = symbol_tracker.give_key()
        self.collision_box = pygame.rect.Rect(self.x, self.y, 100, 100)
        self.display_answer = False

    def update_collision_box(self):
        """This method is called whenever the bubble moves. Move the collision
        box so that it's always where the bubble is.
        """

        self.collision_box = pygame.rect.Rect(self.x, self.y, 100, 100)

    def move(self, amount):
        """Move the bubble

        Args:
            amount (int): how much and to which direction the bubble moves
        """

        self.x += amount

    def toggle_answer_displaying(self):
        """Reveal or hide the bubble's key.
        """

        self.display_answer = not self.display_answer
