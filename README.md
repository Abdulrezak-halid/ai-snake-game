# 🐍 Snake Game Collection

A collection of two snake games built with Python - featuring both a **hand-tracking AI version** using computer vision and a **classic keyboard-controlled version**.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Table of Contents

- [Features](#-features)
- [Demo](#-demo)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Games](#-games)
  - [AI Snake Game](#ai-snake-game---hand-tracking-edition)
  - [Classic Snake Game](#classic-snake-game)
- [Controls](#-controls)
- [Requirements](#-requirements)
- [Contributing](#-contributing)
- [Author](#-author)
- [License](#-license)

## Features

### AI Snake Game
-  **Hand Tracking Control** - Control the snake with your index finger using webcam
-  **Real-time Computer Vision** - Powered by MediaPipe and OpenCV
-  **Game Over & Restart** - Full game cycle with restart capability
-  **Score Tracking** - Current score and high score display
-  **Modern UI** - Gradient snake colors and smooth graphics

### Classic Snake Game
-  **Keyboard Controls** - WASD or Arrow keys
-  **Pause Feature** - Press P or Space to pause
-  **High Score System** - Track your best performance
-  **Progressive Difficulty** - Speed increases as you grow
-  **Clean Graphics** - Modern color scheme with Turtle graphics

## Demo

### AI Snake Game
Control the snake by moving your hand in front of your webcam. Your index finger becomes the snake's head!

### Classic Snake Game
Navigate the snake using keyboard controls to eat food and grow longer without hitting the walls or yourself.

## Installation

### Prerequisites
- Python 3.8 or higher
- Webcam (for AI Snake Game)
- pip package manager

### Clone the Repository

```bash
git clone https://github.com/Abdulrezak-halid/ai-snake-game.git
cd ai-snake-game
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage


### Run AI Snake Game (Hand Tracking)

```bash
python src/ai_snake_game.py
```

### Run Classic Snake Game

```bash
python src/classic_snake_game.py
```

## Games

### AI Snake Game - Hand Tracking Edition

A modern take on the classic snake game using computer vision for control.

**How it works:**
1. The webcam captures your hand movements
2. MediaPipe detects your hand and tracks the index finger
3. The snake follows your finger position in real-time
4. Eat apples to grow and score points
5. Avoid hitting your own body!

**Technology Stack:**
- OpenCV for video capture and rendering
- MediaPipe for hand detection
- cvzone for utility functions

### Classic Snake Game

The traditional snake game everyone knows and loves.

**How it works:**
1. Control the snake using keyboard input
2. Navigate to eat food items
3. Each food eaten makes the snake longer
4. Avoid walls and your own tail
5. Game speeds up as you progress

**Technology Stack:**
- Python Turtle graphics
- Built-in Python libraries only

## Controls

### AI Snake Game
| Action | Control |
|--------|---------|
| Move Snake | Move index finger |
| Restart | Press `R` |
| Quit | Press `Q` |

### 📸 Screenshot
<img width="963" height="618" alt="Screenshot from 2025-12-14 15-17-40" src="https://github.com/user-attachments/assets/f8fc1f6a-55eb-4ef1-8b1c-a15f6883dd99" />

### Classic Snake Game
| Action | Control |
|--------|---------|
| Move Up | `W` or `↑` |
| Move Down | `S` or `↓` |
| Move Left | `A` or `←` |
| Move Right | `D` or `→` |
| Pause | `P` or `Space` |

### 📸 Screenshot
<img width="604" height="639" alt="Screenshot from 2025-12-14 15-17-08" src="https://github.com/user-attachments/assets/ba754853-d556-4389-8431-299e4d4c0e0a" />

## Requirements

```
opencv-python>=4.5.0
cvzone>=1.5.0
mediapipe>=0.8.0
numpy>=1.21.0
```

For the classic game, only Python's built-in `turtle` module is required.

## Author

**ABD ALRAZAK KHALED**
- Project: Mathematics Software Final Project

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
