import unittest
import pygame
from elements.button import Button


class TestButton(unittest.TestCase):
    def setUp(self):
        self.button = Button(
            20, "affricate", 'src/assets/button_images/affricate.png')

    def test_image_is_loaded_and_returned(self):
        image = self.button.get_image()
        self.assertNotEqual(image, None)

    def test_button_collision_box_is_updated(self):
        self.button.x = 80
        self.button.y = 80
        self.button.update_collision_box()
        self.assertEqual(self.button.collision_box,
                         pygame.rect.Rect(self.button.x, self.button.y, 200, 50))

    def test_dragging_can_be_toggled(self):
        original_value = self.button.is_being_dragged
        self.button.toggle_dragging()
        self.assertNotEqual(self.button.is_being_dragged, original_value)

    def test_button_returns_to_starting_point(self):
        self.button.x = 80
        self.button.y = 80
        self.button.return_to_starting_point()
        self.assertNotEqual((self.button.x, self.button.y), (80, 80))
