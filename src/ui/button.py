class Button:
     def __init__(self, x, y, is_being_dragged):
         self.x = x
         self.y = y
         self.is_being_dragged = is_being_dragged

     def move_right(self):
         self.x += 1

     def move_left(self):
         self.x -= 1

     def move_up(self):
         self.y += 1

     def move_down(self):
         self.y -= 1

     def toggle_dragging(self):
         self.is_being_dragged = not self.is_being_dragged