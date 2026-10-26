from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

plaintext = input("Enter plaintext: ")
key = input("Enter 16-byte key: ")

if len(key) != 16:
    print("Key must be 16 characters!")
    exit()

key = key.encode()

cipher = AES.new(key, AES.MODE_ECB)

ciphertext = cipher.encrypt(pad(plaintext.encode(), 16))

decipher = AES.new(key, AES.MODE_ECB)

decrypted = unpad(decipher.decrypt(ciphertext), 16)

print("Ciphertext:", ciphertext.hex())
print("Decrypted:", decrypted.decode())

#CBC MODE

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

plaintext = input("Enter plaintext: ")
key = input("Enter 16-byte key: ")

if len(key) != 16:
    print("Key must be 16 characters!")
    exit()

key = key.encode()

iv = b'1234567890123456'

cipher = AES.new(key, AES.MODE_CBC, iv)

ciphertext = cipher.encrypt(pad(plaintext.encode(), 16))

decipher = AES.new(key, AES.MODE_CBC, iv)

decrypted = unpad(decipher.decrypt(ciphertext), 16)

print("Ciphertext:", ciphertext.hex())
print("Decrypted:", decrypted.decode())

#CFB MODE

from Crypto.Cipher import AES

plaintext = input("Enter plaintext: ")
key = input("Enter 16-byte key: ")

if len(key) != 16:
    print("Key must be 16 characters!")
    exit()

key = key.encode()

iv = b'1234567890123456'

cipher = AES.new(key, AES.MODE_CFB, iv, segment_size=128)

ciphertext = cipher.encrypt(plaintext.encode())

decipher = AES.new(key, AES.MODE_CFB, iv, segment_size=128)

decrypted = decipher.decrypt(ciphertext)

print("Ciphertext:", ciphertext.hex())
print("Decrypted:", decrypted.decode())

#OFB MODE

from Crypto.Cipher import AES

plaintext = input("Enter plaintext: ")
key = input("Enter 16-byte key: ")

if len(key) != 16:
    print("Key must be 16 characters!")
    exit()

key = key.encode()

iv = b'1234567890123456'

cipher = AES.new(key, AES.MODE_OFB, iv)

ciphertext = cipher.encrypt(plaintext.encode())

decipher = AES.new(key, AES.MODE_OFB, iv)

decrypted = decipher.decrypt(ciphertext)

print("Ciphertext:", ciphertext.hex())
print("Decrypted:", decrypted.decode())


#CTR MODE

from Crypto.Cipher import AES

plaintext = input("Enter plaintext: ")
key = input("Enter 16-byte key: ")

if len(key) != 16:
    print("Key must be 16 characters!")
    exit()

key = key.encode()

nonce = b'12345678'

cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)

ciphertext = cipher.encrypt(plaintext.encode())

decipher = AES.new(key, AES.MODE_CTR, nonce=nonce)

decrypted = decipher.decrypt(ciphertext)

print("Ciphertext:", ciphertext.hex())
print("Decrypted:", decrypted.decode())

#GCM MODE

from Crypto.Cipher import AES

plaintext = input("Enter plaintext: ")
key = input("Enter 16-byte key: ")

if len(key) != 16:
    print("Key must be 16 characters!")
    exit()

key = key.encode()

nonce = b'123456789012'

cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)

ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode())

decipher = AES.new(key, AES.MODE_GCM, nonce=nonce)

decrypted = decipher.decrypt_and_verify(ciphertext, tag)

print("Ciphertext:", ciphertext.hex())
print("Authentication Tag:", tag.hex())
print("Decrypted:", decrypted.decode())
print("Verification: Successful!")