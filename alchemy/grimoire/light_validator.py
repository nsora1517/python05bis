from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    low = ingredients.lower()
    allowed = light_spell_allowed_ingredients()
    if any(a in low for a in allowed):
        return f"Ingredients '{ingredients}' are VALID"
    return f"Ingredients '{ingredients}' are INVALID"
