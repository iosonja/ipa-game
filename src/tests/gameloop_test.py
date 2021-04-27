import unittest
import pygame
from gameloop import GameLoop
from scores import Scores
from ui.renderer import Renderer
from event_queue import EventQueue


class TestGameLoop(unittest.TestCase):
    def setUp(self):
        window = pygame.display.set_mode((50, 50))
        scores = Scores()
        renderer = Renderer(window, 50, (0, 0, 0), scores)
        event_queue = EventQueue()
        self.gameloop = GameLoop(window, 50, renderer, event_queue, scores)

    def test_gameloop_exists_after_creation(self):
        self.assertNotEqual(self.gameloop, None)
