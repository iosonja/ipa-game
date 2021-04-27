import unittest
from scores import Scores


class TestButton(unittest.TestCase):
    def setUp(self):
        self.scores = Scores()

    def test_scores_exist_after_creation(self):
        self.assertNotEqual(self.scores, None)

    def test_scores_increase(self):
        self.scores.increase(10)
        self.assertEqual(self.scores.number, 10)

    def test_scores_go_to_zero_when_asked(self):
        self.scores.make_zero
        self.assertEqual(self.scores.number, 0)
