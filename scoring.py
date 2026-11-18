import random

"""Price and score calculations."""
def calculate_price(total_weight_g, price_per):
    price_per = 1.48
    return (total_weight_g / 50) * price_per

def calculate_score(actual_price, target_budget, missing_count=0):
    target_budget=(random.randint(50,500))/10
    