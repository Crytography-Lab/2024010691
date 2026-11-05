from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes

private_key = dsa.generate_private_key(key_size=2048)
public_key = private_key.public_key()

message = input("Enter message: ").encode()

signature = private_key.sign(
    message,
    hashes.SHA256()
)

print("\nDigital Signature:")
print(signature.hex())

try:
    public_key.verify(
        signature,
        message,
        hashes.SHA256()
    )
    print("\nSignature is valid!")
except Exception:
    print("\nSignature is invalid!")
