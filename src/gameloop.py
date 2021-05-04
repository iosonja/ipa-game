import sys
import pygame
from bubble import Bubble


class GameLoop:
    """This class if where the main loop of the game happens. There is one
    bubble at a time in the game window: the first one is created in the
    constructor and the next ones are created inside the main loop. The bubble
    is moved forward with each iteration.

    Attributes:
        _window: The window that displays the user interface.
        _window_width: The width of the window = bubble's travel distance.
        _renderer: The renderer object takes care of updating playing view.
        _event_queue: Events are held here prior to being processed.
        _score_tracker: This object tracks the player's score_tracker.
        _symbol_tracker: Temporary database for symbols and their keys.
        _bubble: The bubble that is currently in the playing view.
    """

    def __init__(self, window, window_width, renderer, event_queue,
                 score_tracker, symbol_tracker):

        self._window = window
        self._window_width = window_width
        self._renderer = renderer
        self._event_queue = event_queue
        self._score_tracker = score_tracker
        self._symbol_tracker = symbol_tracker
        self._bubble = Bubble(self._symbol_tracker)

    def start(self):
        """This method contains the main loop. It repeatedly calls for
        _handle_events() to react to user input. It moves the current bubble's
        position forward with each iteration, unless the bubble has reached the
        right edge. In that case it creates a new bubble and places it to the
        left side of the window.
        """

        while True:
            self._handle_events()

            if self._score_tracker.game_over():
                self._renderer.show_end_banner(
                    self._score_tracker.current_score)
            else:
                if self._bubble.x >= self._window_width + 50:
                    self._bubble = Bubble(self._symbol_tracker)
                self._bubble.move(1)
                self._renderer.redraw(
                    self._bubble, self._score_tracker.current_score)

            pygame.time.delay(20)

    def _handle_correct_answer(self):
        """Do a set of actions when the player answers correctly.
        """

        self._score_tracker.log_correct_answer()
        self._symbol_tracker.correctly_classified(self._bubble.symbol)

        if not self._score_tracker.game_over():
            self._bubble = Bubble(self._symbol_tracker)

    def _handle_events(self):
        """Choose an action based on user input.
        """

        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == self._bubble.key:
                    self._handle_correct_answer()

                self._score_tracker.log_wrong_answer()
