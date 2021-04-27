import sys
import pygame
from ui.bubble import Bubble


class GameLoop:
    def __init__(self, window, window_width, renderer, event_queue):
        self._window = window
        self._window_width = window_width
        self._renderer = renderer
        self._event_queue = event_queue
        self._bubble = Bubble(self._renderer)

    def start(self):
        velocity = 5

        while True:
            if self._handle_events(self._bubble) == False:
                break

            pygame.time.delay(60)

            if self._bubble.x >= self._window_width + self._bubble.radius:
                self._bubble = Bubble(self._renderer)

            if self._bubble.is_moving:
                self._bubble.move(velocity)
                self._bubble.rerender()

        pygame.quit()

    def _handle_events(self, bubble):
        for event in self._event_queue.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    return False
                elif event.key == self._bubble.key:
                    self._bubble.toggle_movement()
                else:
                    return True
            elif event.type == pygame.QUIT:
                return False
