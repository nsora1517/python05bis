import importlib


def check_reagent(name: str) -> bool:
    try:
        module = importlib.import_module(name)
        version = module.__version__
        if name == "pandas":
            print(f"[OK] {name} ({version}) - Data manipulation ready")
        elif name == "numpy":
            print(f"[OK] {name} ({version}) - Numerical computation ready")
        return True
    except ImportError:
        print(f"{name}: NOT INSTALLED")
        print(f" pip: pip install {name}")
        print(f" poetry: poetry add {name}")
        return False


def main() -> None:
    print("REAGENT STATUS: Loading reagents...")
    print()
    print("Checking dependencies:")
    reagent = ["pandas", "numpy"]
    ok = True
    for name in reagent:
        if not check_reagent(name):
            ok = False
    print()
    print("pip vs Poetry:")
    print("  requirements.txt declares what to install; "
          "pip resolves it at install time.")
    print("  pyproject.toml declares the same constraints, "
          "and Poetry pins the resolved")
    print("  versions in poetry.lock so every install is identical.")
    print()
    if ok:
        print("All reagents present and accounted for.")


if __name__ == "__main__":
    main()
