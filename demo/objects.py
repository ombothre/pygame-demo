import random
from pygame import image, mixer, Surface

class Player:
    """
    Class representing the player (ship) that the user controls.
    """

    def __init__(self, screen: Surface):
        """
        Initializes the Player object with the screen to draw on and the player's image.
        """
        self.screen = screen
        self.img = image.load('assets/images/player.png')  # Load the player image.
        self.x = 370  # Initial x-coordinate of the player.
        self.y = 480  # Initial y-coordinate of the player.
        self.x_change = 0  # No movement initially.

    def move(self, direction: str):
        """
        Moves the player left or right based on the direction passed.
        """
        self.x_change = -5 if direction == 'left' else 5  # Move left by -5, right by 5.

    def stop_move(self):
        """Stops the player's movement by setting x_change to 0."""
        self.x_change = 0

    def update(self):
        """
        Updates the player's position based on x_change, ensuring the player stays within screen bounds.
        """
        self.x += self.x_change  # Update the player's x position based on movement.
        # Keep the player within the screen's horizontal bounds (0 to 736).
        self.x = max(0, min(self.x, 736))

    def draw(self):
        """Draws the player image at the current position on the screen."""
        self.screen.blit(self.img, (self.x, self.y))


class Bullet:
    """
    Class representing the player's bullet.
    """

    def __init__(self, screen: Surface):
        """
        Initializes the Bullet object with the screen to draw on and the bullet image.
        """
        self.screen = screen
        self.img = image.load('assets/images/bullet.png')  # Load the bullet image.
        self.x = 0  # Initial x-coordinate of the bullet (starts off-screen).
        self.y = 480  # Initial y-coordinate of the bullet (aligned with the player).
        self.y_change = 10  # The speed at which the bullet moves upwards.
        self.state = "ready"  # The bullet is not fired initially.
        self.sound = mixer.Sound("assets/audio/laser.wav")  # Sound for firing the bullet.

    def fire(self, player_x: int):
        """
        Fires the bullet from the player's current position.

        Args:
            player_x (int): The x-coordinate of the player (where the bullet should spawn).
        """
        if self.state == "ready":  # The bullet can only be fired if it's in the "ready" state.
            self.state = "fire"  # Change the state to "fire" to indicate the bullet has been fired.
            self.x = player_x  # Set the bullet's x-coordinate to the player's current x-coordinate.
            self.sound.play()  # Play the firing sound.

    def update(self):
        """
        Updates the bullet's position (moves it upwards). If the bullet goes off-screen, it resets.
        """
        if self.state == "fire":
            self.y -= self.y_change  # Move the bullet upwards.
            if self.y <= 0:  # If the bullet goes above the screen (y <= 0), reset it.
                self.reset()

    def reset(self):
        """Resets the bullet's position to the initial state (ready to be fired again)."""
        self.y = 480  # Reset the bullet's y-coordinate to the player's starting position.
        self.state = "ready"  # Set the state back to "ready" to allow another shot.

    def draw(self):
        """
        Draws the bullet on the screen if it is in the "fire" state (meaning it has been fired).
        """
        if self.state == "fire":
            self.screen.blit(self.img, (self.x + 16, self.y + 10))  # Draw the bullet image at the current position.


class Enemy:
    """
    Class representing an enemy that the player needs to avoid or destroy.
    """

    def __init__(self, screen: Surface):
        """
        Initializes the Enemy object with the screen to draw on and the enemy image.
        """
        self.screen = screen
        self.img = image.load('assets/images/enemy.png')  # Load the enemy image.
        self.x = random.randint(0, 736)  # Random x-coordinate for the enemy within screen bounds.
        self.y = random.randint(50, 150)  # Random y-coordinate for the enemy within the top section.
        self.x_change = 4  # Speed at which the enemy moves horizontally.
        self.y_change = 40  # Speed at which the enemy moves vertically down when it reaches screen edge.

    def move(self):
        """
        Moves the enemy horizontally across the screen. When it hits the edge, it changes direction
        and moves downwards.
        """
        self.x += self.x_change  # Update the enemy's x-coordinate.
        if self.x <= 0 or self.x >= 736:  # If the enemy reaches the screen boundaries, reverse horizontal direction.
            self.x_change *= -1
            self.y += self.y_change  # Move the enemy downwards when it hits a boundary.

    def draw(self):
        """Draws the enemy image at the current position on the screen."""
        self.screen.blit(self.img, (self.x, self.y))
