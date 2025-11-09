import pygame
import sys

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rectangle Control Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Rectangle positions and sizes
player_rect = pygame.Rect(100, 100, 60, 60)
static_rect = pygame.Rect(400, 250, 100, 80)

# Speed
speed = 5

# Main game loop
running = True
while running:
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get pressed keys
    keys = pygame.key.get_pressed()

    # Movement controls for player_rect
    if keys[pygame.K_LEFT]:
        player_rect.x -= speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += speed
    if keys[pygame.K_UP]:
        player_rect.y -= speed
    if keys[pygame.K_DOWN]:
        player_rect.y += speed

    # Keep player on screen
    if player_rect.x < 0:
        player_rect.x = 0
    if player_rect.y < 0:
        player_rect.y = 0
    if player_rect.x + player_rect.width > WIDTH:
        player_rect.x = WIDTH - player_rect.width
    if player_rect.y + player_rect.height > HEIGHT:
        player_rect.y = HEIGHT - player_rect.height

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, player_rect)
    pygame.draw.rect(screen, BLUE, static_rect)

    pygame.display.update()

# Quit pygame
pygame.quit()
sys.exit()
