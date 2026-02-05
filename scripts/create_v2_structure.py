"""Create models_v2 directory structure by copying models."""

import shutil
from pathlib import Path


def create_v2_structure():
    """Create V2 directory structure."""
    src = Path("src/armodel")
    models = src / "models"
    models_v2 = src / "models_v2"

    if models_v2.exists():
        print(f"WARNING: {models_v2} already exists")
        response = input("Delete and recreate? (y/N): ")
        if response.lower() == "y":
            shutil.rmtree(models_v2)
        else:
            print("Aborted")
            return

    print(f"Copying {models} -> {models_v2}")
    shutil.copytree(models, models_v2)

    print(f"✓ Created {models_v2}")
    print("Next: Run scripts/refactor_v2_imports.py")


if __name__ == "__main__":
    create_v2_structure()
