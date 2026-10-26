
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

private_key = None
public_key = None


def generate_keys():
    global private_key, public_key

    key = RSA.generate(2048)
    private_key = key
    public_key = key.publickey()

    with open("private.pem", "wb") as f:
        f.write(private_key.export_key())

    with open("public.pem", "wb") as f:
        f.write(public_key.export_key())

    print("RSA Keys Generated Successfully!")
    print("Private Key:\n", private_key.export_key().decode())
    print("Public Key:\n", public_key.export_key().decode())


def sign_message():
    if private_key is None:
        print("Generate keys first!")
        return

    message = input("Enter message: ")
    digest = SHA256.new(message.encode())
    signature = pkcs1_15.new(private_key).sign(digest)

    print("Message:", message)
    print("SHA-256 Digest:", digest.hexdigest())
    print("Digital Signature:", signature.hex())


def verify_signature():
    if public_key is None:
        print("Generate keys first!")
        return

    message = input("Enter original message: ")
    signature = input("Enter digital signature (hex): ")

    try:
        signature = bytes.fromhex(signature)
        digest = SHA256.new(message.encode())
        pkcs1_15.new(public_key).verify(digest, signature)
        print("Signature is VALID")
    except (ValueError, TypeError):
        print("Signature is INVALID")


def tampering():
    if private_key is None or public_key is None:
        print("Generate keys first!")
        return

    message = input("Enter message: ")

    digest = SHA256.new(message.encode())
    signature = pkcs1_15.new(private_key).sign(digest)

    modified = message + "X"

    print("Original Message:", message)
    print("Modified Message:", modified)

    try:
        pkcs1_15.new(public_key).verify(
            SHA256.new(modified.encode()), signature
        )
        print("Signature is VALID")
    except (ValueError, TypeError):
        print("Signature is INVALID - Message was modified!")


while True:
    print("\n===== DIGITAL SIGNATURE SYSTEM =====")
    print("1. Generate RSA Keys")
    print("2. Sign a Message")
    print("3. Verify a Signature")
    print("4. Demonstrate Message Tampering")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        generate_keys()
    elif choice == '2':
        sign_message()
    elif choice == '3':
        verify_signature()
    elif choice == '4':
        tampering()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice!")

