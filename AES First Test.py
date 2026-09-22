import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives import hashes

secret_message = b"secret tunnel"
key = AESGCM.generate_key(bit_length=256)

for i in range(5):
    print(f"\nAES Key: {key}")

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=4096,
    )
    public_key = private_key.public_key()
    print(f"\nPrivate Key: {private_key}\nPublic Key: {public_key}")

    encrypted_key = public_key.encrypt(
        key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print(f"Encrypted Key: {encrypted_key}")

    decrypted_key = private_key.decrypt(
        encrypted_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    print(f"Decrypted Key: {decrypted_key}")

    aesgcm = AESGCM(decrypted_key)
    nonce_int = int.from_bytes(os.urandom(12), "big")
    nonce = (nonce_int+i).to_bytes(12, "big")
    crypto_thingy = aesgcm.encrypt(nonce, secret_message, associated_data=None)
    print(f"\nnonce + {i} = {nonce}\nAES-GCM Key: {key}\nEncrypted Message: {crypto_thingy}")
    crypto_thingy = aesgcm.decrypt(nonce, crypto_thingy, associated_data=None)
    print(f"Decrypted Message:{crypto_thingy}\n")