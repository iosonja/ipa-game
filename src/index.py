import pygame
from renderer import Renderer
from gameloop import GameLoop

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
BACKGROUND_COLOR = (212, 220, 255)


def main():
    pygame.init()
    WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("IPA game")

    RENDERER = Renderer(WINDOW, SCREEN_WIDTH, BACKGROUND_COLOR)
    loop = GameLoop(WINDOW, SCREEN_WIDTH, RENDERER)

    loop.start()


if __name__ == "__main__":
    main()
