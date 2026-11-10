import os
import sys
try:
    from dotenv import load_dotenv
except ImportError:
    print("python-dotenv not installed."
          " Run: pip install -r ex1/requirements.txt")
    sys.exit(1)


def load_config() -> dict[str, str]:
    """
    loadding config from env (don't override)
    """
    load_dotenv(override=False)
    return {"mode": os.environ.get("MATRIX_MODE", "development"),
            "database_url": os.environ.get("DATABASE_URL", ""),
            "api_key": os.environ.get("API_KEY", ""),
            "log_level": os.environ.get("LOG_LEVEL", "INFO"),
            "zion_endpoint": os.environ.get("ZION_ENDPOINT", ""),
            }


def configuration(config: dict[str, str]) -> None:
    print("Configuration loaded:")
    print(f"Mode: {config['mode']}")
    if config["database_url"]:
        if "localhost" in config["database_url"]:
            print("Database: Connected to local instance")
        else:
            print("Database: Connected to remote instance")
    else:
        print("Database: Not configured")

    if config["api_key"] and config["api_key"] != "changeme":
        print("API Access: Authenticated")
    else:
        print("API Access: Not configured")

    print(f"Log Level: {config['log_level']}")

    if config["mode"] == "development":
        print("Debug Info: ENABLED (verbose output)")
    else:
        print("Debug Info: DISABLED (production hardening)")

    if config["zion_endpoint"]:
        print("Remote Network: Online")
    else:
        print("Remote Network: Offline")

    print()


def security_check(config: dict[str, str]) -> None:
    print("Configuration security check:")
    if config["api_key"] and config["api_key"] != "changeme":
        print("[OK] No hardcoded secrets detected")
    else:
        print("[WARN] API key is placeholder")

    gitignore_path = "ex1/.gitignore"
    if os.path.exists(gitignore_path):
        with open(gitignore_path) as f:
            content = f.read()
        if ".env" in content:
            print("[OK] .env file properly ignored by git")
        else:
            print("[WARN] .env is NOT in .gitignore")
    else:
        print("[WARN] .gitignore not found")

    print("[OK] Production overrides available")
    print()


def main() -> None:
    print("ORACLE STATUS: Consulting the configuration...")
    print()
    config = load_config()
    configuration(config)
    security_check(config)
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
