import pygame


class Button:
    def __init__(self, x, file_path):
        self._starting_x = x
        self.x = x
        self.y = 400
        self.is_being_dragged = False
        self._image = pygame.image.load(file_path)
        self.collision_box = pygame.rect.Rect(x, 400, 200, 50)

    def move_right(self):
        self.x += 1

    def move_left(self):
        self.x -= 1

    def move_up(self):
        self.y += 1

    def move_down(self):
        self.y -= 1

    def get_image(self):
        return self._image

    def update_collision_box(self):
        self.collision_box = pygame.rect.Rect(self.x, self.y, 200, 50)
        # pygame.draw.rect(self._window, (0, 0, 0), self.collision_box, 1)

    def toggle_dragging(self):
        self.is_being_dragged = not self.is_being_dragged

    def return_to_starting_point(self):
        self.x = self._starting_x
        self.y = 400
