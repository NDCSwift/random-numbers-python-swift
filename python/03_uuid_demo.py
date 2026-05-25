import uuid
import random

# --- UUID4: OS hardware entropy, not Mersenne Twister ---
# Every call reaches down through Python → os.urandom() → /dev/urandom
# → kernel entropy pool → CPU thermal noise, interrupt timing, disk jitter.
# No seed. No state to reconstruct. Different every call.
print("=== UUID4 (hardware entropy) ===")
print(uuid.uuid4())
print(uuid.uuid4())
print(uuid.uuid4())

print()

# --- Contrast: seeded random.getrandbits formatted as hex ---
# Same output FORMAT as a UUID, but from the Mersenne Twister.
# Predictable if you know the seed or have observed enough output.
random.seed(42)
print("=== Mersenne Twister (seeded, same format) ===")
fake_id = f"{random.getrandbits(32):08x}-{random.getrandbits(16):04x}-" \
          f"{random.getrandbits(16):04x}-{random.getrandbits(16):04x}-" \
          f"{random.getrandbits(48):012x}"
print(fake_id)  # looks like a UUID — reproducible with seed 42

# The point: the output format tells you nothing about the path that produced it.
