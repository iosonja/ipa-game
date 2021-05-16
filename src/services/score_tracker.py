class ScoreTracker:
    """This class stores user's scores.

    Attributes:
        current_score (int): current score.
        correct_answers (int): correct answers so far.
        max_correct_answers (int): when this many correct answers have been
        given, the game ends.
    """

    def __init__(self, max_correct_answers):
        self.current_score = 0
        self.correct_answers = 0
        self.max_correct_answers = max_correct_answers

    def log_correct_answer(self):
        """Update object attributes after a symbol has been successfully
        classified.
        """

        if self.game_over():
            return

        self.current_score += 10
        self.correct_answers += 1

    def log_wrong_answer(self):
        """Update object attributes after a symbol has been unsuccessfully
        classified.
        """
        if self.game_over():
            return

        if self.current_score - 2 > 0:
            self.current_score -= 2
        else:
            self.current_score = 0

    def game_over(self):
        """Check if the player has reached the max number of correct answers.

        Returns:
            bool: Maximum number of correct answers has/has not been reached.
        """
        return self.correct_answers >= self.max_correct_answers
