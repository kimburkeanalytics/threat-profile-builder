import os
from pathlib import Path

DATA_DIR = Path("data/cl0p")

files = list(DATA_DIR.glob("*.txt"))

print(f"Found {len(files)} source files.\n")

for file in files:
    print("=" * 60)
    print(file.name)
    
    with open(file, "r", encoding="utf-8") as f:
        text = f.read()

    print(text[:1500])   # preview first chunk
    print("\n")
