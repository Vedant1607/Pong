from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

# Setup the Game Screen
screen.setup(width=1000, height=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0) # turn off screen updates for smoother animation

# Create Game Objects
left_paddle = Paddle((-480,0))
right_paddle = Paddle((470,0))
ball = Ball()
score = Scoreboard()

# Setup key listeners for paddle movements
screen.listen()
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

# Start game loop
game_running = True

while game_running:
    time.sleep(ball.move_speed) # Control game speed
    screen.update() # Refresh the screen with each loop
    ball.move()
    
    # Detect collision with the wall
    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_y()
    
    # Detect collision with the paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 440 or ball.distance(left_paddle) < 50 and ball.xcor() < - 450:
        ball.bounce_x()
    
    # Detect if right paddle misses
    if ball.xcor() > 490:
        score.left_score_increase()
        ball.reset_position()
    
    # Detect if left paddle misses
    if ball.xcor() < -500:
        score.right_score_increase()
        ball.reset_position()
    
    # Detecting the Winner
    if score.left_score == 7:
        score.goto(0,0)
        score.write("   GAME OVER\nRight Player Won", align="center", font=("Courier", 40, "bold"))
        game_running = False
        
    if score.right_score == 7:
        score.goto(0,0)
        score.write("   GAME OVER\nRight Player Won", align="center", font=("Courier", 40, "bold"))
        game_running = False

screen.exitonclick()