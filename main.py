import pygame
import sys
import os
from bowl import Bowl
import ingredients

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Initialize
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Malatang Simulator - Prototype")
bg_image = pygame.image.load(os.path.join(BASE_DIR, "background.png")).convert()
bg_image = pygame.transform.scale(bg_image, (500, 600))
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 24)

CATEGORY_COLORS = {
    "Vegetable": (50, 200, 50),
    "Mushroom": (170, 130, 90),
    "Processed": (240, 220, 130),
    "Seafood": (240, 130, 110),
    "Noodle": (250, 240, 180),
}

def load_sprite(name, category):
    """Use images/<name>.png if it exists, otherwise a colored placeholder."""
    path = os.path.join(BASE_DIR, "images", f"{name}.png")
    if os.path.exists(path):
        img = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(img, (40, 40))
    surf = pygame.Surface((40, 40), pygame.SRCALPHA)
    surf.fill(CATEGORY_COLORS[category])
    return surf

SPRITES = {name: load_sprite(name, data["category"])
           for name, data in ingredients.INGREDIENTS.items()}

# Manual button positions: (x, y, width, height)
BUTTON_RECTS = {
    "BokChoy":           (20,  80, 100, 90),
    "Spinach":           (130, 80, 100, 90),
    "Lettuce":           (240, 80, 110, 90),
    "CrownDaisy":        (350, 80, 115, 90),

    "LotusRootSlices":   (20,  200, 85, 60),
    "PotatoSlices":      (115, 200, 85, 60),
    "EnokiMushroom":     (205, 200, 85, 60),
    "ShiitakeMushroom":  (290, 200, 85, 60),
    "WoodEarMushroom":   (380, 200, 85, 60),

    "Tofu":              (20,  300, 85, 60),
    "TofuSkinRoll":      (115, 300, 85, 60),
    "FishBall":          (200, 300, 85, 60),
    "BeefBall":          (295, 300, 85, 60),
    "QuailEgg":          (380, 300, 85, 60),

    "BeefRoll":          (20,  385, 85, 60),
    "LambRoll":          (115, 385, 85, 60),
    "Shrimp":            (200, 385, 85, 60),
    "Squid":             (290, 385, 85, 60),
    "CrabStick":         (380, 385, 85, 60),

    "GlassNoodle":       (20,  470, 170, 84),
    "InstantNoodle":     (200, 470, 130, 84),
    "SweetPotatoNoodle": (330, 470, 140, 84),
}

BUTTONS = [(name, pygame.Rect(*coords)) for name, coords in BUTTON_RECTS.items()]

# le BOWL
player_bowl = Bowl(price_per_gram=0.0296)
bowl_rect = pygame.Rect(0, 0, 200, 100)
bowl_rect.center = (650, 450)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                for name, rect in BUTTONS:
                    if rect.collidepoint(event.pos):
                        weight = ingredients.generate_weight(name)
                        player_bowl.add(name, weight, SPRITES[name])
                        print(f"Added {name}! Hidden weight: {player_bowl.total_weight():.1f}g")
                        break

            elif event.button == 3:  # Right click to submit
                print("\n--- SUBMITTING BOWL ---")
                print(f"Total Weight: {player_bowl.total_weight():.1f}g")
                print(f"Total Price: {player_bowl.calculate_final_price():.2f}元")
                player_bowl.clear()
                print("Bowl cleared for next customer.\n")

    # Rendering
    screen.fill((60, 40, 30))
    screen.blit(bg_image, (0, 0))

    # Prototype hitboxes (delete these lines later)
    for name, rect in BUTTONS:
        pygame.draw.rect(screen, (255, 0, 0), rect, 3)
    pygame.draw.rect(screen, (0, 0, 255), bowl_rect, 1)

    # Items in bowl
    for item in player_bowl.items:
        rotated_sprite = pygame.transform.rotate(item["image"], item["rotation"])
        draw_x = bowl_rect.centerx + item["offset_x"]
        draw_y = bowl_rect.centery + item["offset_y"]
        rect = rotated_sprite.get_rect(center=(draw_x, draw_y))
        screen.blit(rotated_sprite, rect)

    # Bowl outline
    pygame.draw.ellipse(screen, (180, 180, 180), bowl_rect, 5)

    # Instructions (in the right panel)
    screen.blit(font.render("Left click: add item", True, (255, 255, 255)), (520, 20))
    screen.blit(font.render("Right click: submit & clear", True, (255, 255, 255)), (520, 45))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()