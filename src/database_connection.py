import sqlite3


class DatabaseConnection:
    def __init__(self):
        self._connection = sqlite3.connect("dummy_scores.db")
        self._connection.isolation_level = None

    def add_score(self, nickname, score):
        params = (nickname, score)
        self._connection.execute(
            "INSERT INTO Scores (nickname,score) VALUES (?, ?);", params)
        self._connection.commit()

    def fetch_top_scores(self):
        top_scores = self._connection.execute("SELECT nickname,score FROM Scores ORDER BY score DESC LIMIT 5;").fetchall()
        self._connection.close()
        return top_scores
