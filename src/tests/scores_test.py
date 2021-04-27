import unittest
from scores import Scores


class TestScores(unittest.TestCase):
    def setUp(self):
        self.scores = Scores()

    def test_scores_exist_after_creation(self):
        self.assertNotEqual(self.scores, None)

    def test_scores_increase(self):
        self.scores.increase(10)
        self.assertEqual(self.scores.number, 10)

    def test_scores_decrease_when_not_zero(self):
        self.scores.increase(10)
        self.scores.decrease(2)
        self.assertEqual(self.scores.number, 8)

    def test_scores_dont_go_below_zero(self):
        self.scores.decrease(2)
        self.assertEqual(self.scores.number, 0)
