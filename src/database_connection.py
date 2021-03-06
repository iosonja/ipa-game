import sqlite3
from config import DATABASE_FILENAME


class DatabaseConnection:
    """This class is responsible for interacting with the scores database.
    """

    def __init__(self):
        self._connection = sqlite3.connect(DATABASE_FILENAME)
        self._connection.isolation_level = None

    def add_score(self, nickname, score):
        """Write a new score result in the scores database.

        Args:
            nickname (str): The player name that the score is associated with.
            score (int): New score number.
        """

        try:
            params = (nickname, score)
            self._connection.execute(
                "INSERT INTO Scores (nickname,score) VALUES (?, ?);", params)
            self._connection.commit()
        except:
            print("An error occurred when inserting data")

    def fetch_top_scores(self):
        """Fetch five results with the biggest scores from the database.

        Returns:
            list: list containing 5 tuples with nickname and score in them.
        """

        try:
            top_scores = self._connection.execute(
                "SELECT nickname,score FROM Scores ORDER BY score DESC LIMIT 5;"
            ).fetchall()
            return top_scores
        except:
            print("An error occurred when fetching score data")
            return None

    def close_connection(self):
        self._connection.close()
