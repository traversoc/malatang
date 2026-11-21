import pygame
import sys
import os
import random
from bowl import Bowl
import ingredients
import scoring

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, "images", "ingredient sprites", "sprites")
BG_DIR = os.path.join(BASE_DIR, "images")

# Initialize
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Malatang Simulator - Prototype")

# Load Background
bg_image = pygame.image.load(os.path.join(BG_DIR, "background.png")).convert()
bg_image = pygame.transform.scale(bg_image, (500, 600))

# Load Title Screen (full window size)
title_image = pygame.image.load(os.path.join(BG_DIR, "titlescreen.png")).convert()
title_image = pygame.transform.scale(title_image, (800, 600))

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)
big_font = pygame.font.SysFont(None, 36)

game_state = "TITLE"

CATEGORY_COLORS = {
    "Vegetable": (50, 200, 50),
    "Mushroom": (170, 130, 90),
    "Processed": (240, 220, 130),
    "Seafood": (240, 130, 110),
    "Noodle": (250, 240, 180),
}

def load_sprite(name, category):
    path = os.path.join(IMG_DIR, f"{name}.png")
    if os.path.exists(path):
        img = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(img, (40, 40))
    surf = pygame.Surface((40, 40), pygame.SRCALPHA)
    surf.fill(CATEGORY_COLORS[category])
    return surf

SPRITES = {name: load_sprite(name, data["category"])
           for name, data in ingredients.INGREDIENTS.items()}

BUTTON_RECTS = {
    "BokChoy": (20, 80, 100, 90), "Spinach": (130, 80, 100, 90), "Lettuce": (240, 80, 110, 90), "CrownDaisy": (350, 80, 115, 90),
    "LotusRootSlices": (20, 200, 85, 60), "PotatoSlices": (115, 200, 85, 60), "EnokiMushroom": (205, 200, 85, 60), "ShiitakeMushroom": (290, 200, 85, 60), "WoodEarMushroom": (380, 200, 85, 60),
    "Tofu": (20, 300, 85, 60), "TofuSkinRoll": (115, 300, 85, 60), "FishBall": (200, 300, 85, 60), "BeefBall": (295, 300, 85, 60), "QuailEgg": (380, 300, 85, 60),
    "BeefRoll": (20, 385, 85, 60), "LambRoll": (115, 385, 85, 60), "Shrimp": (200, 385, 85, 60), "Squid": (290, 385, 85, 60), "CrabStick": (380, 385, 85, 60),
    "GlassNoodle": (20, 470, 170, 84), "InstantNoodle": (200, 470, 130, 84), "SweetPotatoNoodle": (330, 470, 140, 84),
}

BUTTONS = [(name, pygame.Rect(*coords)) for name, coords in BUTTON_RECTS.items()]

# le BOWL
player_bowl = Bowl(price_per_gram=0.0296)
bowl_rect = pygame.Rect(0, 0, 200, 100)
bowl_rect.center = (650, 450)

# --- GAME VARIABLES ---
PRICE_PER_50G = 1.48
target_budget = scoring.generate_customer_target()
required_item = random.choice(list(ingredients.INGREDIENTS.keys()))
actual_price = 0.0
final_score = 0
missing = []

# --- UI BUTTONS ---
submit_button_rect = pygame.Rect(520, 520, 250, 50)
next_button_rect = pygame.Rect(520, 520, 250, 50)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Title screen: Spacebar starts the game
        if event.type == pygame.KEYDOWN and game_state == "TITLE":
            if event.key == pygame.K_SPACE:
                game_state = "PLAYING"

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if game_state == "PLAYING":
                # Check ingredient buttons
                for name, rect in BUTTONS:
                    if rect.collidepoint(event.pos):
                        weight = ingredients.generate_weight(name)
                        player_bowl.add(name, weight, SPRITES[name])

                # Check Submit Button
                if submit_button_rect.collidepoint(event.pos):
                    missing = player_bowl.check_requirements([required_item])
                    actual_price, final_score = scoring.calculate_score(
                        player_bowl.total_weight(),
                        PRICE_PER_50G,
                        target_budget,
                        len(missing)
                    )
                    game_state = "EVALUATING"

            elif game_state == "EVALUATING":
                if next_button_rect.collidepoint(event.pos):
                    player_bowl.clear()
                    target_budget = scoring.generate_customer_target()
                    required_item = random.choice(list(ingredients.INGREDIENTS.keys()))
                    game_state = "PLAYING"

    # --- TITLE SCREEN RENDERING ---
    if game_state == "TITLE":
        screen.blit(title_image, (0, 0))
        pygame.display.flip()
        clock.tick(60)
        continue  # skip drawing the game underneath

    # Rendering
    screen.fill((60, 40, 30))
    screen.blit(bg_image, (0, 0))

    # # Prototype hitboxes (comment out to hide red boxes)
    # for name, rect in BUTTONS:
    #     pygame.draw.rect(screen, (255, 0, 0), rect, 1)

    # Items in bowl
    for item in player_bowl.items:
        rotated_sprite = pygame.transform.rotate(item["image"], item["rotation"])
        draw_x = bowl_rect.centerx + item["offset_x"]
        draw_y = bowl_rect.centery + item["offset_y"]
        rect = rotated_sprite.get_rect(center=(draw_x, draw_y))
        screen.blit(rotated_sprite, rect)

    # Bowl outline
    pygame.draw.ellipse(screen, (180, 180, 180), bowl_rect, 3)

    # --- UI ---
    if game_state == "PLAYING":
        screen.blit(big_font.render(f"Target: ¥{target_budget:.2f}", True, (255, 255, 0)), (520, 20))
        screen.blit(font.render(f"Price: ¥{PRICE_PER_50G:.2f} / 50g", True, (200, 200, 200)), (520, 60))

        screen.blit(font.render("Must Have:", True, (200, 200, 200)), (520, 100))
        screen.blit(font.render(f"- {required_item}", True, (255, 100, 100)), (530, 130))

        screen.blit(font.render(f"Items in bowl: {len(player_bowl.items)}", True, (255, 255, 255)), (520, 180))

        pygame.draw.rect(screen, (0, 150, 0), submit_button_rect)
        pygame.draw.rect(screen, (255, 255, 255), submit_button_rect, 2)
        screen.blit(font.render("Weigh & Pay", True, (255, 255, 255)), (submit_button_rect.x + 80, submit_button_rect.y + 15))

    elif game_state == "EVALUATING":
        overlay = pygame.Surface((800, 600), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        screen.blit(overlay, (0, 0))

        screen.blit(big_font.render("RESULTS", True, (255, 255, 255)), (350, 150))
        screen.blit(font.render(f"Target Price: ¥{target_budget:.2f}", True, (255, 255, 255)), (320, 220))
        screen.blit(font.render(f"Your Price:   ¥{actual_price:.2f}", True, (255, 255, 255)), (320, 250))

        if len(missing) > 0:
            screen.blit(font.render(f"Missing: {', '.join(missing)}", True, (255, 50, 50)), (320, 280))
        else:
            screen.blit(font.render("All required items included!", True, (50, 255, 50)), (320, 280))

        screen.blit(big_font.render(f"Score: {final_score}/100", True, (255, 255, 0)), (320, 340))

        pygame.draw.rect(screen, (0, 0, 150), next_button_rect)
        pygame.draw.rect(screen, (255, 255, 255), next_button_rect, 2)
        screen.blit(font.render("Next Customer", True, (255, 255, 255)), (next_button_rect.x + 65, next_button_rect.y + 15))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
