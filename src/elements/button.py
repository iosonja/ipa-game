import pygame


class Button:
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
        self.collision_box = pygame.rect.Rect(self.x, self.y, 200, 50)

    def toggle_dragging(self):
        self.is_being_dragged = not self.is_being_dragged

    def return_to_starting_point(self):
        self.x = self._starting_x
        self.y = self._starting_y
