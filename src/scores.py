class Scores:
    def __init__(self):
        self.number = 0

    def increase(self, amount):
        self.number += amount

    def decrease(self, amount):
        self.number -= amount

    def make_zero(self):
        self.number = 0
