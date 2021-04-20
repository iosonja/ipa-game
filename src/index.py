import pygame
from gameloop import GameLoop

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500

def main():
    pygame.init()
    WINDOW = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("IPA game")

    loop = GameLoop(WINDOW, SCREEN_WIDTH)

    loop.start()


if __name__ == "__main__":
    main()