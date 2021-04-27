import pygame
from ui.bubble import Bubble


class GameLoop:
    def __init__(self, window, window_width, renderer, event_queue, scores):
        self._window = window
        self._window_width = window_width
        self._renderer = renderer
        self._event_queue = event_queue
        self._bubble = Bubble(self._renderer)
        self._scores = scores

    def start(self):
        velocity = 5

        while True:
            if self._handle_events() is False:
                break
            if self._bubble.x >= self._window_width + self._bubble.radius:
                self._bubble = Bubble(self._renderer)

            pygame.time.delay(60)
            self._bubble.move(velocity)
            self._bubble.rerender()

        pygame.quit()

    def _handle_events(self):
        for event in self._event_queue.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    return False
                if event.key == self._bubble.key:
                    self._scores.increase(10)
                    self._bubble = Bubble(self._renderer)
                    return True

                self._scores.decrease(1)
                return True

            if event.type == pygame.QUIT:
                return False

            return True
