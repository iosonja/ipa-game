import sys
import pygame
from elements.bubble import Bubble
from elements.button import Button


class GameLoop:
    """This class if where the game loop happens. There is one bubble at a time
    in the game window: the first one is created in the constructor and the
    next ones are created inside the main loop. The bubble
    is moved forward with each iteration.

    Attributes:
        _window: The window that displays the user interface.
        _window_width: The width of the window = bubble's travel distance.
        _renderer: The renderer object takes care of updating playing view.
        _event_queue: Events are held here prior to being processed.
        _score_tracker: This object tracks the player's score_tracker.
        _symbol_tracker: Temporary database for symbols and their keys.
        _db_connection: Connection to a top scores database.
        _bubble: The bubble that is currently in the playing view.
        _buttons: List of classification buttons' x positions, files and names.
        _active_button: The button that is currently being dragged.
        _answer_toggler: A button that reveals or hides the correct answer.
    """

    def __init__(self, window, window_width, renderer, event_queue,
                 score_tracker, symbol_tracker, db_connection):

        self._window = window
        self._window_width = window_width
        self._renderer = renderer
        self._event_queue = event_queue
        self._score_tracker = score_tracker
        self._symbol_tracker = symbol_tracker
        self._db_connection = db_connection
        self._bubble = Bubble(self._symbol_tracker)
        self._buttons = self._list_buttons()
        self._active_button = self._buttons[0]
        self._answer_toggler = pygame.rect.Rect(1000, 0, 200, 40)

    @staticmethod
    def _list_buttons():
        return [
            Button(20, "affricate", 'src/assets/button_images/affricate.png'),
            Button(260, "approximant", 'src/assets/button_images/approximant.png'),
            Button(500, "fricative", 'src/assets/button_images/fricative.png'),
            Button(740, "nasal", 'src/assets/button_images/nasal.png'),
            Button(980, "plosive", 'src/assets/button_images/plosive.png')
        ]

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
                self._loop_game_over_view()
                continue

            if self._bubble.x >= self._window_width + 50:
                self._bubble = Bubble(self._symbol_tracker)
            self._bubble.move(1)
            self._bubble.update_collision_box()

            for button in self._buttons:
                if button.is_being_dragged:
                    self._handle_drag(button)
                    break

            self._renderer.redraw(self._bubble, self._buttons,
                                  self._score_tracker.current_score,
                                  self._active_button, self._answer_toggler)

            pygame.time.delay(5)

    def _loop_game_over_view(self):
        nickname = ""
        while True:
            for event in self._event_queue.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE and nickname is not None:
                        nickname = nickname[:-1]
                    if event.key == pygame.K_RETURN:
                        self._db_connection.add_score(
                            nickname, self._score_tracker.current_score)
                        self._loop_scores_view()
                    if len(nickname) > 15:
                        continue
                    elif nickname != "":
                        nickname = nickname + event.unicode
                    else:
                        nickname = event.unicode
            self._renderer.show_end_banner(self._score_tracker.current_score)
            self._renderer.display_nickname_field(nickname)

    def _loop_scores_view(self):
        top_scores = self._db_connection.fetch_top_scores()
        self._renderer.reset_view()
        self._renderer.get_text_displayer().draw_top_scores(top_scores)
        pygame.display.update()
        while True:
            for event in self._event_queue.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def _handle_drag(self, button):
        self._active_button = button
        mouse_x, mouse_y = pygame.mouse.get_pos()
        button.x = mouse_x - 50
        button.y = mouse_y - 25
        button.update_collision_box()
        if button.collision_box.colliderect(self._bubble.collision_box):
            self._handle_drag_collision(button)

    def _handle_drag_collision(self, button):
        if button.key == self._bubble.key:
            self._handle_correct_answer()
            return
        button.toggle_dragging()
        pygame.mouse.set_visible(True)
        button.return_to_starting_point()
        self._score_tracker.log_wrong_answer()

    def _handle_correct_answer(self):
        """Do a set of actions when the player answers correctly.
        """

        self._score_tracker.log_correct_answer()
        self._symbol_tracker.correctly_classified(self._bubble.symbol)

        if not self._score_tracker.game_over():
            self._bubble = Bubble(self._symbol_tracker)

    def _click(self):
        for button in self._buttons:
            if button.collision_box.collidepoint(pygame.mouse.get_pos()):
                button.toggle_dragging()
                pygame.mouse.set_visible(False)
                break
        if self._answer_toggler.collidepoint(pygame.mouse.get_pos()):
            self._bubble.toggle_answer_displaying()

    def _release_button(self):
        for button in self._buttons:
            if button.collision_box.collidepoint(pygame.mouse.get_pos()):
                button.toggle_dragging()
                button.return_to_starting_point()
                pygame.mouse.set_visible(True)
                break

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._click()
            elif event.type == pygame.MOUSEBUTTONUP:
                self._release_button()
