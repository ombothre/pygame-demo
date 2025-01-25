import pygame
from pygame import image, Surface
from pygame.font import Font
import math

def check_collision(enemy_x: int, enemy_y: int, bullet_x: int, bullet_y: int):
    """Check if bullet hits enemy."""
    distance = math.sqrt(
        (enemy_x - bullet_x)**2 + 
        (enemy_y - bullet_y)**2
    )
    return distance < 27

def show_score(screen: Surface, score: int, font: Font):
    """Render score on screen."""
    score_text = font.render(
        f"Score: {score}", 
        True, 
        (255, 255, 255)
    )
    screen.blit(score_text, (10, 10))

def game_over_text(screen: Surface, font: Font):
    """Display game over message."""
    over_text = font.render(
        "GAME OVER", 
        True, 
        (255, 255, 255)
    )
    screen.blit(over_text, (200, 250))

def game_init():
    """Initialize pygame and game window."""
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Space Wars")
    
    # Background setup
    background = image.load('assets/images/background.png')
    
    return screen, background