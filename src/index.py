import pygame
from ui.renderer import Renderer
from services.symbol_tracker import SymbolTracker
from gameloop import GameLoop
from services.event_queue import EventQueue
from services.score_tracker import ScoreTracker

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = (212, 220, 255)
symbol_tracker = SymbolTracker()
MAX_CORRECT_ANSWERS = symbol_tracker.get_nbr_of_remaining_symbols()
score_tracker = ScoreTracker(MAX_CORRECT_ANSWERS)


def main():
    """This function creates the main components of the game. It initializes
    pygame and starts the game loop.
    """

    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("IPA game")

    renderer = Renderer(window, WINDOW_WIDTH, BACKGROUND_COLOR, score_tracker)
    event_queue = EventQueue()
    loop = GameLoop(window, WINDOW_WIDTH, renderer,
                    event_queue, score_tracker, symbol_tracker)

    pygame.init()
    loop.start()


if __name__ == "__main__":
    main()
