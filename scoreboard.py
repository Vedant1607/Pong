from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.left_score = 0
        self.right_score = 0
        self.penup()
        self.hideturtle()
        self.update_score()
    
    # Update the scoreboard display with the current scores
    def update_score(self):
        self.clear() # clears the previous score
        self.goto(-200, 280)
        self.write(self.left_score, align="center", font=("Courier", 80, "normal"))
        self.goto(200, 280)
        self.write(self.right_score, align="center", font=("Courier", 80, "normal"))
    
    # Increase the left player's score by 1 and update the display
    def left_score_increase(self):
        self.left_score += 1
        self.update_score()
    
    # Increase the right player's score by 1 and update the display
    def right_score_increase(self):
        self.right_score += 1
        self.update_score()