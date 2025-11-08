import pygame
import random

pygame.init()

width = 500
height = 400
screen_res = (width, height)
colors = ['Red', 'Blue', 'Green', 'Yellow', 'Cyan', 'Tomato', 'DarkOrange', 'Brown']
bg_colors = ['Red', 'Blue', 'Green', 'Yellow', 'Cyan', 'Tomato', 'DarkOrange', 'Brown']
clr = random.choice(colors)

pygame.display.set_caption("Bouncing game")
screen = pygame.display.set_mode(screen_res)
# set the colors
# red = (255, 0, 0)
# black = (0, 0, 0)

x = 100
y = 100
bg_color = 'red'
# define rect
rect_obj = pygame.draw.rect(screen, 'Red', pygame.Rect(x, y, 40, 40))
# define speed of rect
speed = [1, -1]

#game loop 
while True:
    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            exit()

    
    screen.fill(bg_color)

    rect_obj = rect_obj.move(speed)

    
    speed[0] = -speed[0]
    clr = random.choice(colors)
    bg_color = random.choice(bg_colors)

    while True:
    # event loop
      for event in pygame.event.get():  
        # check if a user wants to exit the game or not
          if event.type == pygame.QUIT:
            exit()

    # fill black color on screen
      screen.fill(bg_color)

      rect_obj = rect_obj.move(speed)

    # if ball goes out of screen then change direction of movement
      if rect_obj.left <= 0 or rect_obj.right >= width:
          speed[0] = -speed[0]
          clr = random.choice(colors)
          bg_color = random.choice(bg_colors)

      if rect_obj.top <= 0 or rect_obj.bottom >= height:
          speed[1] = -speed[1]
          clr = random.choice(colors)
          bg_color = random.choice(bg_colors)

    # draw ball at new centers that are obtained after moving ball_obj
      rect_obj = pygame.draw.rect(screen, clr, pygame.Rect(rect_obj.x, rect_obj.y, 40, 40))


    
      rect_obj = pygame.draw.rect(screen, clr, pygame.Rect(rect_obj.x, rect_obj.y, 40, 40))

      pygame.display.flip()
