import pygame
import random, time
from objects import Player, Bullet, Enemy
from helpers import check_collision, show_score, game_over_text, game_init

"""
Main game loop for a simple 2D shooting game.

In this game:
- The player controls a ship and shoots bullets to hit falling enemies.
- Each bullet hit increases the score.
- The game ends when any enemy reaches the bottom of the screen.
"""

# Game initialization
screen, background = game_init()  # Initialize the game screen and background image.

# Fonts for displaying the score
score_font = pygame.font.Font('freesansbold.ttf', 32)  # Set font style and size for score display.

# Game objects
player = Player(screen)  # Create the player object (the ship controlled by the user).
bullet = Bullet(screen)  # Create the bullet object (used to shoot at enemies).
enemies = [Enemy(screen) for _ in range(6)]  # Create a list of 6 enemy objects that will fall from the top.

# Score tracking
score = 0  # Initialize the score at the start of the game.

# Game loop: This loop will run until the game is over.
running = True
while running:
    # Event handling: Check for user input (key presses) and system events (like closing the window).
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()  # Exit the game if the player closes the window.
            running = False  # Stop the game loop if the window is closed.
        
        # Check for key presses (player input)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.move('left')  # Move player to the left if the left arrow key is pressed.
            if event.key == pygame.K_RIGHT:
                player.move('right')  # Move player to the right if the right arrow key is pressed.
            if event.key == pygame.K_SPACE:
                bullet.fire(player.x)  # Fire a bullet if the spacebar is pressed.
        
        # Check for key releases (stopping player movement)
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                player.stop_move()  # Stop the player's movement when the left or right arrow key is released.

    # Update game state:
    screen.fill((0, 0, 0))  # Clear the screen and fill it with black color to prevent previous frames from showing.
    screen.blit(background, (0, 0))  # Draw the background image on the screen.

    player.update()  # Update the player's position based on user input.
    bullet.update()  # Update the bullet's position (move it upwards if fired).

    game_over = False  # Initialize the game over condition (set to False initially).
    
    # Update the position of each enemy and check if the game is over or if collisions happen.
    for enemy in enemies:
        enemy.move()  # Move the enemy down the screen.

        # Check if the enemy has passed the bottom of the screen, indicating game over.
        if enemy.y > 440:  # If the enemy's y-coordinate is greater than 440, the game is over.
            game_over = True
        
        # Check if the bullet collides with the enemy.
        if check_collision(enemy.x, enemy.y, bullet.x, bullet.y):  # If the bullet hits an enemy:
            score += 1  # Increase the score by 1.
            enemy.x = random.randint(0, 736)  # Move the enemy to a new random x-coordinate.
            enemy.y = random.randint(50, 150)  # Move the enemy to a random y-coordinate (to the top).
            bullet.reset()  # Reset the bullet position after hitting an enemy.

    # Render the game objects on the screen.
    player.draw()  # Draw the player (ship).
    bullet.draw()  # Draw the bullet.
    for enemy in enemies:
        enemy.draw()  # Draw each enemy.

    # Render the score on the screen.
    show_score(screen, score, score_font)  # Display the score at the top of the screen.

    # Game over handling:
    if game_over:
        game_over_text(screen, score_font)  # Display the "Game Over" text.
        running = False  # End the game loop (stop the game).

    pygame.display.update()  # Update the screen to reflect changes made in this frame.

# Wait for a few seconds after the game ends before quitting.
time.sleep(2)

# Quit pygame and close the game window.
pygame.quit()