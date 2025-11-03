

import pygame
import sys
import math
import time

pygame.init()
WIDTH, HEIGHT = 900, 420
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Game Screen")

CLOCK = pygame.time.Clock()
FPS = 60

# Colors
BG_TOP = (230, 245, 255)
BG_BOTTOM = (200, 235, 255)
TV_BLUE = (34, 150, 210)
TV_LIGHT = (180, 230, 255)
WHITE = (255, 255, 255)
ACCENT = (255, 90, 90)
DARK = (20, 20, 30)
PANEL = (245, 245, 245)
BUTTON_NORMAL = (255, 255, 255)
BUTTON_HOVER = (255, 230, 225)
BUTTON_BORDER = (255, 100, 80)

pygame.font.init()
TITLE_FONT = pygame.font.SysFont("arial", 30, bold=True)
SUBFONT = pygame.font.SysFont("arial", 20)
SMALL = pygame.font.SysFont("arial", 14)
SCREEN_FONT = pygame.font.SysFont("arial", 26, bold=True)

# Small helper: rounded_rect for pygame < 2.0 fallback uses draw.rect
def rounded_rect(surface, rect, color, radius=12):
    try:
        pygame.draw.rect(surface, color, rect, border_radius=radius)
    except TypeError:
        pygame.draw.rect(surface, color, rect)  # fallback

# Floating decorative icon
class Icon:
    def __init__(self, x, y, r, color, face_color=(0,0,0)):
        self.x = x
        self.y = y
        self.r = r
        self.base_y = y
        self.color = color
        self.face = face_color
        self.phase = (x + y) % 360

    def update(self, t):
        # bobbing motion
        self.y = self.base_y + math.sin(t * 2 + self.phase * 0.02) * 10

    def draw(self, surf):
        pygame.draw.circle(surf, self.color, (int(self.x), int(self.y)), self.r)
        # eyes
        ex = int(self.x - self.r * 0.3)
        ey = int(self.y - self.r * 0.15)
        pygame.draw.circle(surf, WHITE, (ex, ey), max(1, int(self.r * 0.2)))
        pygame.draw.circle(surf, WHITE, (int(self.x + self.r * 0.3), ey), max(1, int(self.r * 0.2)))
        pygame.draw.circle(surf, self.face, (ex, ey), max(1, int(self.r * 0.08)))
        pygame.draw.circle(surf, self.face, (int(self.x + self.r * 0.3), ey), max(1, int(self.r * 0.08)))
        # smile
        pygame.draw.arc(surf, self.face, (int(self.x - self.r*0.45), int(self.y - self.r*0.05), int(self.r*0.9), int(self.r*0.7)), math.pi/8, math.pi - math.pi/8, 2)

# Create a few decorative icons
icons = [
    Icon(110, 110, 28, (111, 221, 134), DARK),
    Icon(60, 70, 20, (255, 180, 90), DARK),
    Icon(40, 230, 18, (255, 120, 180), DARK),
    Icon(180, 200, 22, (120, 200, 255), DARK),
    Icon(220, 90, 16, (255, 220, 90), DARK),
    Icon(280, 140, 24, (200, 130, 240), DARK),
]

# Submit button rect
button_rect = pygame.Rect(WIDTH - 220, HEIGHT - 90, 140, 42)
submit_clicked_at = None
submitted_message_duration = 2.0  # seconds

def draw_background(surf):
    # vertical gradient
    for i in range(HEIGHT):
        ratio = i / HEIGHT
        r = int(BG_TOP[0] * (1 - ratio) + BG_BOTTOM[0] * ratio)
        g = int(BG_TOP[1] * (1 - ratio) + BG_BOTTOM[1] * ratio)
        b = int(BG_TOP[2] * (1 - ratio) + BG_BOTTOM[2] * ratio)
        pygame.draw.line(surf, (r, g, b), (0, i), (WIDTH, i))

