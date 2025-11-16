# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Background
background = pygame.image.load('backgroundspace.png')

# Player
playerImg = pygame.image.load('player.png')
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

def player(x,y)
    
    screen.blit(palayerlag,(x,y))

    #bullet

bulleting = pyagme.image.load('bullet.png')
bulletx = 0
bullety =PLAYER_START_Y
bulletX_change = BULLET_SPEED_Y
bullet_state ="ready"

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen,blit(bulleting,(x+16,y+10))
running = True

while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletX = playerX
                fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            playerX_change = 0

    playerX += playerX_change
    playerX = max(0, min(playerX, SCREEN_WIDTH - 64))

    if bulletY <= 0:
        bulletY = PLAYER_START_Y
        bullet_state = "ready"
    elif bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX,playerY)
    pygame.display.update()




