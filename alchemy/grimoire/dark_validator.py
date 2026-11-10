from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    low = ingredients.lower()
    dark_magic = dark_spell_allowed_ingredients()
    if any(allowed in low for allowed in dark_magic):
        return f"Ingredients '{ingredients}' are VALID"
    return f"Ingredients '{ingredients}' are INVALID"
