import random

# --- Unseeded shuffle: different order every run ---
# The model must see samples in a different order each epoch
# or it starts learning the order instead of the patterns.
training_data = list(range(100))

print("Before:", training_data[:8])

random.shuffle(training_data)   # Mersenne Twister, OS-seeded by default
print("After: ", training_data[:8])   # different every run

print()

# --- Seeded shuffle: same order every run ---
# Seed before shuffling when you need to:
#   - reproduce a training run exactly
#   - share results with a collaborator
#   - debug a run from last week
random.seed(42)
training_data = list(range(100))
random.shuffle(training_data)

print("Seeded (42):", training_data[:8])   # same on every machine, every run

random.seed(42)
training_data = list(range(100))
random.shuffle(training_data)

print("Seeded (42):", training_data[:8])   # identical — proof
