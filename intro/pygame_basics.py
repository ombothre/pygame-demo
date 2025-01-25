import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame Basics")

# Set up colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Main loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white color
    screen.fill(WHITE)

    # Draw a red rectangle
    pygame.draw.rect(screen, RED, (100, 100, 50, 50))

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
