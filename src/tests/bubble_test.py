import unittest
import pygame
from elements.bubble import Bubble
from services.symbol_tracker import SymbolTracker


class TestBubble(unittest.TestCase):
    def setUp(self):
        symbol_tracker = SymbolTracker()
        self.bubble = Bubble(symbol_tracker)

    def test_bubble_collision_box_is_updated(self):
        self.bubble.x = 80
        self.bubble.y = 80
        self.bubble.update_collision_box()
        self.assertEqual(self.bubble.collision_box, pygame.rect.Rect(
            self.bubble.x, self.bubble.y, 100, 100))

    def test_bubble_moves_in_x_dimension(self):
        self.bubble.move(57)
        self.assertEqual(self.bubble.x, 7)

    def test_bubble_does_not_move_in_y_direction(self):
        original_y = self.bubble.y
        self.bubble.move(57)
        self.assertEqual(self.bubble.y, original_y)

    def test_display_answer_can_be_toggled(self):
        original_value = self.bubble.display_answer
        self.bubble.toggle_answer_displaying()
        self.assertNotEqual(self.bubble.display_answer, original_value)
