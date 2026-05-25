// Run this file: swift 01_random_basics.swift
// Requires: macOS 10.15+ or Swift 5.5+

import Foundation

// Swift's default random uses SystemRandomNumberGenerator under the hood —
// hardware entropy, the same path as secrets in Python.
// That's the default. To get a seeded, reproducible PRNG you have to ask explicitly.

print("=== Unseeded: different every run ===")
let roll1 = Int.random(in: 1...6)
let roll2 = Int.random(in: 1...6)
let roll3 = Int.random(in: 1...6)
print(roll1, roll2, roll3)

print()

// Ranges, floats, booleans — all use hardware entropy by default
print("=== Different types ===")
print(Double.random(in: 0..<1))
print(Bool.random())
print(Int.random(in: 1...100))

print()

// Shuffling an array — in-place and returning a new copy
var deck = Array(1...10)
deck.shuffle()
print("Shuffled:", deck)

let original = Array(1...10)
let shuffled = original.shuffled()
print("Shuffled copy:", shuffled)

print()

// Random element from a collection
let loot = ["sword", "shield", "potion", "gold", "nothing"]
if let drop = loot.randomElement() {
    print("Loot drop:", drop)
}
