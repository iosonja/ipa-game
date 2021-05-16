import unittest
from database_connection import DatabaseConnection


class TestDatabaseConnection(unittest.TestCase):
    def setUp(self):
        self.db = DatabaseConnection()

    def test_new_score_is_added(self):
        original_result = self.db.fetch_top_scores()
        self.db.add_score("testname", 98)
        new_result = self.db.fetch_top_scores()
        self.assertNotEqual(new_result, original_result)

    def test_scores_are_fetched(self):
        result = self.db.fetch_top_scores()
        self.assertNotEqual(result, None)

    def test_connection_can_be_closed(self):
        self.db.close_connection()
        result = self.db.fetch_top_scores()
        self.assertEqual(result, None)
