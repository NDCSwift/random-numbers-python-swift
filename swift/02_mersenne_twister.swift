// Paste into an Xcode Playground with GameplayKit linked,
// or add to an Xcode target (GameplayKit is linked automatically on Apple platforms).
// GameplayKit is NOT available as a standalone swift file — it requires Xcode.

import GameplayKit

// GKMersenneTwisterRandomSource is the Swift equivalent of random.Random(seed) in Python.
// Deterministic and reproducible — designed for game logic, not security.
// GameplayKit names it explicitly so you know exactly what you're getting.

let seeded = GKMersenneTwisterRandomSource(seed: 42)

let r1 = seeded.nextInt(upperBound: 6) + 1
let r2 = seeded.nextInt(upperBound: 6) + 1
let r3 = seeded.nextInt(upperBound: 6) + 1

print("Seeded rolls:", r1, r2, r3)   // same three values every run

// Create a second source with the same seed — proves determinism
let seeded2 = GKMersenneTwisterRandomSource(seed: 42)

let s1 = seeded2.nextInt(upperBound: 6) + 1
let s2 = seeded2.nextInt(upperBound: 6) + 1
let s3 = seeded2.nextInt(upperBound: 6) + 1

print("Same seed:  ", s1, s2, s3)   // identical

print()

// Shuffling an array with a seeded source
// GKRandomSource provides sharedRandom() for the unseeded equivalent
let items = ["fire damage", "cold damage", "life", "mana", "attack speed"]

let shuffledSeeded = GKMersenneTwisterRandomSource(seed: 99)
    .arrayByShufflingObjects(in: items) as! [String]

print("Seeded shuffle:", shuffledSeeded)

// Run again with same seed — same order
let shuffledAgain = GKMersenneTwisterRandomSource(seed: 99)
    .arrayByShufflingObjects(in: items) as! [String]

print("Same seed:     ", shuffledAgain)

print()

// Weighted distribution using GKGaussianDistribution
// Equivalent to random.choices() with a bell-curve weight
let distribution = GKGaussianDistribution(
    randomSource: GKMersenneTwisterRandomSource(seed: 42),
    mean: 50,
    deviation: 10
)

print("Gaussian rolls (mean 50, deviation 10):")
for _ in 0..<5 {
    print(distribution.nextInt())
}
