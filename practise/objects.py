import random
from pygame import image, mixer, Surface

class Player:
    def __init__(self, screen: Surface):
        """Initialize the player with screen, image, and position."""
        # Add code here

    def move(self, direction: str):
        """Move the player left or right based on direction."""
        # Add code here

    def stop_move(self):
        """Stop the player's movement."""
        # Add code here

    def update(self):
        """Update the player's position."""
        # Add code here

    def draw(self):
        """Draw the player on the screen."""
        # Add code here

class Bullet:
    def __init__(self, screen: Surface):
        """Initialize the bullet with screen, image, and position."""
        # Add code here

    def fire(self, player_x: int):
        """Fire the bullet from the player's position."""
        # Add code here

    def update(self):
        """Update the bullet's position."""
        # Add code here

    def reset(self):
        """Reset the bullet to the initial state."""
        # Add code here

    def draw(self):
        """Draw the bullet on the screen."""
        # Add code here

class Enemy:
    def __init__(self, screen: Surface):
        """Initialize the enemy with screen, image, and position."""
        # Add code here

    def move(self):
        """Move the enemy and change direction if needed."""
        # Add code here

    def draw(self):
        """Draw the enemy on the screen."""
        # Add code here