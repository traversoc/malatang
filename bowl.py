import pygame
import random
import math
import os

class Bowl:
    def __init__(self, price_per_gram):
        self.items = []
        self.price_per_gram = price_per_gram 
        
        base_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(base_dir, "images", "Bowl.png")
        
        try:
            self.image = pygame.image.load(path).convert_alpha()
            self.image = pygame.transform.smoothscale(self.image, (240, 150))
        except Exception as e:
            print(f"Could not load Bowl.png: {e}")
            self.image = pygame.Surface((240, 150), pygame.SRCALPHA)
            pygame.draw.ellipse(self.image, (180, 180, 180), (0, 0, 240, 150), 3)

    def add(self, name, actual_weight, image_surface):
        scaled_image = pygame.transform.smoothscale(image_surface, (30, 30))
        
        angle = random.uniform(0, 2 * math.pi)
        radius = math.sqrt(random.uniform(0, 1)) 
        offset_x = math.cos(angle) * radius * 80  
        offset_y = math.sin(angle) * radius * 45  

        self.items.append({
            "name": name, 
            "weight": actual_weight,
            "image": scaled_image,
            "offset_x": offset_x,
            "offset_y": offset_y,
            "rotation": random.randint(0, 360)
        })
        
        self.items.sort(key=lambda i: i["offset_y"])

    def total_weight(self):
        return sum(item["weight"] for item in self.items)

    def calculate_final_price(self):
        return self.total_weight() * self.price_per_gram

    def check_requirements(self, required_items):
        bowl_names = [item["name"] for item in self.items]
        return [req for req in required_items if req not in bowl_names]

    def clear(self):
        self.items = []
