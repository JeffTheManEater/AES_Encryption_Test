import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# 1. Generate a secure random 256-bit key (32 bytes)
key = AESGCM.generate_key(bit_length=256)
aesgcm = AESGCM(key)

# 2. Prepare the data (must be in bytes)
secret_message = b"This is a highly confidential message."

# 3. Generate a unique 96-bit Nonce (Initialization Vector)
# NEVER reuse a nonce with the same key
nonce_1 = os.urandom(12)
nonce_2 = os.urandom(12)

# 4. Encrypt the data
ciphertext_nonce_1_1 = aesgcm.encrypt(nonce_1, secret_message, associated_data=None)
print(f"Ciphertext: {ciphertext_nonce_1_1.hex()}")

ciphertext_nonce_1_2 = aesgcm.encrypt(nonce_1, secret_message, associated_data=None)
print(f"Ciphertext: {ciphertext_nonce_1_2.hex()}")

if ciphertext_nonce_1_1 == ciphertext_nonce_1_2:
    print("Same")
else:
    print("Different")

# 4. Encrypt the data
ciphertext_nonce_2_1 = aesgcm.encrypt(nonce_2, secret_message, associated_data=None)
print(f"Ciphertext: {ciphertext_nonce_2_1.hex()}")

ciphertext_nonce_2_2 = aesgcm.encrypt(nonce_2, secret_message, associated_data=None)
print(f"Ciphertext: {ciphertext_nonce_2_2.hex()}")

if ciphertext_nonce_2_1 == ciphertext_nonce_2_2:
    print("Same")
else:
    print("Different")g