import pygame
import random

# Initialize Pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Custom Event: Change Sprite Color")

# Define colors
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]

# Sprite class
class ColorSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=(x, y))

    def change_color(self):
        self.color = random.choice(colors)
        self.image.fill(self.color)

# Create two sprites
sprite1 = ColorSprite(200, 200, random.choice(colors))
sprite2 = ColorSprite(400, 200, random.choice(colors))

# Group sprites
all_sprites = pygame.sprite.Group(sprite1, sprite2)

# Custom event
CHANGE_COLOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000)  # every 2 seconds

# Game loop
running = True
while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == CHANGE_COLOR_EVENT:
            sprite1.change_color()
            sprite2.change_color()

    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()