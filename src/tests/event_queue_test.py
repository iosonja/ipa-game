import unittest
import pygame
from gameloop import GameLoop
from database_connection import DatabaseConnection
from services.score_tracker import ScoreTracker
from ui.renderer import Renderer
from services.event_queue import EventQueue
from services.symbol_tracker import SymbolTracker


class TestEventQueue(unittest.TestCase):
    def setUp(self):
        window = pygame.display.set_mode((50, 50))
        score_tracker = ScoreTracker(24)
        renderer = Renderer(window, 50, (0, 0, 0))
        self.event_queue = EventQueue()
        symbol_tracker = SymbolTracker()
        db_connection = DatabaseConnection()
        GameLoop(window, 50, renderer, self.event_queue,
                 score_tracker, symbol_tracker, db_connection)

    def test_event_queue_getter_returns_data(self):
        response = self.event_queue.get()
        self.assertNotEqual(response, None)
