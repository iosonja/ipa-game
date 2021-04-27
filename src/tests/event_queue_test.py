import unittest
import pygame
from  gameloop import GameLoop
from scores import Scores
from ui.renderer import Renderer
from event_queue import EventQueue

class TestEventQueue(unittest.TestCase):
    def setUp(self):
        window = pygame.display.set_mode((50, 50))
        scores = Scores()
        renderer = Renderer(window, 50, (0, 0, 0), scores)
        self.event_queue = EventQueue()
        GameLoop(window, 50, renderer, self.event_queue, scores)

    def test_event_queue_getter_returns_data(self):
        response = self.event_queue.get()
        self.assertNotEqual(response, None)