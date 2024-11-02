from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1 # Initial speed of the ball
    
    # Move the ball by updating its x and y coordinates
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    
    # Bounce the ball by reversing the y direction
    def bounce_y(self):
        self.y_move *= -1 # Reverse the y movement direction
    
    # Bounce the ball by reversing the x direction and increasing speed due to collision
    def bounce_x(self):
        self.x_move *= -1 # Reverse the x movement direction
        self.move_speed *= 0.9 # Increase the speed slightly by reducing delay
    
    # Reset the ball to the center and restart movement in the opposite x direction
    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()