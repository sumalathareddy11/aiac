import random

# Sample product database with categories and brands
products = [
    {"name": "UltraSoft Toothbrush", "category": "Toothbrush", "brand": "SmileCo"},
    {"name": "BrightWhite Toothbrush", "category": "Toothbrush", "brand": "Dentex"},
    {"name": "FreshMint Toothpaste", "category": "Toothpaste", "brand": "SmileCo"},
    {"name": "Whitening Toothpaste", "category": "Toothpaste", "brand": "Dentex"},
    {"name": "SilkyShampoo", "category": "Shampoo", "brand": "HairCare"},
    {"name": "VolumeBoost Shampoo", "category": "Shampoo", "brand": "Glow"},
    {"name": "GentleSoap", "category": "Soap", "brand": "CleanSkin"},
    {"name": "AloeSoap", "category": "Soap", "brand": "NatureFresh"},
]

# User feedback memory (for a simple learning system)
user_feedback = {}

def get_user_purchase():
    print("Available products:")
    for idx, prod in enumerate(products):
        print(f"{idx+1}. {prod['name']} ({prod['category']}, {prod['brand']})")
    while True:
        try:
            choice = int(input("Enter the number of a product you bought before: "))
            if 1 <= choice <= len(products):
                return products[choice-1]
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Please enter a valid number.")

def recommend_products(purchased_product):
    # Recommend products from the same category but different brand if possible
    category = purchased_product['category']
    prev_brand = purchased_product['brand']
    # Filter out products of the same brand as last purchase
    candidates = [p for p in products if p['category'] == category and p['brand'] != prev_brand]
    # If all products are from the same brand, allow same brand
    if not candidates:
        candidates = [p for p in products if p['category'] == category]
    # Shuffle to avoid always picking the same
    random.shuffle(candidates)
    # Sort by user feedback (likes first)
    candidates.sort(key=lambda p: -user_feedback.get(p['name'], 0))
    # Recommend up to 2 products
    return candidates[:2]

def explain_recommendation(product, purchased_product):
    # Explain why this product is suggested
    explanation = f"We recommend '{product['name']}' because it's also a {product['category']} "
    if product['brand'] != purchased_product['brand']:
        explanation += f"from a different brand ({product['brand']}) to give you more variety."
    else:
        explanation += f"from the same brand you liked before ({product['brand']})."
    return explanation

def get_feedback(product):
    # Ask user for feedback and update memory
    while True:
        feedback = input(f"Do you like the suggestion '{product['name']}'? (like/dislike): ").strip().lower()
        if feedback in ("like", "dislike"):
            # +1 for like, -1 for dislike
            user_feedback[product['name']] = user_feedback.get(product['name'], 0) + (1 if feedback == "like" else -1)
            return
        else:
            print("Please type 'like' or 'dislike'.")

def main():
    print("Welcome to the Product Recommender!")
    purchased = get_user_purchase()
    recommendations = recommend_products(purchased)
    if not recommendations:
        print("Sorry, we have no recommendations at this time.")
        return
    for rec in recommendations:
        print(f"\nSuggested product: {rec['name']} ({rec['brand']})")
        print("Reason:", explain_recommendation(rec, purchased))
        get_feedback(rec)  # Let user give feedback to improve the system

    print("\nThank you for your feedback! Our recommendations will improve over time.")

if __name__ == "__main__":
    main()
