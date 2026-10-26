
text = input("Enter the text: ").upper()
key = int(input("Enter the key: "))

cipher = ""

for ch in text:
    if ch.isalpha():
        cipher += chr((ord(ch) - 65 + key) % 26 + 65)
    else:
        cipher += ch

print("Encrypted text:", cipher)

plain = ""

for ch in cipher:
    if ch.isalpha():
        plain += chr((ord(ch) - 65 - key) % 26 + 65)
    else:
        plain += ch

print("Decrypted text:", plain)
