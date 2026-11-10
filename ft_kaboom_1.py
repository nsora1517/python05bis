print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")


from alchemy.grimoire.dark_spellbook import dark_spell_record  # noqa: E402


def main() -> None:
    print(dark_spell_record("magic", "earth"))


if __name__ == "__main__":
    main()
