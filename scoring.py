import random

def generate_customer_target():
    """Generates a random target budget in RMB."""
    return round(random.uniform(15.0, 40.0), 2)

def calculate_score(total_weight_g, price_per_50g, target_budget, missing_items_count):
    """
    Calculates final price and score. 
    Score is out of 100. Missing items incur a harsh penalty.
    """
    # Actual Price
    actual_price = (total_weight_g / 50) * price_per_50g
    actual_price = round(actual_price, 2)

    # Score
    difference = abs(actual_price - target_budget)
    error_percentage = difference / target_budget
    
    base_score = max(0, 100 - int(error_percentage * 100))

    # Penalty
    if missing_items_count > 0:
        base_score = base_score // 2
        if base_score < 0: base_score = 0

    return actual_price, base_score