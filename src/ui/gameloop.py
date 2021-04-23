import sys
from random import randrange
import pygame
from ui.bubble import Bubble


class GameLoop:
    def __init__(self, window, screen_width, renderer):
        self._window = window
        self._screen_width = screen_width
        self._renderer = renderer

    def start(self):
        symbols = ["f", "v", "θ", "ð", "z", "ʃ", "ʒ", "h", "p", "b", "t",
                   "d", "k", "g", "ʈʃ", "dʒ", "m", "n", "ŋ", "r", "j", "w", "l", "ɫ"]
        classes = {
            "fricative": ["f", "v", "θ", "ð", "z", "ʃ", "ʒ", "h"],
            "plosive": ["p", "b", "t", "d", "k", "g"],
            "affricate": ["ʈʃ", "dʒ"],
            "nasal": ["m", "n", "ŋ"],
            "approximant": ["r", "j", "w", "l", "ɫ"]
        }

        colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

        x_bubble = 0
        y_bubble = 150
        bubble_radius = 25
        bubble_color = colors[randrange(3)]
        velocity = 5
        bubble_is_moving = True

        bubble = Bubble(x_bubble, y_bubble, bubble_radius,
                        bubble_color, self._renderer)

        while True:
            pygame.time.delay(100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()  # Better that just exit() bc no dialogue created

            keys = pygame.key.get_pressed()

            if keys[pygame.K_x]:
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            # practice function: bubble stops when classified correctly
            elif keys[bubble.key]:
                bubble_is_moving = False

            if bubble.x_position >= self._screen_width + bubble_radius:
                # The bubble has reached the right end. Some punishment will be
                # added here.
                # Start over
                bubble.move(-(self._screen_width + bubble_radius))

            if bubble_is_moving:
                bubble.move(velocity)
                bubble.rerender()

        pygame.quit()
