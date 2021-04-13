class Button:
    def __init__(self, x, y, isBeingDragged):
        self.x = x
        self.y = y
        self.isBeingDragged = isBeingDragged
    
    def move_right(self):
        self.x += 1

    def move_left(self):
        self.x -= 1

    def move_up(self):
        self.y += 1

    def move_down(self):
        self.y -= 1

    def toggle_dragging(self):
        self.isBeingDragged = not self.isBeingDragged