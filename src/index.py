import pygame
from ui.renderer import Renderer
from gameloop import GameLoop
from event_queue import EventQueue

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = (212, 220, 255)


def main():
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("IPA game")

    renderer = Renderer(window, BACKGROUND_COLOR)
    event_queue = EventQueue()
    loop = GameLoop(window, WINDOW_WIDTH, renderer, event_queue)

    pygame.init()
    loop.start()


if __name__ == "__main__":
    main()
