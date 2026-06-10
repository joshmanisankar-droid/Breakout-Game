# 🧱 Breakout Game

A classic Breakout arcade game built using Python's Turtle graphics module and Object-Oriented Programming principles.

The player controls a paddle at the bottom of the screen and must bounce the ball to destroy all the bricks without letting the ball fall below the paddle.

---

## 🎮 Features

- Smooth paddle movement
- Ball collision physics
- Multiple rows of colored bricks
- Score tracking system
- Win screen
- Game over screen
- Object-Oriented Design

---

## 📸 Gameplay

### Objective

Destroy all bricks by bouncing the ball using the paddle.

Avoid letting the ball fall below the paddle.

---

## 🛠️ Built With

- Python 3
- Turtle Graphics
- Object-Oriented Programming (OOP)

---

## 📂 Project Structure

```text
Breakout/
│
├── main.py
├── player.py
├── ball.py
├── bricks.py
├── scoreboard.py
├── README.md
└── .gitignore
```

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/breakout-game.git
cd breakout-game
```

### Run the Game

```bash
python main.py
```

---

## 🎮 Controls

| Key | Action |
|------|---------|
| ← Left Arrow | Move Paddle Left |
| → Right Arrow | Move Paddle Right |

---

## 🏗️ OOP Design

### Player Class

Responsible for:

- Creating the paddle
- Moving left
- Moving right

### Ball Class

Responsible for:

- Ball movement
- Wall collisions
- Paddle collisions
- Direction changes

### Brick Class

Responsible for:

- Creating individual bricks
- Brick positioning

### Scoreboard Class

Responsible for:

- Displaying score
- Updating score
- Showing win message
- Showing game over message

---

## 📊 Scoring System

Each destroyed brick awards:

```text
+1 Point
```

The score is displayed at the top of the screen.

---

## 🏆 Win Condition

The player wins when:

```text
All bricks are destroyed.
```

---

## ❌ Game Over

The game ends when:

```text
The ball falls below the paddle.
```

---

## 📚 Concepts Practiced

- Classes and Objects
- Inheritance
- Constructors (`__init__`)
- Lists of Objects
- Collision Detection
- Event Handling
- Game Loops
- Screen Updates
- Encapsulation
- Turtle Graphics

---

## 🔮 Future Improvements

- Multiple Levels
- Lives System
- Increasing Ball Speed
- Sound Effects
- High Score Saving
- Power-Ups
- Different Brick Strengths
- Pause Menu
- Start Screen

---

## 👨‍💻 Author

Josh Mani Sankar

Built as part of my Python development journey and the 100 Days of Code Python Bootcamp.

---

## ⭐ Lessons Learned

This project provided hands-on experience with:

- Game development fundamentals
- Object-oriented programming
- Real-time collision detection
- Managing multiple objects on screen
- Designing maintainable Python applications
