import random
import secrets

# --- The wrong way: Mersenne Twister output formatted as hex ---
# Looks like a secure token. It is not.
# The published attack requires 624 observed integers to reconstruct
# the full internal state — after which every future value is predictable.
bad_token = hex(random.getrandbits(128))
print("random.getrandbits:", bad_token)

print()

# --- The right way: OS hardware entropy ---
# secrets.token_hex reaches: Python → os.urandom() → /dev/urandom
# → kernel entropy pool → CPU thermal noise, interrupt timing.
# No seed. No state. Even with complete output history, next value is unknowable.
good_token = secrets.token_hex(32)    # 32 bytes → 64 hex characters
print("secrets.token_hex: ", good_token)

print()

# --- Other secrets functions ---
# token_urlsafe: base64url encoding, safe for URLs and headers
url_token  = secrets.token_urlsafe(32)
print("secrets.token_urlsafe:", url_token)

# token_bytes: raw bytes when you need binary key material
raw_bytes  = secrets.token_bytes(32)
print("secrets.token_bytes: ", raw_bytes.hex())

print()

# --- Side-by-side to see they look identical in format ---
print("Both look like random hex. One is safe for adversarial contexts.")
print("MT  :", hex(random.getrandbits(128)))
print("CSPRNG:", secrets.token_hex(16))

# Rule: if a value needs to be unpredictable to an adversary → secrets.
#       Everything else → random is fine.
