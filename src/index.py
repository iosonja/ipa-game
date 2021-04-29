import pygame
from ui.renderer import Renderer
from gameloop import GameLoop
from event_queue import EventQueue
from scores import Scores

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = (212, 220, 255)
scores = Scores()


def main():
    """This function creates the window, renderer, event queue and game loop.
    It initializes pygame and starts the game loop.
    """
    
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("IPA game")

    renderer = Renderer(window, WINDOW_WIDTH, BACKGROUND_COLOR, scores)
    event_queue = EventQueue()
    loop = GameLoop(window, WINDOW_WIDTH, renderer, event_queue, scores)

    pygame.init()
    loop.start()


if __name__ == "__main__":
    main()
