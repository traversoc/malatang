"""Ingredient catalogue and hidden weight generation."""
import random

INGREDIENTS = {
    # ROW1
    "BokChoy": {"category": "Vegetable", "min_weight": 10, "max_weight": 30},
    "Spinach": {"category": "Vegetable", "min_weight": 10, "max_weight": 25},
    "Lettuce": {"category": "Vegetable", "min_weight": 10, "max_weight": 25},
    "CrownDaisy": {"category": "Vegetable", "min_weight": 6, "max_weight": 12},

    # ROW2
    "LotusRootSlices": {"category": "Vegetable", "min_weight": 10, "max_weight": 15},
    "PotatoSlices": {"category": "Vegetable", "min_weight": 8, "max_weight": 16},
    "EnokiMushroom": {"category": "Mushroom", "min_weight": 10, "max_weight": 30},
    "ShiitakeMushroom": {"category": "Mushroom", "min_weight": 15, "max_weight": 35},
    "WoodEarMushroom": {"category": "Mushroom", "min_weight": 7, "max_weight": 15},

    # ROW3
    "Tofu": {"category": "Processed", "min_weight": 15, "max_weight": 25},
    "TofuSkinRoll": {"category": "Processed", "min_weight": 10, "max_weight": 15},
    "FishBall": {"category": "Processed", "min_weight": 12, "max_weight": 20},
    "BeefBall": {"category": "Processed", "min_weight": 12, "max_weight": 20},
    "QuailEgg": {"category": "Processed", "min_weight": 8, "max_weight": 12},

    # ROW4
    "BeefRoll": {"category": "Processed", "min_weight": 8, "max_weight": 14},
    "LambRoll": {"category": "Processed", "min_weight": 8, "max_weight": 14},
    "Shrimp": {"category": "Seafood", "min_weight": 10, "max_weight": 20},
    "Squid": {"category": "Seafood", "min_weight": 8, "max_weight": 16},
    "CrabStick": {"category": "Seafood", "min_weight": 8, "max_weight": 15},
    
    # ROW5
    "GlassNoodle": {"category": "Noodle", "min_weight": 30, "max_weight": 40},
    "InstantNoodle": {"category": "Noodle", "min_weight": 40, "max_weight": 67},
    "SweetPotatoNoodle": {"category": "Noodle", "min_weight": 25, "max_weight": 50}
}

def generate_weight(name, rng=None):
    rng = rng or random
    item = INGREDIENTS[name]
    return rng.randint(item["min_weight"], item["max_weight"])