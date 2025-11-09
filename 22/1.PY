import pygame

pygame.init()

SMIDTH = 600
SHEIGHT = 400

screen = pygame.display.set_mode((SMIDTH, SHEIGHT))

font = pygame.font.SysFont("Times New Roman", 72)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, h, w):
        super().__init__()
        self.image = pygame.Surface((w,h))
        self.image.fill(color)
        self.image.set_colorkey(color)
       # pygame.draw.rect(self.image, image_color, pygame.Rect(30,30,30,30))
        self.rect = self.image.get_rect()
    def move(self,xchange,ychange):
        self.rect.x = max(min(self.rect.x + xchange, SMIDTH - self.rect.x), 0)
        self.rect.y = max(min(self.rect.y + ychange, SHEIGHT - self.rect.y), 0)

clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

sprite1 = Sprite(("green"), 20, 20)
sprite1.rect.x = 200
sprite1.rect.y =200
all_sprites.add(sprite1)

sprite2 = Sprite(("red"), 20, 20)
sprite2.rect.x = 100
sprite1.rect.y = 50
all_sprites.add(sprite2)

while True:
    screen.fill("black")
    for event in pygame.event.get():
        if event.type == pygame .QUIT:
            quit()
    keys = pygame.key.getpressed()

    xchange = (keys[pygame.K_right]-keys[pygame.K_Left]) *mspeed
    ychange = (keys[pygame.K_DOWN]-keys[pygame.K_UP]) *mspeed
    if sprite1.rect,collederect(sprite2.rect):

        win_text =font.render("you win👍👌",True,pygame.color('yellow'))
        screen.blit(win_text,(200,200))
        all_sprites.remove(sprite2)

sprite1.move(xchange,ychange)
pygame.display.flip()
clock.tick(90)
