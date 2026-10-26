from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Input
plaintext = input("Enter the plaintext: ")
key = input("Enter a 16-byte secret key: ")

# AES-128 requires a 16-byte key
if len(key) != 16:
    print("Error: Key must be exactly 16 characters (16 bytes).")
    exit()

key = key.encode()

# Create AES cipher (ECB mode)
cipher = AES.new(key, AES.MODE_ECB)

# Encrypt
padded_text = pad(plaintext.encode(), AES.block_size)
ciphertext = cipher.encrypt(padded_text)

# Decrypt
decipher = AES.new(key, AES.MODE_ECB)
decrypted = unpad(decipher.decrypt(ciphertext), AES.block_size)

# Output
print("\n----- OUTPUT -----")
print("Plaintext           :", plaintext)
print("Secret Key          :", key.decode())
print("Ciphertext (Hex)    :", ciphertext.hex().upper())
print("Decrypted Plaintext :", decrypted.decode())

# Verification
if plaintext == decrypted.decode():
    print("Verification        : Successful! Plaintext matches.")
else:
    print("Verification        : Failed!")
