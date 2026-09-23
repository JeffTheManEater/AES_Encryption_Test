import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives import hashes, serialization

secret_message = b"secret tunnel"
key = AESGCM.generate_key(bit_length=256)

def display_rsa_keys(first_add, private_key_local, mid_add, public_key_local, last_add):
    private_pem = private_key_local.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    public_pem = public_key_local.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    print(f"{first_add}{private_pem}{mid_add}{public_pem}{last_add}")

for i in range(1):
    print(f"\nAES Key: {key}")

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=4096,
    )
    public_key = private_key.public_key()

    display_rsa_keys("\n", private_key, "\n", public_key, "\n")

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
    nonce_int = int.from_bytes(os.urandom(12), 
                               "big")
    nonce = (nonce_int+i).to_bytes(12, 
                                   "big")
    crypto_thingy = aesgcm.encrypt(nonce, 
                                   secret_message, 
                                   associated_data=None)
    print(f"\nnonce + {i} = {nonce}\nAES-GCM Key: {key}\nEncrypted Message: {crypto_thingy}")
    crypto_thingy = aesgcm.decrypt(nonce, 
                                   crypto_thingy, 
                                   associated_data=None)
    print(f"Decrypted Message: {crypto_thingy}\n")