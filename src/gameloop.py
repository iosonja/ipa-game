
import sys
import pygame


class GameLoop:
    def __init__(self, window, screen_width, renderer):
        self._window = window
        self._screen_width = screen_width
        self._renderer = renderer

    def start(self):
        x_bubble = 0
        y_bubble = 150
        bubble_radius = 25
        bubble_color = (144, 122, 214)
        velocity = 5

        while True:
            pygame.time.delay(100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()  # Better that just exit() bc no dialogue created

            #  keys = pygame.key.get_pressed()

            x_bubble += velocity

            if x_bubble >= self._screen_width + bubble_radius:
                # The bubble has reached the right end. Some punishment will be added here.
                pygame.quit()  # Remove this later

            self._renderer.redraw(bubble_color, x_bubble,
                                  y_bubble, bubble_radius)

        pygame.quit()
