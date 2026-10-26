
import hashlib

def sha1(text):
    return hashlib.sha1(text.encode()).hexdigest()


while True:
    print("\n--- SHA-1 MENU ---")
    print("1. Generate SHA-1 Hash")
    print("2. Demonstrate Avalanche Effect")
    print("3. Compare Two Messages")
    print("4. Demonstrate Padding")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        text = input("Enter message: ")
        print("Original Message:", text)
        print("SHA-1 Hash:", sha1(text))

    elif choice == '2':
        text = input("Enter message: ")

        if text == "":
            print("Enter a non-empty message!")
            continue

        modified = input("Enter modified message (change one character): ")

        print("Original Hash:", sha1(text))
        print("Modified Hash:", sha1(modified))

    elif choice == '3':
        text1 = input("Enter first message: ")
        text2 = input("Enter second message: ")

        hash1 = sha1(text1)
        hash2 = sha1(text2)

        print("First Hash:", hash1)
        print("Second Hash:", hash2)

        if hash1 == hash2:
            print("Messages are identical")
        else:
            print("Messages are different")

    elif choice == '4':
        text = input("Enter a sentence: ")

        binary = ''.join(format(b, '08b') for b in text.encode())
        length = len(binary)

        padded = binary + '1'

        while len(padded) % 512 != 448:
            padded += '0'

        padded += format(length, '064b')

        print("Original Binary:", binary)
        print("Padded Message:", padded)
        print("Total 512-bit Blocks:", len(padded) // 512)
        print("SHA-1 Hash:", sha1(text))

    elif choice == '5':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")
