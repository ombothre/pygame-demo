import pygame
import random, time
from objects import Player, Bullet, Enemy
from helpers import check_collision, show_score, game_over_text, game_init

"""Main game loop."""
# Game initialization
screen, background = game_init()

# Fonts
score_font = pygame.font.Font('freesansbold.ttf', 32)

# Game objects 
player = Player(screen)
bullet = Bullet(screen)
enemies = [Enemy(screen) for _ in range(6)]

# Score tracking
score = 0

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.move('left')
            if event.key == pygame.K_RIGHT:
                player.move('right')
            if event.key == pygame.K_SPACE:
                bullet.fire(player.x)
        
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                player.stop_move()
    
    # Update game state
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    
    player.update()
    bullet.update()
    
    game_over = False
    for enemy in enemies:
        enemy.move()
        
        # Check for game over
        if enemy.y > 440:
            game_over = True
        
        # Check for collisions
        if check_collision(enemy.x, enemy.y, bullet.x, bullet.y):
            score += 1
            enemy.x = random.randint(0, 736)
            enemy.y = random.randint(50, 150)
            bullet.reset()
    
    # Render game objects
    player.draw()
    bullet.draw()
    for enemy in enemies:
        enemy.draw()
    
    # Render score
    show_score(screen, score, score_font)
    
    # Game over handling
    if game_over:
        game_over_text(screen, score_font)
        running = False
    
    pygame.display.update()

time.sleep(5)
pygame.quit()