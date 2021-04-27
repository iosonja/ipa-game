import sys
from random import randrange
import pygame
from ui.bubble import Bubble


class GameLoop:
    def __init__(self, window, window_width, renderer, event_queue):
        self._window = window
        self._window_width = window_width
        self._renderer = renderer
        self._event_queue = event_queue
        self._bubble_is_moving = True

    def start(self):
        colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]

        x_bubble = 0
        y_bubble = 150
        bubble_radius = 50
        bubble_color = colors[randrange(3)]
        velocity = 5

        bubble = Bubble(x_bubble, y_bubble, bubble_radius,
                        bubble_color, self._renderer)

        while True:
            if self._handle_events(bubble) == False:
                break

            pygame.time.delay(100)


            if bubble.x_position >= self._window_width + bubble_radius:
                # The bubble has reached the right end. Some punishment will be
                # added here.

                # Temporary action: Start over
                bubble.move(-(self._screen_width + bubble_radius))

            if self._bubble_is_moving:
                bubble.move(velocity)
                bubble.rerender()

        pygame.quit()

    def _handle_events(self, bubble):
        for event in self._event_queue.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    return False
                elif event.key == bubble.key:
                    self._bubble_is_moving = False
                else:
                    return True
            elif event.type == pygame.QUIT:
                return False