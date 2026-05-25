import random


def generate_world(seed, width=40, height=12):
    # Private instance — does not touch or affect global random state.
    # If two systems both call random.seed(), they step on each other.
    # random.Random(seed) gives each system its own isolated chain.
    rng = random.Random(seed)

    tiles   = ['~', '.', '.', '^', 'T', '#']
    weights = [0.1, 0.4, 0.2, 0.1, 0.1, 0.1]
    # ~ water  . grass  ^ mountain  T tree  # stone

    world = []
    for _ in range(height):
        row = [rng.choices(tiles, weights=weights)[0] for _ in range(width)]
        world.append(''.join(row))

    return world


# --- Same seed → same world, every run, every machine ---
print("=== SEED: 12345 ===")
for row in generate_world(12345):
    print(row)

print()

# --- One integer apart → completely different world ---
print("=== SEED: 12346 ===")
for row in generate_world(12346):
    print(row)

print()

# --- Run generate_world(12345) again to prove determinism ---
print("=== SEED: 12345 again ===")
for row in generate_world(12345):
    print(row)
