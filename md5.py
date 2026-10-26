
import hashlib
import os

def md5(text):
    return hashlib.md5(text.encode()).hexdigest()

while True:
    print("\n--- MD5 MENU ---")
    print("1. Generate MD5 Digest")
    print("2. Verify Message Integrity")
    print("3. Avalanche Effect")
    print("4. MD5 Checksum for File")
    print("5. Compare MD5, SHA-1 and SHA-256")
    print("6. Exit")

    ch = input("Enter choice: ")

    if ch == '1':
        text = input("Enter message: ")
        print("MD5 Digest:", md5(text))

    elif ch == '2':
        text = input("Enter message: ")
        old = input("Enter previous digest: ")

        if md5(text) == old.lower():
            print("Message Matches")
        else:
            print("Message Does Not Match")

    elif ch == '3':
        text1 = input("Enter first message: ")
        text2 = input("Enter modified message: ")

        print("First MD5:", md5(text1))
        print("Second MD5:", md5(text2))

    elif ch == '4':
        path = input("Enter file path: ")

        try:
            with open(path, 'rb') as f:
                data = f.read()
            print("File MD5:", hashlib.md5(data).hexdigest())
        except FileNotFoundError:
            print("File not found!")

    elif ch == '5':
        text = input("Enter message: ")
        data = text.encode()

        print("MD5:", hashlib.md5(data).hexdigest())
        print("SHA-1:", hashlib.sha1(data).hexdigest())
        print("SHA-256:", hashlib.sha256(data).hexdigest())

    elif ch == '6':
        print("Exiting...")
        break

    else:
        print("Invalid choice!")

