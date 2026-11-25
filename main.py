#!/usr/bin/env python3
"""The Best Meal You Ever Had — one sentence that makes the meal feel real."""
import os

LINE = "My grandmother's rendang, slow-cooked until the coconut milk broke into oil, eaten with my fingers on her porch while the rain hammered the tin roof."
assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
