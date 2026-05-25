import random

# The Randomness Dial
# Games use a spectrum from pure chaos to full control.
# Each step gives the player more agency — and a different emotional feel.

MOD_POOL = {
    "fire damage":    10,
    "cold damage":    10,
    "lightning res":  10,
    "life":           15,
    "attack speed":   12,
    "crit chance":    10,
    "physical damage": 8,
    "mana":            8,
    "life on hit":     7,
    "cold res":       10,
}

def weighted_sample(pool: dict, blocked: set = None, k: int = 4) -> list:
    items = [(mod, w) for mod, w in pool.items() if mod not in (blocked or set())]
    mods, weights = zip(*items)
    seen, result = set(), []
    while len(result) < k:
        pick = random.choices(mods, weights)[0]
        if pick not in seen:
            seen.add(pick)
            result.append(pick)
    return result


# ── 1. Pure Chaos ─────────────────────────────────────────────────────────────
# Full pool, equal weight, no guarantees. High variance. Exciting and brutal.
def chaos() -> list:
    return random.sample(list(MOD_POOL), k=4)


# ── 2. Weighted + Filtered ────────────────────────────────────────────────────
# Some mods are more likely; some are blocked entirely.
# Players can target a theme but can't pin down a specific outcome.
def fossil(boost: set, block: set) -> list:
    pool = {m: (w * 3 if m in boost else w) for m, w in MOD_POOL.items()}
    return weighted_sample(pool, blocked=block, k=4)


# ── 3. Guaranteed + Random ────────────────────────────────────────────────────
# One slot is locked in. The rest still roll randomly.
# Feels like progress — you secured the important mod, now gamble the rest.
def essence(guaranteed: str) -> list:
    rest = weighted_sample(MOD_POOL, blocked={guaranteed}, k=3)
    return [guaranteed] + rest


# ── 4. Controlled Craft ───────────────────────────────────────────────────────
# You choose the mod. The game chooses the roll within a tier.
# Minimal variance. Satisfying precision.
def bench_craft(mod: str, tier: tuple) -> str:
    value = random.randint(*tier)
    return f"+{value} {mod}"


# ── Demo ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=== The Randomness Dial ===\n")

    print("[1] Pure Chaos — anything goes")
    print("   ", chaos())

    print("\n[2] Fossil Craft — fire/lightning boosted, cold/physical blocked")
    print("   ", fossil(boost={"fire damage", "lightning res"}, block={"cold damage", "cold res", "physical damage"}))

    print("\n[3] Essence — 'life' guaranteed, 3 random fills")
    print("   ", essence("life"))

    print("\n[4] Bench Craft — you pick the mod, RNG picks the value")
    print("   ", bench_craft("to maximum life", tier=(60, 79)))

    print()
    print("Dial:  chaos ──────── weighted ──────── guaranteed ──────── controlled")
    print("Feel:  exciting       targeted           progress             precise")
