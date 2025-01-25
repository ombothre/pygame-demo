import pygame
from pygame import image, Surface
from pygame.font import Font
import math

def check_collision(enemy_x: int, enemy_y: int, bullet_x: int, bullet_y: int) -> bool:
    """
    Check if the bullet collides with the enemy by calculating the distance 
    between their coordinates. If the distance is smaller than a threshold, 
    it indicates a collision.
    """
    # Calculate the Euclidean distance between the bullet and the enemy
    distance = math.sqrt(
        (enemy_x - bullet_x)**2 + 
        (enemy_y - bullet_y)**2
    )
    
    # If the distance is less than a threshold (27), it means a collision occurred.
    return distance < 27


def show_score(screen: Surface, score: int, font: Font) -> None:
    """
    Render the current score on the screen.
    """
    # Create the score text using the font and render it in white color.
    score_text = font.render(
        f"Score: {score}", 
        True, 
        (255, 255, 255)  # White color for the score
    )
    
    # Display the score text at the position (10, 10) on the screen.
    screen.blit(score_text, (10, 10))


def game_over_text(screen: Surface, font: Font) -> None:
    """
    Display a "GAME OVER" message on the screen when the player loses.
    """
    # Create the game over text using the font and render it in white color.
    over_text = font.render(
        "GAME OVER", 
        True, 
        (255, 255, 255)  # White color for the game over message
    )
    
    # Display the "GAME OVER" text at the center of the screen (roughly at (200, 250)).
    screen.blit(over_text, (200, 250))


def game_init() -> tuple:
    """
    Initialize the pygame library and set up the game window and background.

    Returns:
        tuple: A tuple containing the screen object and the background image.
    """
    pygame.init()  # Initialize pygame
    screen = pygame.display.set_mode((800, 600))  # Set the screen size to 800x600 pixels.
    pygame.display.set_caption("Space Wars")  # Set the title of the game window.
    
    # Load the background image for the game.
    background = image.load('assets/images/background.png')

    # Set the game icon (optional)
    pygame_icon = pygame.image.load('assets/images/ufo.png')
    pygame.display.set_icon(pygame_icon)
    
    # Return both the screen and background to be used in the game loop.
    return screen, background