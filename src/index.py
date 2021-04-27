import pygame
from ui.renderer import Renderer
from ui.gameloop import GameLoop

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 500
BACKGROUND_COLOR = (212, 220, 255)


def main():
    pygame.init()
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("IPA game")

    renderer = Renderer(window, BACKGROUND_COLOR)
    loop = GameLoop(window, SCREEN_WIDTH, renderer)

    loop.start()


if __name__ == "__main__":
    main()
