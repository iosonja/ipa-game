import unittest
from services.score_tracker import ScoreTracker


class TestScoreTracker(unittest.TestCase):
    def setUp(self):
        self.score_tracker = ScoreTracker(24)

    def test_score_tracker_exist_after_creation(self):
        self.assertNotEqual(self.score_tracker, None)

    def test_current_score_increases(self):
        self.score_tracker.log_correct_answer()
        self.assertEqual(self.score_tracker.current_score, 10)

    def test_current_score_does_not_increase_after_game_ends(self):
        for i in range(27):
            self.score_tracker.log_correct_answer()
        self.assertEqual(self.score_tracker.current_score, 240)

    def test_current_score_decreases_when_not_zero(self):
        self.score_tracker.log_correct_answer()
        self.score_tracker.log_wrong_answer()
        self.assertEqual(self.score_tracker.current_score, 8)

    def test_current_score_cant_go_below_zero(self):
        self.score_tracker.log_wrong_answer()
        self.assertEqual(self.score_tracker.current_score, 0)

    def test_current_score_does_not_decrease_after_game_ends(self):
        for i in range(24):
            self.score_tracker.log_correct_answer()
        self.score_tracker.log_wrong_answer()
        self.assertEqual(self.score_tracker.current_score, 240)
