import pygame


class Button:
    """This class holds information of a draggable button.

    Attributes:
        _starting_x: X-coordinate in the beginning.
        x: Current X-coordinate.
        _starting_y:Y-coordinate in the beginning.
        y: Current Y-coordinate.
        key: The button's class, e.g. affricate. Also the text on button image.
        is_being_dragged: Boolean stating if the button is being dragged.
        _image: The image to be displayed on the window in button's place.
        collision_box: A rectangle area that is used for checking if the button
        is touching a bubble.
    """

    def __init__(self, x, key, file_path):
        self._starting_x = x
        self.x = x
        self._starting_y = 448
        self.y = self._starting_y
        self.key = key
        self.is_being_dragged = False
        self._image = pygame.image.load(file_path)
        self.collision_box = pygame.rect.Rect(x, self._starting_y, 200, 50)

    def get_image(self):
        return self._image

    def update_collision_box(self):
        """This method is called whenever the button moves. Move the collision
        box so that it's always where the button is.
        """

        self.collision_box = pygame.rect.Rect(self.x, self.y, 200, 50)

    def toggle_dragging(self):
        """This method is called when mouse has been clicked or released over
        the button's collision box.
        """

        self.is_being_dragged = not self.is_being_dragged

    def return_to_starting_point(self):
        """The button's position is reset here after mouse release or wrong
        answer.
        """

        self.x = self._starting_x
        self.y = self._starting_y
