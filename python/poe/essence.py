import random

# Essence of Spite on a weapon
# Guarantees: #% increased Global Accuracy Rating
# Remaining 5 mod slots roll from the normal weapon pool

guaranteed = "% increased Global Accuracy Rating"   # essence forces exactly this

mods    = ["added physical damage", "attack speed", "critical strike chance", "critical strike multiplier",
           "added fire damage",     "added cold damage", "added lightning damage",
           "elemental damage with attacks", "life on hit", "mana on hit"]
weights = [20,                       15,             15,                      10,
           10,                       10,              10,
           8,                        7,               5]

random_mods = random.choices(mods, weights, k=5)

result = [guaranteed] + random_mods
print(result)
