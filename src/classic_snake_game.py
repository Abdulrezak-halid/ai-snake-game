"""
Classic Snake Game
==================
A traditional snake game built with Python's Turtle graphics.
Control the snake with WASD or Arrow keys.

Original concept by @TokyoEdTech
Enhanced and professionally formatted version.
"""

import turtle
import time
import random


class ClassicSnakeGame:
    """
    Classic Snake Game using Turtle graphics.
    
    Features:
    - Keyboard controls (WASD or Arrow keys)
    - Score and high score tracking
    - Collision detection with walls and self
    - Progressive difficulty (speed increases)
    """
    
    def __init__(self):
        """Initialize the game components."""
        self.delay = 0.1
        self.score = 0
        self.high_score = 0
        self.is_paused = False
        self.segments = []
        
        # Set up the screen
        self.screen = turtle.Screen()
        self._setup_screen()
        
        # Create game objects
        self.head = self._create_snake_head()
        self.food = self._create_food()
        self.pen = self._create_scoreboard()
        
        # Bind keyboard controls
        self._setup_controls()
        
    def _setup_screen(self):
        """Configure the game window."""
        self.screen.title("Classic Snake Game")
        self.screen.bgcolor("#2C3E50")  # Dark blue-gray
        self.screen.setup(width=600, height=600)
        self.screen.tracer(0)  # Turn off automatic screen updates
        
        # Draw border
        border = turtle.Turtle()
        border.speed(0)
        border.penup()
        border.hideturtle()
        border.pencolor("#ECF0F1")
        border.pensize(3)
        border.goto(-290, -290)
        border.pendown()
        for _ in range(4):
            border.forward(580)
            border.left(90)
    
    def _create_snake_head(self):
        """Create and return the snake's head."""
        head = turtle.Turtle()
        head.speed(0)
        head.shape("square")
        head.color("#27AE60")  # Green
        head.penup()
        head.goto(0, 0)
        head.direction = "stop"
        return head
    
    def _create_food(self):
        """Create and return the food object."""
        food = turtle.Turtle()
        food.speed(0)
        food.shape("circle")
        food.color("#E74C3C")  # Red
        food.penup()
        food.goto(0, 100)
        return food
    
    def _create_scoreboard(self):
        """Create and return the scoreboard."""
        pen = turtle.Turtle()
        pen.speed(0)
        pen.shape("square")
        pen.color("#ECF0F1")  # Light gray
        pen.penup()
        pen.hideturtle()
        pen.goto(0, 260)
        pen.write("Score: 0  High Score: 0", 
                  align="center", 
                  font=("Arial", 20, "bold"))
        return pen
    
    def _setup_controls(self):
        """Set up keyboard bindings."""
        self.screen.listen()
        
        # WASD controls
        self.screen.onkeypress(self.go_up, "w")
        self.screen.onkeypress(self.go_down, "s")
        self.screen.onkeypress(self.go_left, "a")
        self.screen.onkeypress(self.go_right, "d")
        
        # Arrow key controls
        self.screen.onkeypress(self.go_up, "Up")
        self.screen.onkeypress(self.go_down, "Down")
        self.screen.onkeypress(self.go_left, "Left")
        self.screen.onkeypress(self.go_right, "Right")
        
        # Pause control
        self.screen.onkeypress(self.toggle_pause, "p")
        self.screen.onkeypress(self.toggle_pause, "space")
    
    def go_up(self):
        """Change direction to up if not moving down."""
        if self.head.direction != "down":
            self.head.direction = "up"
    
    def go_down(self):
        """Change direction to down if not moving up."""
        if self.head.direction != "up":
            self.head.direction = "down"
    
    def go_left(self):
        """Change direction to left if not moving right."""
        if self.head.direction != "right":
            self.head.direction = "left"
    
    def go_right(self):
        """Change direction to right if not moving left."""
        if self.head.direction != "left":
            self.head.direction = "right"
    
    def toggle_pause(self):
        """Toggle game pause state."""
        self.is_paused = not self.is_paused
    
    def move(self):
        """Move the snake head based on current direction."""
        step = 20
        
        if self.head.direction == "up":
            self.head.sety(self.head.ycor() + step)
        elif self.head.direction == "down":
            self.head.sety(self.head.ycor() - step)
        elif self.head.direction == "left":
            self.head.setx(self.head.xcor() - step)
        elif self.head.direction == "right":
            self.head.setx(self.head.xcor() + step)
    
    def update_scoreboard(self):
        """Update the score display."""
        self.pen.clear()
        self.pen.write(f"Score: {self.score}  High Score: {self.high_score}", 
                       align="center", 
                       font=("Arial", 20, "bold"))
    
    def spawn_food(self):
        """Move food to a random location."""
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        self.food.goto(x, y)
    
    def add_segment(self):
        """Add a new segment to the snake's body."""
        segment = turtle.Turtle()
        segment.speed(0)
        segment.shape("square")
        segment.color("#1ABC9C")  # Teal
        segment.penup()
        self.segments.append(segment)
    
    def move_segments(self):
        """Move body segments to follow the head."""
        # Move segments in reverse order
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)
        
        # Move first segment to head's position
        if self.segments:
            self.segments[0].goto(self.head.xcor(), self.head.ycor())
    
    def check_wall_collision(self):
        """Check if snake hit the wall."""
        x, y = self.head.xcor(), self.head.ycor()
        return abs(x) > 290 or abs(y) > 290
    
    def check_self_collision(self):
        """Check if snake hit itself."""
        for segment in self.segments:
            if segment.distance(self.head) < 20:
                return True
        return False
    
    def reset_game(self):
        """Reset game state after collision."""
        time.sleep(0.5)
        self.head.goto(0, 0)
        self.head.direction = "stop"
        
        # Hide and remove segments
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        
        # Update high score
        if self.score > self.high_score:
            self.high_score = self.score
        
        # Reset score and speed
        self.score = 0
        self.delay = 0.1
        
        self.update_scoreboard()
    
    def run(self):
        """Main game loop."""
        print("=" * 50)
        print("     CLASSIC SNAKE GAME")
        print("=" * 50)
        print("Controls:")
        print("  - WASD or Arrow Keys to move")
        print("  - P or Space to pause")
        print("  - Close window to quit")
        print("=" * 50)
        
        try:
            while True:
                self.screen.update()
                
                if self.is_paused:
                    time.sleep(0.1)
                    continue
                
                # Check wall collision
                if self.check_wall_collision():
                    self.reset_game()
                
                # Check food collision
                if self.head.distance(self.food) < 20:
                    self.spawn_food()
                    self.add_segment()
                    self.score += 10
                    
                    # Increase speed slightly
                    if self.delay > 0.05:
                        self.delay -= 0.002
                    
                    if self.score > self.high_score:
                        self.high_score = self.score
                    
                    self.update_scoreboard()
                
                # Move body segments
                self.move_segments()
                
                # Move head
                self.move()
                
                # Check self collision
                if self.check_self_collision():
                    self.reset_game()
                
                time.sleep(self.delay)
                
        except turtle.Terminator:
            pass  # Window was closed
        
        print(f"\nGame Over! Final High Score: {self.high_score}")


def main():
    """Main entry point."""
    game = ClassicSnakeGame()
    game.run()


if __name__ == "__main__":
    main()
