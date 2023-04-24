import random
from math import gcd

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    # Use extended Euclidean algorithm to find the modular inverse of e
    d = pow(e, -1, phi)

    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    # Unpack the key into its components
    e, n = pk

    # Convert each letter in the plaintext to its corresponding ASCII value
    plaintext_ascii = [ord(c) for c in plaintext]

    # Encrypt each ASCII value using the public key
    ciphertext = [pow(m, e, n) for m in plaintext_ascii]

    # Return the encrypted message as a string
    return ''.join([chr(c) for c in ciphertext])

def decrypt(pk, ciphertext):
    # Unpack the key into its components
    d, n = pk

    # Convert each character in the ciphertext to its corresponding ASCII value
    ciphertext_ascii = [ord(c) for c in ciphertext]

    # Decrypt each ASCII value using the private key
    plaintext = [pow(c, d, n) for c in ciphertext_ascii]

    # Return the decrypted message as a string
    return ''.join([chr(p) for p in plaintext])

# Choose two prime numbers
p = 61
q = 53

# Generate a keypair using the primes
public_key, private_key = generate_keypair(p, q)

# Encrypt a message using the public key
plaintext = "Hello, world!"
ciphertext = encrypt(public_key, plaintext)

# Decrypt the message using the private key
decrypted_text = decrypt(private_key, ciphertext)

print(decrypted_text)  # Output: "Hello, world!"