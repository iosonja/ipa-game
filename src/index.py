import pygame
from gameloop import GameLoop
from database_connection import DatabaseConnection
from ui.renderer import Renderer
from services.event_queue import EventQueue
from services.score_tracker import ScoreTracker
from services.symbol_tracker import SymbolTracker


def main():
    """This function creates the main components of the game. It initializes
    pygame and starts the game loop.
    """

    window_width = 1200
    window_height = 500
    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("IPA game")

    background_color = (212, 220, 255)
    renderer = Renderer(window, window_width, background_color)

    database_connection = DatabaseConnection()
    event_queue = EventQueue()
    symbol_tracker = SymbolTracker()
    score_tracker = ScoreTracker(symbol_tracker.get_nbr_of_remaining_symbols())

    gameloop = GameLoop(window, window_width, renderer,
                        event_queue, score_tracker, symbol_tracker, database_connection)

    pygame.init()
    gameloop.start()


if __name__ == "__main__":
    main()
