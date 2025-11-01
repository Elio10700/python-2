import pygame 

pygame.init()

pygame.display.set_mode((400,500))
pygame.display.set_caption("my game window")

done = False 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    pygame.display.flip()