"""
AI Snake Game - Hand Tracking Edition
=====================================
A modern snake game controlled by hand gestures using computer vision.
Uses OpenCV and MediaPipe for real-time hand tracking.

Author: Abdulrezak Halit
Project: Mathematics Software Final Project
"""

import math
import random
import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
from pathlib import Path


class SnakeGame:
    """
    A snake game class that uses hand tracking for control.
    
    The snake follows the player's index finger position detected through
    the webcam using MediaPipe hand detection.
    """
    
    def __init__(self, food_image_path: str):
        """
        Initialize the snake game.
        
        Args:
            food_image_path: Path to the food/apple image file
        """
        # Snake body tracking
        self.points = []  # All points of the snake body
        self.lengths = []  # Length between each point
        self.current_length = 0  # Total current length of snake
        self.allowed_length = 100  # Maximum allowed length
        self.previous_head = (0, 0)  # Previous head position
        
        # Food/Apple setup
        self.food_image = cv2.imread(food_image_path, cv2.IMREAD_UNCHANGED)
        if self.food_image is None:
            # Create a simple red circle as fallback if image not found
            self.food_image = self._create_default_food()
        else:
            self.food_image = cv2.resize(self.food_image, (50, 50))
        
        self.food_height, self.food_width = self.food_image.shape[:2]
        self.food_position = (0, 0)
        self.randomize_food_location()
        
        # Game state
        self.score = 0
        self.high_score = 0
        self.game_over = False
        
    def _create_default_food(self):
        """Create a default red circle as food if image is not found."""
        import numpy as np
        food = np.zeros((50, 50, 4), dtype=np.uint8)
        cv2.circle(food, (25, 25), 20, (0, 0, 255, 255), -1)
        return food
    
    def randomize_food_location(self):
        """Place food at a random location on the screen."""
        self.food_position = (
            random.randint(100, 700),
            random.randint(100, 500)
        )
    
    def reset_game(self):
        """Reset the game state for a new game."""
        self.points = []
        self.lengths = []
        self.current_length = 0
        self.allowed_length = 100
        self.previous_head = (0, 0)
        
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.game_over = False
        self.randomize_food_location()
    
    def check_collision(self, point):
        """
        Check if the snake head collides with its body.
        
        Args:
            point: Current head position (x, y)
            
        Returns:
            bool: True if collision detected
        """
        px, py = point
        # Check collision with body (skip recent points to avoid false positives)
        if len(self.points) > 50:
            for i, body_point in enumerate(self.points[:-50]):
                bx, by = body_point
                distance = math.hypot(px - bx, py - by)
                if distance < 15:
                    return True
        return False
    
    def update(self, main_image, current_head):
        """
        Update game state and render the frame.
        
        Args:
            main_image: The camera frame to draw on
            current_head: Current position of snake head (x, y)
            
        Returns:
            Updated image with game graphics
        """
        if self.game_over:
            return self._render_game_over(main_image)
        
        px, py = self.previous_head
        cx, cy = current_head
        
        # Add new point to snake body
        self.points.append([cx, cy])
        distance = math.hypot(cx - px, cy - py)
        self.lengths.append(distance)
        self.current_length += distance
        self.previous_head = (cx, cy)
        
        # Trim snake length if too long
        self._trim_snake_length()
        
        # Check food collision
        self._check_food_collision(cx, cy)
        
        # Check self collision
        if self.check_collision(current_head):
            self.game_over = True
            return self._render_game_over(main_image)
        
        # Render the game
        main_image = self._render_snake(main_image)
        main_image = self._render_food(main_image)
        main_image = self._render_ui(main_image)
        
        return main_image
    
    def _trim_snake_length(self):
        """Remove excess length from the snake tail."""
        while self.current_length > self.allowed_length and self.lengths:
            self.current_length -= self.lengths[0]
            self.lengths.pop(0)
            self.points.pop(0)
    
    def _check_food_collision(self, cx, cy):
        """Check if snake head touches the food."""
        rx, ry = self.food_position
        half_width = self.food_width // 2
        half_height = self.food_height // 2
        
        if (rx - half_width < cx < rx + half_width and 
            ry - half_height < cy < ry + half_height):
            self.randomize_food_location()
            self.allowed_length += 30
            self.score += 1
    
    def _render_snake(self, image):
        """Draw the snake on the image."""
        if not self.points:
            return image
            
        # Draw snake body
        for i in range(1, len(self.points)):
            # Gradient color effect for snake body
            intensity = int(255 * (i / len(self.points)))
            color = (0, intensity, 255 - intensity)
            cv2.line(image, tuple(self.points[i-1]), tuple(self.points[i]), color, 20)
        
        # Draw snake head
        if self.points:
            cv2.circle(image, tuple(self.points[-1]), 22, (50, 50, 200), cv2.FILLED)
            cv2.circle(image, tuple(self.points[-1]), 18, (100, 0, 255), cv2.FILLED)
        
        return image
    
    def _render_food(self, image):
        """Draw the food on the image."""
        rx, ry = self.food_position
        half_width = self.food_width // 2
        half_height = self.food_height // 2
        
        try:
            image = cvzone.overlayPNG(image, self.food_image, 
                                       (rx - half_width, ry - half_height))
        except Exception:
            # Fallback: draw a simple circle
            cv2.circle(image, (rx, ry), 20, (0, 0, 255), cv2.FILLED)
        
        return image
    
    def _render_ui(self, image):
        """Draw the UI elements (score, high score)."""
        # Semi-transparent background for score
        overlay = image.copy()
        cv2.rectangle(overlay, (30, 15), (250, 80), (0, 0, 0), cv2.FILLED)
        cv2.addWeighted(overlay, 0.5, image, 0.5, 0, image)
        
        # Score text
        cv2.putText(image, f"Score: {self.score}", (40, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.putText(image, f"Best: {self.high_score}", (40, 75), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 1)
        
        return image
    
    def _render_game_over(self, image):
        """Render the game over screen."""
        # Dark overlay
        overlay = image.copy()
        cv2.rectangle(overlay, (0, 0), (image.shape[1], image.shape[0]), 
                      (0, 0, 0), cv2.FILLED)
        cv2.addWeighted(overlay, 0.7, image, 0.3, 0, image)
        
        # Game over text
        cv2.putText(image, "GAME OVER", (200, 250), 
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 4)
        cv2.putText(image, f"Final Score: {self.score}", (250, 320), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(image, f"High Score: {self.high_score}", (260, 360), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)
        cv2.putText(image, "Press 'R' to Restart | 'Q' to Quit", (150, 420), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200, 200, 200), 2)
        
        return image


def main():
    """Main function to run the AI Snake Game."""
    # Initialize camera
    cap = cv2.VideoCapture(0)
    cap.set(3, 800)  # Width
    cap.set(4, 600)  # Height
    
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return
    
    # Initialize hand detector
    detector = HandDetector(detectionCon=0.7, maxHands=1)
    
    # Get the path to assets folder
    script_dir = Path(__file__).parent.parent
    food_path = str(script_dir / "assets" / "apple.png")
    
    # Fallback to current directory
    if not Path(food_path).exists():
        food_path = str(script_dir / "apple.png")
    
    # Initialize game
    game = SnakeGame(food_path)
    
    print("=" * 50)
    print("  AI SNAKE GAME - Hand Tracking Edition")
    print("=" * 50)
    print("Controls:")
    print("  - Move your index finger to control the snake")
    print("  - Eat the apples to grow and score points")
    print("  - Avoid hitting your own body!")
    print("  - Press 'R' to restart after game over")
    print("  - Press 'Q' to quit")
    print("=" * 50)
    
    while True:
        success, img = cap.read()
        if not success:
            print("Error: Failed to capture frame.")
            break
            
        # Flip image horizontally for mirror effect
        img = cv2.flip(img, 1)
        
        # Detect hands
        hands, img = detector.findHands(img, flipType=False)
        
        if hands:
            # Get index finger tip position
            landmark_list = hands[0]['lmList']
            index_finger_tip = landmark_list[8][0:2]
            img = game.update(img, index_finger_tip)
        else:
            # Show instructions when no hand detected
            if not game.game_over:
                cv2.putText(img, "Show your hand to play!", (200, 300), 
                           cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
        # Display the frame
        cv2.imshow("AI Snake Game - Hand Tracking", img)
        
        # Handle key presses
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q') or key == ord('Q'):
            break
        elif key == ord('r') or key == ord('R'):
            game.reset_game()
    
    # Cleanup
    cap.release()
    cv2.destroyAllWindows()
    
    print(f"\nThanks for playing! Final High Score: {game.high_score}")


if __name__ == "__main__":
    main()
