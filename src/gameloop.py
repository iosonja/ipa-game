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
        _bubble: The bubble that is currently in the playing view.
    """

    def __init__(self, window, window_width, renderer, event_queue, score_tracker, symbol_tracker):
        """Constructor for creating a new game loop.

        Args:
            window (pygame.Surface): User interface display.
            window_width (int): Each bubble's distance from start to finish.
            renderer (Renderer): Renderer takes care of updating playing view.
            event_queue (EventQueue): Events are held here before processing.
            score_tracker (ScoreTracker): This tracks scores & correct answers.
        """

        self._window = window
        self._window_width = window_width
        self._renderer = renderer
        self._event_queue = event_queue
        self._score_tracker = score_tracker
        self._symbol_tracker = symbol_tracker
        self._bubble = Bubble(self._symbol_tracker)

    def start(self):
        """This method contains the main loop. It repeatedly calls for
        _handle_events() to check whether or not to continue looping. It moves
        the current bubble's position forward with each iteration, unless the
        bubble has reach the right edge. In that case it creates a new bubble
        and places it to the left side of the window. After the main loop has
        been exited, the method quits pygame.
        """

        velocity = 3

        while True:
            self._handle_events()

            if self._bubble.x >= self._window_width + 50:
                self._bubble = Bubble(self._symbol_tracker)

            pygame.time.delay(60)
            self._bubble.move(velocity)
            self._renderer.redraw(self._bubble)

        pygame.quit()
        sys.exit()

    def _handle_correct_answer(self):
        self._score_tracker.log_correct_answer()
        self._symbol_tracker.correctly_classified(self._bubble.symbol)

        if not self._score_tracker.game_over():
            self._bubble = Bubble(self._symbol_tracker)

    def _handle_events(self):
        """This method chooses an action based on user input until game's over.
        """

        if self._score_tracker.game_over():
            pygame.quit()
            sys.exit()

        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == self._bubble.key:
                    self._handle_correct_answer()

                self._score_tracker.log_wrong_answer()
