import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invader")

# Load background image
background = pygame.image.load("background.png")

# Load background music
pygame.mixer.music.load("background.wav")
pygame.mixer.music.play(-1)  # Loop indefinitely

# Load player
player_img = pygame.image.load("player.png")
player_x = 370
player_y = 480
player_x_change = 0

# Load enemy
enemy_img = pygame.image.load("enemy.png")
enemy_x = random.randint(0, 736)
enemy_y = random.randint(50, 150)
enemy_x_change = 4
enemy_y_change = 40

# Load bullet
bullet_img = pygame.image.load("bullet.png")
bullet_x = 0
bullet_y = 480
bullet_x_change = 0
bullet_y_change = 10
bullet_state = "ready"  # "ready" - can't see bullet; "fire" - bullet is moving

# Function to draw player
def player(x, y):
    screen.blit(player_img, (x, y))

# Function to draw enemy
def enemy(x, y):
    screen.blit(enemy_img, (x, y))

# Function to fire bullet
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))

# Function to check collision
def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = ((enemy_x - bullet_x)**2 + (enemy_y - bullet_y)**2)**0.5
    return distance < 27

# Game loop
running = True
while running:
    screen.blit(background, (0, 0))  # Draw background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Key press events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -5
            if event.key == pygame.K_RIGHT:
                player_x_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # Player movement
    player_x += player_x_change
    player_x = max(0, min(player_x, 736))

    # Enemy movement
    enemy_x += enemy_x_change
    if enemy_x <= 0 or enemy_x >= 736:
        enemy_x_change *= -1
        enemy_y += enemy_y_change

    # Bullet movement
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change
        if bullet_y <= 0:
            bullet_y = 480
            bullet_state = "ready"

    # Collision detection
    if is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
        bullet_y = 480
        bullet_state = "ready"
        enemy_x = random.randint(0, 736)
        enemy_y = random.randint(50, 150)

    player(player_x, player_y)
    enemy(enemy_x, enemy_y)

    pygame.display.update()