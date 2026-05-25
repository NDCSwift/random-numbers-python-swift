import random

# Chaos Orb — pure RNG, full pool
mod_pool = ["fire damage", "cold damage", "life", "mana",
            "attack speed", "crit chance", "lightning res"]

result = random.sample(mod_pool, k=4)
print(result)
# ['mana', 'fire damage', 'crit chance', 'cold damage'] — different every run
