"""Ingredient catalogue and hidden weight generation."""
import random

INGREDIENTS = {
    "Beef slices": {"category": "Meat", "min_weight": 50, "max_weight": 120},
}

def generate_weight(name, rng=None):
    rng = rng or random
    item = INGREDIENTS[name]
    return rng.randint(item["min_weight"], item["max_weight"])
