# 🐍 Snake Game Collection

A collection of two snake games built with Python - featuring both a **hand-tracking AI version** using computer vision and a **classic keyboard-controlled version**.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📋 Table of Contents

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

## ✨ Features

### AI Snake Game
- 🖐️ **Hand Tracking Control** - Control the snake with your index finger using webcam
- 🎯 **Real-time Computer Vision** - Powered by MediaPipe and OpenCV
- 🔄 **Game Over & Restart** - Full game cycle with restart capability
- 📊 **Score Tracking** - Current score and high score display
- 🎨 **Modern UI** - Gradient snake colors and smooth graphics

### Classic Snake Game
- ⌨️ **Keyboard Controls** - WASD or Arrow keys
- ⏸️ **Pause Feature** - Press P or Space to pause
- 🏆 **High Score System** - Track your best performance
- 🎮 **Progressive Difficulty** - Speed increases as you grow
- 🖼️ **Clean Graphics** - Modern color scheme with Turtle graphics

## 🎬 Demo

### AI Snake Game
Control the snake by moving your hand in front of your webcam. Your index finger becomes the snake's head!

### Classic Snake Game
Navigate the snake using keyboard controls to eat food and grow longer without hitting the walls or yourself.

## 🚀 Installation

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

## 📖 Usage


### Run AI Snake Game (Hand Tracking)

```bash
python src/ai_snake_game.py
```

### Run Classic Snake Game

```bash
python src/classic_snake_game.py
```

## 📁 Project Structure

```
AI_Snake_Game/
├── src/
│   ├── __init__.py           # Package initialization
│   ├── ai_snake_game.py      # Hand tracking snake game
│   └── classic_snake_game.py # Keyboard controlled snake game
├── assets/
│   └── apple.png             # Food image for AI game
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── LICENSE                   # MIT License
```

## 🎮 Games

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

## 🎯 Controls

### AI Snake Game
| Action | Control |
|--------|---------|
| Move Snake | Move index finger |
| Restart | Press `R` |
| Quit | Press `Q` |

### Classic Snake Game
| Action | Control |
|--------|---------|
| Move Up | `W` or `↑` |
| Move Down | `S` or `↓` |
| Move Left | `A` or `←` |
| Move Right | `D` or `→` |
| Pause | `P` or `Space` |

## 📦 Requirements

```
opencv-python>=4.5.0
cvzone>=1.5.0
mediapipe>=0.8.0
numpy>=1.21.0
```

For the classic game, only Python's built-in `turtle` module is required.

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 👤 Author

**ABD ALRAZAK KHALED**
- Project: Mathematics Software Final Project

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  Made with ❤️ and Python
</p>