def draw_left_art(surf):
    # big rounded panel containing art
    panel_rect = pygame.Rect(20, 30, 360, HEIGHT - 60)
    rounded_rect(surf, panel_rect, PANEL, 14)
    # draw a decorative TV inside panel
    tv_rect = pygame.Rect(50, 60, 280, 180)
    rounded_rect(surf, tv_rect, TV_BLUE, 18)
    inner = pygame.Rect(tv_rect.x + 12, tv_rect.y + 12, tv_rect.w - 24, tv_rect.h - 24)
    rounded_rect(surf, inner, TV_LIGHT, 12)
    # "MY FIRST GAME SCREEN" text inside tv
    lines = ["MY FIRST", "GAME SCREEN"]
    t1 = SCREEN_FONT.render(lines[0], True, DARK)
    t2 = SCREEN_FONT.render(lines[1], True, DARK)
    surf.blit(t1, (inner.x + (inner.w - t1.get_width()) // 2, inner.y + 30))
    surf.blit(t2, (inner.x + (inner.w - t2.get_width()) // 2, inner.y + 70))

    # draw small buttons/leds on tv
    pygame.draw.circle(surf, (255, 100, 100), (tv_rect.x + 18, tv_rect.y + tv_rect.h - 18), 6)
    pygame.draw.circle(surf, (255, 220, 100), (tv_rect.x + 40, tv_rect.y + tv_rect.h - 18), 6)
    pygame.draw.circle(surf, (120, 255, 140), (tv_rect.x + 62, tv_rect.y + tv_rect.h - 18), 6)

    # draw a simple controller below TV
    ctrl_x, ctrl_y = 120, 260
    ctrl_w, ctrl_h = 200, 80
    rounded_rect(surf, pygame.Rect(ctrl_x, ctrl_y, ctrl_w, ctrl_h), DARK, 14)
    inner_ctrl = pygame.Rect(ctrl_x + 10, ctrl_y + 10, ctrl_w - 20, ctrl_h - 20)
    rounded_rect(surf, inner_ctrl, (240, 240, 250), 10)
    # dpad
    pygame.draw.rect(surf, DARK, (ctrl_x + 20, ctrl_y + 26, 12, 28))
    pygame.draw.rect(surf, DARK, (ctrl_x + 8, ctrl_y + 38, 36, 12))
    # face buttons
    pygame.draw.circle(surf, (255, 95, 95), (ctrl_x + 160, ctrl_y + 30), 10)
    pygame.draw.circle(surf, (95, 195, 255), (ctrl_x + 185, ctrl_y + 48), 10)
    pygame.draw.circle(surf, (255, 205, 90), (ctrl_x + 140, ctrl_y + 48), 10)
    # small labels
    surf.blit(SMALL.render("A", True, DARK), (ctrl_x + 154, ctrl_y + 22))
    surf.blit(SMALL.render("B", True, DARK), (ctrl_x + 180, ctrl_y + 40))

    # draw some scattered icons
    for ic in icons:
        ic.draw(surf)

def draw_right_panel(surf, mouse_pos):
    # Title and description area
    start_x = 410
    box = pygame.Rect(start_x, 30, WIDTH - start_x - 20, HEIGHT - 60)
    # white card background
    rounded_rect(surf, box, (250,250,250), 10)

    # Title
    surf.blit(TITLE_FONT.render("My First Game Screen", True, DARK), (box.x + 20, box.y + 18))
    surf.blit(SUBFONT.render("Let's Begin with Pygame", True, (90,90,90)), (box.x + 20, box.y + 56))

    desc = "Write a Python program to create your first Game screen using the Pygame library."
    # wrap description
    words = desc.split()
    line = ""
    y = box.y + 96
    for w in words:
        test = (line + " " + w).strip()
        txt = SMALL.render(test, True, (80,80,80))
        if txt.get_width() > box.w - 40:
            surf.blit(SMALL.render(line, True, (80,80,80)), (box.x + 20, y))
            line = w
            y += 18
        else:
            line = test
    if line:
        surf.blit(SMALL.render(line, True, (80,80,80)), (box.x + 20, y))

    # due date and points
    surf.blit(SMALL.render("11:59 PM WAST, Nov 08, 2025", True, (110,110,110)), (box.x + 20, box.y + box.h - 88))
    surf.blit(SMALL.render("Due date of submission", True, (150,150,150)), (box.x + 20, box.y + box.h - 68))
    surf.blit(SMALL.render("+100 points", True, (100,100,100)), (box.x + box.w - 110, box.y + box.h - 88))

    # Draw "Submit now" button with hover effect
    hover = button_rect.collidepoint(mouse_pos)
    bcolor = BUTTON_HOVER if hover else BUTTON_NORMAL
    rounded_rect(surf, button_rect, bcolor, 8)
    pygame.draw.rect(surf, BUTTON_BORDER, button_rect, 2, border_radius=8)
    txt = SUBFONT.render("Submit now", True, (150, 40, 35))
    surf.blit(txt, (button_rect.x + (button_rect.w - txt.get_width())//2, button_rect.y + (button_rect.h - txt.get_height())//2))

def main():
    global submit_clicked_at
    running = True
    start_time = time.time()
    while running:
        t = time.time() - start_time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if button_rect.collidepoint(event.pos):
                    submit_clicked_at = time.time()
                    print("Submit clicked (simulated).")  # simulate submission action

        # update icons
        for ic in icons:
            ic.update(t)

        # draw
        draw_background(SCREEN)
        draw_left_art(SCREEN)
        mouse_pos = pygame.mouse.get_pos()
        draw_right_panel(SCREEN, mouse_pos)

        
        if submit_clicked_at:
            elapsed = time.time() - submit_clicked_at
            if elapsed < submitted_message_duration:
                msg = TITLE_FONT.render("Submitted!", True, (10, 150, 70))
                SCREEN.blit(msg, (WIDTH - 220, HEIGHT - 140))
            else:
                submit_clicked_at = None

        pygame.display.flip()
        CLOCK.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()