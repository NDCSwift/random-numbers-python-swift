# 🎲 How random Actually Works in Software

Every Python and Swift example from the video — runnable, annotated, and ready to clone.

---

## 🤔 What this is

A companion code repo for the *How random Actually Works in Software* video. It covers the full spectrum from unseeded Mersenne Twister calls to cryptographically secure entropy — in both Python and Swift. Every file maps to a specific chapter timestamp so you can follow along or run examples independently.

## ✅ Why you'd use it

- **Side-by-side languages** — the same concepts implemented in both Python and Swift so you can see how each language shapes the API
- **Runnable in minutes** — all Python examples use only the standard library; most Swift files run straight from the terminal with no setup
- **PoE crafting spectrum** — four isolated files (chaos → fossil → essence → bench) that each demonstrate a different point on the randomness dial

## 📺 Watch on YouTube

[![Watch on YouTube](https://img.shields.io/badge/YouTube-Watch%20the%20Tutorial-red?style=for-the-badge&logo=youtube)](https://youtu.be/vynD4hKga9M)

> This project was built for the [NoahDoesCoding YouTube channel](https://www.youtube.com/@NoahDoesCoding97).

---

## 🚀 Getting Started

### 1. Clone

```bash
git clone https://github.com/NDCSwift/random-numbers-python-swift.git
cd random-numbers-python-swift
```

### 2. Run Python examples

```bash
python3 python/01_hook.py
python3 python/02_ml_shuffle.py
python3 python/03_uuid_demo.py
python3 python/04_world_gen.py
python3 python/05_crafting_spectrum.py
python3 python/06_secrets_demo.py
```

### 3. Run Swift examples

```bash
swift swift/01_random_basics.swift
swift swift/03_secure_random.swift
# 02_mersenne_twister.swift → paste into an Xcode Playground
```

---

## Python

| File | Chapter | What it covers |
|---|---|---|
| `01_hook.py` | 0:00 | Unseeded vs seeded — the opening split-screen demo |
| `02_ml_shuffle.py` | 1:30 | Training data shuffles, unseeded and seeded |
| `03_uuid_demo.py` | 2:15 | UUID4 and why it uses OS entropy, not Mersenne Twister |
| `04_world_gen.py` | 5:00 | Seed-driven world generator with isolated `random.Random` instance |
| `05_crafting_spectrum.py` | 8:00 | All four PoE tiers together — the full randomness dial |
| `poe/chaos.py` | 8:00 | Chaos Orb — pure `random.sample`, full pool, equal weight |
| `poe/fossils.py` | 9:00 | Metallic + Scorched Fossil — blocked mods at weight 0, fire/lightning boosted |
| `poe/essence.py` | 10:00 | Essence of Spite — guaranteed mod + 5 weighted random fills |
| `poe/bench.py` | 11:00 | Crafting Bench — you pick the mod, `randint` rolls the value within a tier |
| `06_secrets_demo.py` | 11:00 | `random` vs `secrets` — same output format, different guarantee |

---

## Swift

| File | Chapter | What it covers |
|---|---|---|
| `01_random_basics.swift` | 1:30 | `Int.random`, `shuffle()`, `randomElement()` — hardware entropy by default |
| `02_mersenne_twister.swift` | 5:00 | `GKMersenneTwisterRandomSource` — seeded, deterministic, Xcode only |
| `03_secure_random.swift` | 11:00 | `SecRandomCopyBytes` — the Swift equivalent of `secrets` |

---

## 🛠️ Notes

- `02_mersenne_twister.swift` requires Xcode — paste it into a new Playground with GameplayKit available. It will not compile from the terminal.
- The `poe/` subfolder contains individual focused files for each crafting mechanic. `05_crafting_spectrum.py` runs all four together with a shared mod pool.
- All Python examples use only the standard library (`random`, `uuid`, `secrets`). No packages to install.

## 📦 Requirements

**Python** — 3.6 or later (all examples use only the standard library)

**Swift** — `01_random_basics.swift` and `03_secure_random.swift` run from the terminal. `02_mersenne_twister.swift` requires Xcode with GameplayKit.

---

## Quick Reference

### Python `random` module
| Function | Notes |
|---|---|
| `random.seed(n)` | Fix the starting state — same seed always produces the same sequence |
| `random.Random(seed)` | Isolated instance — does not share state with the global `random` module |
| `random.random()` | Float in `[0.0, 1.0)` |
| `random.randint(a, b)` | Integer in `[a, b]` inclusive |
| `random.shuffle(list)` | In-place shuffle — seed first for reproducible ML experiments |
| `random.sample(pop, k)` | k unique items, no replacement — use for loot pools |
| `random.choices(pop, weights, k)` | Weighted selection with replacement — use for shaped distributions |
| `random.getrandbits(n)` | n random bits — fast, but Mersenne Twister output, not for security |

### Python `uuid` module
| Function | Notes |
|---|---|
| `uuid.uuid4()` | Random UUID using OS hardware entropy (`os.urandom`) — not Mersenne Twister |

### Python `secrets` module
| Function | Notes |
|---|---|
| `secrets.token_hex(n)` | n bytes as a hex string — 32 bytes → 64 characters |
| `secrets.token_urlsafe(n)` | URL-safe base64 string — use for session tokens and API keys |
| `secrets.token_bytes(n)` | Raw bytes — use for encryption key material |

### Swift
| API | Notes |
|---|---|
| `Int.random(in:)` | Uses `SystemRandomNumberGenerator` (hardware entropy) by default |
| `array.shuffle()` | In-place, hardware entropy by default |
| `GKMersenneTwisterRandomSource(seed:)` | Seeded, deterministic — `import GameplayKit`, Xcode only |
| `SecRandomCopyBytes` | Cryptographic-grade random bytes — `import Security` |

---

## Common Mistakes

**"My session tokens are predictable"**
Using `random.getrandbits()` for tokens. Fix: `secrets.token_hex(32)`.

**"My world generates the same terrain every run"**
Not passing a seed to `random.Random()`. Fix: `rng = random.Random(seed)` inside the generator and use `rng` for every call.

**"random.seed() is changing unrelated parts of my program"**
Using the global `random` module — shared state means any call anywhere affects the sequence. Fix: `random.Random(seed)` for an isolated instance per system.

**"My tests are non-deterministic"**
Game logic or world generation using global `random` state. Fix: inject a `random.Random(seed)` instance so tests are reproducible regardless of what else runs.

**"secrets.token_hex(32) — why 64 characters?"**
The argument is bytes, not characters. Hex encoding is 2 characters per byte. If you need a specific character count, divide by 2: `secrets.token_hex(16)` → 32 characters.

---

## The Rule

```
if a value needs to be unpredictable to an adversary → secrets
everything else                                      → random is fine
```

---

📺 [Watch the guide on YouTube](https://youtu.be/vynD4hKga9M)
