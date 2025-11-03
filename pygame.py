# Simple Pygame example: create a game screen and add elements (rectangles + text)
# Save as main.py and run with: python main.py
# Requirements: pygame (pip install pygame)

import sys
import pygame

# ---- Configuration ----
WIDTH, HEIGHT = 800, 500
FPS = 60
BG_COLOR = (245, 245, 250)       # very light background
RECT_COLOR = (70, 130, 180)      # steel blue
RECT_BORDER = (30, 60, 90)       # darker border
BUTTON_COLOR = (220, 70, 70)     # red button
BUTTON_HOVER = (255, 90, 90)
TEXT_COLOR = (255, 255, 255)
TITLE_COLOR = (40, 40, 40)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Add elements to my Screen — Basic Game Building Concepts")
clock = pygame.time.Clock()

# Fonts: use default font
title_font = pygame.font.Font(None, 40)
body_font = pygame.font.Font(None, 32)
button_font = pygame.font.Font(None, 28)

# Pre-render static text surfaces
title_surf = title_font.render("Basic Game Building Concepts", True, TITLE_COLOR)
subtitle_surf = body_font.render("Write a Python program to add rectangles and text using pygame.", True, TITLE_COLOR)

# Define a big rectangle (e.g., a panel)
panel_rect = pygame.Rect(80, 110, WIDTH - 160, 220)

# Define a button rectangle (example: "Submit now")
button_rect = pygame.Rect((WIDTH // 2) - 80, panel_rect.bottom + 30, 160, 48)

running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and button_rect.collidepoint(event.pos):
                # Example action for clicking the button
                print("Submit button clicked!")

    # ---- Drawing ----
    screen.fill(BG_COLOR)

    # Draw title at top-left
    screen.blit(title_surf, (40, 20))
    screen.blit(subtitle_surf, (40, 70))

    # Draw panel rectangle with border
    pygame.draw.rect(screen, RECT_BORDER, panel_rect, border_radius=8)           # border (drawn first)
    inner_panel = panel_rect.inflate(-8, -8)                                    # slightly smaller inner rect
    pygame.draw.rect(screen, RECT_COLOR, inner_panel, border_radius=6)           # filled inner

    # Draw some example text inside the panel
    sample_text = body_font.render("This is a rectangle (panel). You can put text here.", True, (255, 255, 255))
    text_rect = sample_text.get_rect(center=(panel_rect.centerx, panel_rect.centery - 20))
    screen.blit(sample_text, text_rect)

    # Draw a smaller informational rectangle (like a card)
    card_rect = pygame.Rect(120, panel_rect.top + 30, 220, 120)
    pygame.draw.rect(screen, (255, 255, 255), card_rect, border_radius=6)
    pygame.draw.rect(screen, (200, 200, 200), card_rect, 2, border_radius=6)

    card_title = body_font.render("Card Title", True, (20, 20, 20))
    screen.blit(card_title, (card_rect.left + 12, card_rect.top + 12))
    card_body = pygame.font.Font(None, 20).render("Some explanatory text here.", True, (60, 60, 60))
    screen.blit(card_body, (card_rect.left + 12, card_rect.top + 48))

    # Draw submit button (hover effect)
    is_hover = button_rect.collidepoint(mouse_pos)
    pygame.draw.rect(screen, BUTTON_HOVER if is_hover else BUTTON_COLOR, button_rect, border_radius=6)
    button_label = button_font.render("Submit now", True, TEXT_COLOR)
    blit_rect = button_label.get_rect(center=button_rect.center)
    screen.blit(button_label, blit_rect)

    # Draw FPS in top-right for debugging/feedback
    fps_surf = button_font.render(f"FPS: {int(clock.get_fps())}", True, (80, 80, 80))
    screen.blit(fps_surf, (WIDTH - fps_surf.get_width() - 12, 12))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()