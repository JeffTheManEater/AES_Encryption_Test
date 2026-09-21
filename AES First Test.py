import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# 1. Generate a secure random 256-bit key (32 bytes)
key = AESGCM.generate_key(bit_length=256)
aesgcm = AESGCM(key)

# 2. Prepare the data (must be in bytes)
secret_message = b"This is a highly confidential message0o000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000."

# 3. Generate a unique 96-bit Nonce (Initialization Vector)
# NEVER reuse a nonce with the same key


for i in range(5):
    nonce_int = int.from_bytes(os.urandom(12), "big")
    nonce = (nonce_int+1).to_bytes(12, "big")
    crypto_thingy = aesgcm.encrypt(nonce, secret_message, associated_data=None)
    print(crypto_thingy)
    crypto_thingy = aesgcm.decrypt(nonce, crypto_thingy, associated_data=None)
    print(f"{crypto_thingy}\n")