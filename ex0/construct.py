import sys
import site


def check() -> bool:
    return sys.prefix != sys.base_prefix


def print_env_info() -> None:
    print(f"Current Python: {sys.executable}")
    if not check():
        print("Virtual Environment: None detected")
        print()
        print("WARNING: You are in the global environment!")
        print()
        print("To seal the laboratory, run:")
        print("python3 -m venv lab_env")
        print("source lab_env/bin/activate # On Unix")
        print("lab_env\\Scripts\\activate # On Windows")
        print()
        print("Then run this program again.")
    else:
        print("Virtual Environment: lab_env")
        print(f"Environment Path: {sys.prefix}")
        print()
        print("SUCCESS: You are working in an isolated environment!")
        print("Safe to install reagents without affecting")
        print("the global system.")
        print()
        print("Reagent installation path:")
        print(site.getsitepackages()[0])


def main() -> None:
    if not check():
        print("LABORATORY STATUS: You are working in the open")
        print()
    else:
        print("LABORATORY STATUS: The laboratory is sealed")
        print()
    print_env_info()


if __name__ == "__main__":
    main()
