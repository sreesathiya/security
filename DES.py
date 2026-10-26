from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# Accept plaintext
plaintext = input("Enter the plaintext: ")

# Accept 8-byte key
key = input("Enter an 8-byte secret key: ")

# Ensure the key is exactly 8 bytes
if len(key) != 8:
    print("Error: DES key must be exactly 8 characters (8 bytes).")
    exit()

key = key.encode()

# Create DES cipher (ECB mode)
cipher = DES.new(key, DES.MODE_ECB)

# Encrypt
padded_text = pad(plaintext.encode(), DES.block_size)
ciphertext = cipher.encrypt(padded_text)

# Decrypt
decipher = DES.new(key, DES.MODE_ECB)
decrypted = unpad(decipher.decrypt(ciphertext), DES.block_size)

# Display Results
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
