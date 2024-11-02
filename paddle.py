from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.color("white")
        self.goto(position)
    
    # Move the paddle up by 20 units
    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    
    # Move the paddle down by 20 units
    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)