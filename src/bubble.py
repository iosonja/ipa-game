class Bubble:
    def __init__(self, x, y, radius, color, renderer):
        self.x_position = x
        self.y_position = y
        self._radius = radius
        self._color = color
        self._renderer = renderer

    def move(self, amount):
        self.x_position += amount

    def rerender(self):
        self._renderer.redraw(self._color, self.x_position, self.y_position, self._radius)