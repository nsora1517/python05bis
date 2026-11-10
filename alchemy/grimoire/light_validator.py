MAGIC = ["earth", "air", "fire", "water"]


def validate_ingredients(ingredients: str) -> str:
    low = ingredients.lower()
    if any(allowed in low for allowed in MAGIC):
        return f"Ingredients '{ingredients}' are VALID"
    return f"Ingredients '{ingredients}' are INVALID"
