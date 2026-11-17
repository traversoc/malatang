import pygame
import sys
import bowl; import game; import ingredients; import player; import scoring; import shop

pygame.init()

# DISPLAY
WIDTH, HEIGHT = 800,600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Background Image")

# 3. Load and scale the background image
bg_image = pygame.image.load("background.png").convert()
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))

# 4. Main game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the background FIRST (at top-left corner 0, 0)
    screen.blit(bg_image, (0, 0))

    # Draw other game objects (players, enemies, UI) AFTER the background

    # Update the display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
