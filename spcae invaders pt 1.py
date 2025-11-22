import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invader Project - Part 1")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Sprite dimensions
PLAYER_SIZE = 50
ENEMY_SIZE = 40

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
        self.image.fill((0, 255, 0))  # Green
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT - 60))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += 5

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((ENEMY_SIZE, ENEMY_SIZE))
        self.image.fill((255, 0, 0))  # Red
        self.rect = self.image.get_rect(
            center=(random.randint(ENEMY_SIZE, WIDTH - ENEMY_SIZE),
                    random.randint(ENEMY_SIZE, HEIGHT // 2))
        )

# Sprite groups
player = Player()
player_group = pygame.sprite.Group(player)

enemies = pygame.sprite.Group()
for _ in range(7):
    enemies.add(Enemy())

# Game loop
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player_group.update()

    # Collision detection
    collided_enemies = pygame.sprite.spritecollide(player, enemies, True)
    score += len(collided_enemies)

    # Draw sprites
    player_group.draw(screen)
    enemies.draw(screen)

    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()