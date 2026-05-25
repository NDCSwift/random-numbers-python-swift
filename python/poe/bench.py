import random

# Crafting Bench — deterministic mod, random value within tier range
# Adds exactly one chosen mod to an item with open prefix/suffix slots

existing_mods = ["added physical damage", "attack speed", "critical strike chance"]

crafted_mod_value = random.randint(18, 25)
crafted_mod = f"+{crafted_mod_value} to Strength"

result = existing_mods + [crafted_mod]
print(result)
