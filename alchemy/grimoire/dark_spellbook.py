from .dark_validator import validate_ingredients


DARK_MAGIC = ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_allowed_ingredients() -> list[str]:
    return DARK_MAGIC


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    result = validate_ingredients(ingredients)
    if "VALID" in result and "INVALID" not in result:
        return f"Spell recorded: {spell_name} ({ingredients} - VALID)"
    return f"Spell rejected: {spell_name} ({ingredients} - INVALID)"
