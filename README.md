# Pong Game

This project is a simple Pong game implemented using Python's `turtle` graphics module. The game simulates the classic Pong experience, where two paddles controlled by players aim to prevent a ball from passing them. Scores are displayed at the top, and the game speed increases as the ball bounces between the paddles.

## Game Files

This project includes four main files:

1. **main.py** - Initializes the game screen and manages game logic, such as ball movement, collision detection, and score updates.

2. **paddle.py** - Defines the `Paddle` class for creating paddles that players control. The paddles move up and down when specific keys are pressed.

3. **ball.py** - Defines the `Ball` class, which handles the ball's movement and bounce logic. It manages the ball's speed, direction, and collision with the paddles and walls.

4. **scoreboard.py** - Defines the `Scoreboard` class for displaying and updating the game score. Each time the ball passes a paddle, the opposing player’s score increases.

## Classes Overview

- **Scoreboard**:
    - Manages the display of the left and right player scores at the top of the screen.
    - Increments scores when the opposing player misses the ball.

- **Paddle**:
    - Creates paddles with a specified position.
    - Allows movement up and down based on player inputs.

- **Ball**:
    - Manages the ball’s movement, speed, and bounce behavior.
    - Resets the position when a player misses and gradually increases speed after each bounce.

## How to Run the Game

1. Ensure Python is installed on your machine.
2. Install any necessary packages (e.g., `turtle` is included with standard Python installations).
3. Run the game by executing the following command in the terminal:

   ```bash
   python main.py
   ```

## Game Controls

- **Left Paddle**: Use the "W" key to move up and "S" key to move down.
- **Right Paddle**: Use the "Up Arrow" to move up and "Down Arrow" to move down.

## Game Rules

- Each player controls a paddle to prevent the ball from crossing their side.
- If the ball crosses a player’s side, the opposing player scores a point.
- The first player to score a predefined number of points wins the game (you can set this manually in the code if desired).

## Example Game Flow

1. Run the game, and two paddles appear on the left and right sides of the screen.
2. The ball starts moving automatically.
3. Players control their respective paddles to bounce the ball back.
4. The game displays scores at the top, updating whenever a player scores.
5. The ball resets to the center after each point, and its speed increases with each bounce.

Enjoy the classic Pong experience!
