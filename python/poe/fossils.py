import random

# Metallic + Scorched Fossils in a 2-socket resonator
# Metallic: more lightning mods,  no physical mods
# Scorched: more fire mods,       no cold mods
# Combined: fire and lightning boosted — physical and cold blocked entirely

mods    = ["fire damage", "fire res", "lightning damage", "lightning res", "life", "attack speed", "physical damage", "physical as extra", "cold damage",   "cold res"]
weights = [35,             25,         35,                  25,              10,     10,              0,                  0,                   0,              0]
#                                                                                                         ^-- blocked by Metallic                  ^-- blocked by Scorched

result = random.choices([m for m, w in zip(mods, weights) if w > 0],
                        [w for w in weights if w > 0], k=4)
print(result)
