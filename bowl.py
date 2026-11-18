import random

class Bowl:
    def __init__(self, price_per_gram):
        self.items = []
        self.price_per_gram = price_per_gram

    def add(self, name, actual_weight, image_surface):
        self.items.append({
            "name": name, 
            "weight": actual_weight,
            "image": image_surface,
            "offset_x": random.randint(-25, 25),
            "offset_y": random.randint(-15, 15),
            "rotation": random.randint(-45, 45)
        })

    def total_weight(self):
        return sum(item["weight"] for item in self.items)

    def calculate_final_price(self):
        return self.total_weight() * self.price_per_gram

    def check_requirements(self, required_items):
        bowl_names = [item["name"] for item in self.items]
        return [req for req in required_items if req not in bowl_names]

    def clear(self):
        self.items = []