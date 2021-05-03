import unittest
import pygame
from gameloop import GameLoop
from score_tracker import ScoreTracker
from ui.renderer import Renderer
from event_queue import EventQueue


class TestGameLoop(unittest.TestCase):
    def setUp(self):
        window = pygame.display.set_mode((50, 50))
        score_tracker = ScoreTracker(24)
        renderer = Renderer(window, 50, (0, 0, 0), score_tracker)
        event_queue = EventQueue()
        self.gameloop = GameLoop(window, 50, renderer,
                                 event_queue, score_tracker)

    def test_gameloop_exists_after_creation(self):
        self.assertNotEqual(self.gameloop, None)
