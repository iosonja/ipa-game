class Scores:
    def __init__(self):
        self.number = 0

    def increase(self, amount):
        self.number += amount

    def decrease(self, amount):
        if self.number - amount > 0:
            self.number -= amount
        else:
            self.number = 0
