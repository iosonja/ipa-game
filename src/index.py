import pygame
from gameloop import GameLoop
from database_connection import DatabaseConnection
from ui.renderer import Renderer
from services.event_queue import EventQueue
from services.score_tracker import ScoreTracker
from services.symbol_tracker import SymbolTracker

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = (212, 220, 255)
symbol_tracker = SymbolTracker()
MAX_CORRECT_ANSWERS = symbol_tracker.get_nbr_of_remaining_symbols()
score_tracker = ScoreTracker(MAX_CORRECT_ANSWERS)
DATABASE_CONNECTION = DatabaseConnection()


def main():
    """This function creates the main components of the game. It initializes
    pygame and starts the game loop.
    """

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("IPA game")

    renderer = Renderer(window, WINDOW_WIDTH, BACKGROUND_COLOR)
    event_queue = EventQueue()
    loop = GameLoop(window, WINDOW_WIDTH, renderer,
                    event_queue, score_tracker, symbol_tracker, DATABASE_CONNECTION)

    pygame.init()
    loop.start()


if __name__ == "__main__":
    main()
