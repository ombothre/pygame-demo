# Space Wars Game

## Overview
Space Wars is a simple 2D space shooter game built using Python and Pygame. The player controls a spaceship and must shoot down enemies while avoiding collisions.

![game](image.png)

## Installation
1. Ensure you have Python installed on your system.
2. Install Pygame by running:
    ```sh
    pip install pygame
    ```

## How to Play
1. Run the game by executing `main.py`:
    ```sh
    python main.py
    ```
2. Use the left and right arrow keys to move the spaceship.
3. Press the spacebar to shoot bullets.
4. Avoid enemies and shoot them to score points.
5. The game ends if an enemy reaches the bottom of the screen.

## Files
- `main.py`: Contains the main game loop and event handling.
- `objects.py`: Defines the game objects such as Player, Bullet, and Enemy.
- `helpers.py`: Contains helper functions for collision detection, score display, and game initialization.

## Assets
- `assets/images/player.png`: Image for the player's spaceship.
- `assets/images/bullet.png`: Image for the bullet.
- `assets/images/enemy.png`: Image for the enemy.
- `assets/images/background.png`: Background image for the game.
- `assets/audio/laser.wav`: Sound effect for shooting bullets.