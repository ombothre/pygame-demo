import pygame
import random, time
from objects import Player, Bullet, Enemy
from helpers import check_collision, game_init

"""
Main game loop.

This script demonstrates a very basic shooting game where:
- A player can move left and right to shoot bullets at falling enemies.
- The player earns points for every enemy hit.
- The game ends when an enemy reaches the bottom of the screen.

This version removes certain game mechanics and focuses on player input, object updates, and collision handling.

"""

# Game initialization
screen, background = game_init()  # Initialize the game screen and background image.

# Game objects
player = Player(screen)  # Create the player object.
bullet = Bullet(screen)  # Create the bullet object.
enemies = [Enemy(screen) for _ in range(6)]  # Create a list of 6 enemies.

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Exit the game if the player closes the window.
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.move('left')  # Move the player left if the left arrow key is pressed.
            if event.key == pygame.K_RIGHT:
                player.move('right')  # Move the player right if the right arrow key is pressed.
            if event.key == pygame.K_SPACE:
                bullet.fire(player.x)  # Fire a bullet if the spacebar is pressed.
        
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                player.stop_move()  # Stop the player when arrow keys are released.

    # Update game state:
    screen.fill((0, 0, 0))  # Clear the screen with black.
    screen.blit(background, (0, 0))  # Draw the background.

    player.update()  # Update the player's position.
    bullet.update()  # Update the bullet's position.

    # Render game objects:
    player.draw()  # Draw the player on the screen.
    bullet.draw()  # Draw the bullet on the screen.
    for enemy in enemies:
        enemy.draw()  # Draw each enemy on the screen.

    pygame.display.update()  # Update the display.

time.sleep(2)  # Wait for 2 seconds before quitting.
pygame.quit()  # Quit pygame and close the window.