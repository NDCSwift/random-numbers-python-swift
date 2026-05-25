// Run this file: swift 03_secure_random.swift
// Requires: macOS 10.15+ — Security framework is available on all Apple platforms.

import Foundation
import Security

// SecRandomCopyBytes is the Swift equivalent of secrets.token_bytes() in Python.
// Reaches: Swift → Security framework → CCRandomGenerateBytes (macOS)
//          → kernel entropy pool → CPU thermal noise, interrupt timing.
// No seed. No state to reconstruct. Hardware entropy.

// --- 32 bytes of cryptographically secure random data ---
var bytes = [UInt8](repeating: 0, count: 32)   // allocate buffer

let status = SecRandomCopyBytes(kSecRandomDefault, bytes.count, &bytes)

if status == errSecSuccess {
    let hexToken = bytes.map { String(format: "%02hhx", $0) }.joined()
    print("Secure token:", hexToken)   // 64 hex characters = 32 bytes
} else {
    print("SecRandomCopyBytes failed — status:", status)
}

print()

// --- Generating multiple tokens to show they're all different ---
print("Three tokens (all different, none predictable from the others):")
for _ in 0..<3 {
    var buf = [UInt8](repeating: 0, count: 16)
    if SecRandomCopyBytes(kSecRandomDefault, buf.count, &buf) == errSecSuccess {
        print(buf.map { String(format: "%02hhx", $0) }.joined())
    }
}

print()

// --- Swift 5.9+ alternative: CryptoKit ---
// If your deployment target allows CryptoKit, this is cleaner:
//
// import CryptoKit
// let key = SymmetricKey(size: .bits256)   // 32 bytes hardware entropy
// print(key.withUnsafeBytes { Data($0).map { String(format: "%02hhx", $0) }.joined() })

// --- Comparison: SystemRandomNumberGenerator ---
// Int.random() uses SystemRandomNumberGenerator, which also reads hardware entropy.
// For generating random numbers in game logic, this is sufficient.
// For generating tokens that must be unguessable, SecRandomCopyBytes or CryptoKit
// are the explicit, auditable choices.
print("Int.random uses hardware entropy too — but SecRandomCopyBytes is")
print("the explicit, auditable choice for security-critical code.")
