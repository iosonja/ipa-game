import unittest
import pygame
from gameloop import GameLoop
from score_tracker import ScoreTracker
from ui.renderer import Renderer
from event_queue import EventQueue


class TestEventQueue(unittest.TestCase):
    def setUp(self):
        window = pygame.display.set_mode((50, 50))
        score_tracker = ScoreTracker(24)
        renderer = Renderer(window, 50, (0, 0, 0), score_tracker)
        self.event_queue = EventQueue()
        GameLoop(window, 50, renderer, self.event_queue, score_tracker)

    def test_event_queue_getter_returns_data(self):
        response = self.event_queue.get()
        self.assertNotEqual(response, None)
