import random

# --- Unseeded: OS picks the starting point ---
# Run this on two machines and you get different output.
# Same Python version, same code, different numbers.
print("=== UNSEEDED ===")
print(random.random())
print(random.randint(1, 10))

print()

# --- Seeded: you pick the starting point ---
# Run this on two machines and you get identical output.
random.seed(42)
print("=== SEED 42 — run 1 ===")
print(random.random())
print(random.randint(1, 10))
print(random.randint(1, 100))

print()

# Reset to the same seed and the chain starts over
random.seed(42)
print("=== SEED 42 — run 2 ===")
print(random.random())       # identical to run 1
print(random.randint(1, 10))
print(random.randint(1, 100))
