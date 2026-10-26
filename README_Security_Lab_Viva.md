# Security Laboratory – Viva README

Simple revision notes for the Security Laboratory viva. This README covers the purpose, working, key mathematical ideas, bit sizes, key sizes, and important viva points for the algorithms listed below.

---

## 1. Basic Terms You Must Know

### Bit and byte
- **Bit:** The smallest unit of digital information; it is either `0` or `1`.
- **Byte:** 8 bits.
- **Example:** 128 bits = 16 bytes.

### Plaintext and ciphertext
- **Plaintext:** The original readable message.
- **Ciphertext:** The encrypted, unreadable message.
- **Encryption:** Converts plaintext into ciphertext.
- **Decryption:** Converts ciphertext back into plaintext.

### Symmetric and asymmetric cryptography
- **Symmetric encryption:** The sender and receiver use the same secret key. Examples: AES and DES.
- **Asymmetric cryptography:** Uses a public key and a private key. RSA is an example.
- **Hashing:** Produces a fixed-length digest from data. Standard hash functions such as MD5 and SHA-256 do not use an encryption key.
- **Digital signature:** Helps verify who signed a message and whether it was changed.
- **MAC/HMAC:** Uses a shared secret to check message integrity and authenticity.

### Prime number
A **prime number** is an integer greater than 1 that has only two positive factors: 1 and itself. Examples: 2, 3, 5, 7, 11.

### GCD
The **greatest common divisor (GCD)** is the largest number that divides two integers without a remainder.

Example: `gcd(12, 18) = 6`.

### Modulo
`a mod m` is the remainder when `a` is divided by `m`.

Example: `17 mod 5 = 2`.

### Modular inverse
The modular inverse of `a` modulo `m` is a number `x` such that:

`a × x mod m = 1`

It exists only when `gcd(a, m) = 1`.

### XOR
XOR compares two bits:
- `0 XOR 0 = 0`
- `0 XOR 1 = 1`
- `1 XOR 0 = 1`
- `1 XOR 1 = 0`

XOR is used in cryptographic operations, including DES.

---

## 2. Caesar Cipher

**Type:** Symmetric substitution cipher.

**Purpose:** Replaces each letter with another letter a fixed number of positions away in the alphabet.

**Working:**
1. Choose a shift key `K` from 0 to 25.
2. Convert each letter to a number: A = 0, B = 1, ..., Z = 25.
3. Encrypt using `C = (P + K) mod 26`.
4. Decrypt using `P = (C - K) mod 26`.

**Bit/key size:**
- No standard bit-based block size.
- For the 26-letter English alphabet, there are 26 possible shifts, including shift 0.
- The key can be represented using about 5 bits because 5 bits can represent 32 values.

**Viva points:**
- It is easy to understand but insecure.
- It can be broken by trying all 26 possible shifts.
- It is a substitution cipher because letters are replaced.

---

## 3. Playfair Cipher

**Type:** Symmetric digraph substitution cipher.

**Purpose:** Encrypts two letters at a time rather than one letter at a time.

**Working:**
1. Create a 5×5 matrix using a keyword.
2. Remove repeated letters from the keyword.
3. Fill the remaining spaces with the unused alphabet letters; I and J are usually combined.
4. Split plaintext into letter pairs. Repeated letters in a pair are normally separated with a filler such as X; an extra filler may be added if needed.
5. Apply the row, column, or rectangle rule:
   - Same row: replace each letter with the letter to its right for encryption.
   - Same column: replace each letter with the letter below it for encryption.
   - Rectangle: replace each letter with the letter in the same row and the other letter's column.
6. Decryption reverses the row and column directions; the rectangle rule is applied correspondingly.

**Bit/key size:**
- Processes two letters at a time; it has no standard binary block size.
- Key is a keyword used to construct the 5×5 matrix.
- The matrix has 25 positions because I and J are commonly combined.

**Viva points:**
- It is a classical cipher and is not secure for modern use.
- It encrypts pairs of letters, which makes it different from Caesar cipher.

---

## 4. Hill Cipher

**Type:** Symmetric matrix-based substitution cipher.

**Purpose:** Encrypts groups of letters using matrix multiplication modulo 26.

**Working:**
1. Convert letters to numbers from 0 to 25.
2. Arrange letters into a vector `P`.
3. Choose a square key matrix `K`.
4. Encrypt using `C = K × P mod 26`.
5. To decrypt, calculate the inverse matrix `K⁻¹` modulo 26.
6. Decrypt using `P = K⁻¹ × C mod 26`.

**Key condition:**
- The key matrix must be invertible modulo 26.
- Its determinant must satisfy `gcd(det(K), 26) = 1`.
- Because `26 = 2 × 13`, the determinant must not be divisible by 2 or 13.
- A prime number is not required to build the key matrix, but the GCD condition is essential.

**Bit/key size:**
- No fixed bit-based key size.
- The key is a square matrix; a common teaching example is a 2×2 matrix.

**Viva points:**
- The key is a matrix rather than a single number.
- If the matrix has no modular inverse, decryption will not work correctly.

---

## 5. Rail Fence Cipher

**Type:** Symmetric transposition cipher.

**Purpose:** Rearranges the positions of letters without changing the letters themselves.

**Working:**
1. Choose the number of rails.
2. Write the plaintext in a zigzag pattern across the rails.
3. Read the letters row by row to form ciphertext.
4. For decryption, reconstruct the zigzag pattern and read in the original order.

**Bit/key size:**
- No standard bit-based block or key size.
- The key is the number of rails.

**Viva points:**
- Unlike substitution ciphers, it does not replace letters.
- It changes the order of letters.

---

## 6. DES (Data Encryption Standard)

**Type:** Symmetric block cipher.

**Purpose:** Encrypts data using the same secret key for encryption and decryption.

**Working:**
1. Takes a 64-bit data block.
2. Applies an initial permutation.
3. Splits the block into two 32-bit halves.
4. Processes the halves through 16 Feistel rounds using round keys.
5. Applies the final permutation to produce ciphertext.
6. Decryption uses the same overall structure with round keys in reverse order.

**Bit/key sizes:**
- **Block size:** 64 bits.
- **Key input size:** 64 bits.
- **Effective key size:** 56 bits; the remaining 8 bits are parity bits.
- **Rounds:** 16.

**Viva points:**
- DES uses XOR and substitution/permutation operations.
- DES is considered insecure today because its effective key is too short and can be brute-forced.
- AES replaced DES for modern use.

---

## 7. AES (Advanced Encryption Standard)

**Type:** Symmetric block cipher.

**Purpose:** Encrypts fixed-size blocks using a secret key.

**Working:**
1. Takes a 128-bit data block.
2. Expands the key into round keys.
3. Performs an initial AddRoundKey operation.
4. Applies the main round operations: SubBytes, ShiftRows, MixColumns, and AddRoundKey.
5. The final round omits MixColumns.
6. Decryption uses the corresponding inverse operations.

**Bit/key sizes:**

| AES Version | Block Size | Key Size | Number of Rounds |
|---|---:|---:|---:|
| AES-128 | 128 bits | 128 bits | 10 |
| AES-192 | 128 bits | 192 bits | 12 |
| AES-256 | 128 bits | 256 bits | 14 |

**Viva points:**
- AES always uses a 128-bit block, regardless of key size.
- AES-256 means the key is 256 bits; the block is still 128 bits.
- AES is widely used for modern symmetric encryption.
- AES key generation does not use the RSA prime-number and GCD method.

---

## 8. RSA

**Type:** Asymmetric cryptographic algorithm.

**Purpose:** Can be used for encryption and digital signatures.

**Working/key generation:**
1. Choose two large distinct prime numbers, `p` and `q`.
2. Calculate `n = p × q`.
3. Calculate Euler's totient: `φ(n) = (p − 1)(q − 1)`.
4. Choose `e` such that `1 < e < φ(n)` and `gcd(e, φ(n)) = 1`.
5. Find `d` such that `e × d mod φ(n) = 1`.
6. Public key: `(e, n)`.
7. Private key: `(d, n)`.

**Basic textbook formulas:**
- Encryption: `C = M^e mod n`.
- Decryption: `M = C^d mod n`.

These formulas describe basic textbook RSA. Real systems must use secure padding schemes and appropriate libraries.

**Bit/key sizes:**
- RSA key size means the bit length of modulus `n`.
- Common sizes include **2048 bits** and **3072 bits**; **4096 bits** is also used.
- RSA has no fixed block size like AES; the permitted message size depends on the modulus and padding scheme.

**Viva points:**
- `p` and `q` must be prime.
- `gcd(e, φ(n)) = 1` ensures that the modular inverse `d` can be found.
- The public key can be shared; the private key must be kept secret.
- RSA is slower than AES, so practical systems often use RSA to protect or exchange a symmetric key rather than encrypt large amounts of data directly.

---

## 9. Diffie–Hellman Key Exchange

**Type:** Public-key key agreement method.

**Purpose:** Allows two people to establish a shared secret over a public channel. It does not directly encrypt the message.

**Working:**
1. Publicly agree on a large prime `p` and a suitable generator `g`.
2. Alice chooses private number `a` and calculates `A = g^a mod p`.
3. Bob chooses private number `b` and calculates `B = g^b mod p`.
4. They exchange public values `A` and `B`.
5. Alice calculates `K = B^a mod p`.
6. Bob calculates `K = A^b mod p`.
7. Both obtain the same shared secret because both values equal `g^(ab) mod p`.

**Bit/key sizes:**
- Finite-field Diffie–Hellman commonly uses a **2048-bit or larger prime group**, depending on security requirements.
- Elliptic-curve Diffie–Hellman (ECDH) uses elliptic-curve parameters instead; its sizes are different.
- There is no single fixed size for all Diffie–Hellman variants.

**Viva points:**
- Private values `a` and `b` are never sent over the network.
- Public values `A` and `B` are exchanged.
- The shared secret should normally be passed through a key-derivation function before use.
- Basic Diffie–Hellman does not authenticate the participants and can be vulnerable to a man-in-the-middle attack if used without authentication.

---

## 10. MD5

**Type:** Cryptographic hash function.

**Purpose:** Converts data of any length into a fixed-size digest.

**Working:**
1. Pad the message.
2. Append the message length according to MD5's format.
3. Process the padded message in 512-bit blocks.
4. Update the internal state through the compression function.
5. Produce the final hash.

**Bit sizes:**
- **Message block size:** 512 bits.
- **Hash output:** 128 bits, usually shown as 32 hexadecimal characters.
- **Key size:** None in standard MD5.

**Viva points:**
- Hashing is not encryption; there is no decryption key.
- MD5 is no longer secure for collision-resistant uses because collisions can be constructed.
- Do not use MD5 for modern digital signatures or security-sensitive integrity checks.

---

## 11. SHA-1

**Type:** Cryptographic hash function.

**Purpose:** Produces a fixed-size message digest.

**Working:**
1. Pad the message.
2. Append the message length.
3. Process the message in 512-bit blocks.
4. Update the internal hash state through 80 rounds per block.
5. Produce the final digest.

**Bit sizes:**
- **Message block size:** 512 bits.
- **Hash output:** 160 bits, usually shown as 40 hexadecimal characters.
- **Key size:** None in standard SHA-1.

**Viva points:**
- SHA-1 produces a longer digest than MD5, but it is also considered insecure for collision-resistant uses.
- It is a hash function, not an encryption algorithm.
- Do not use SHA-1 for new security-sensitive digital signatures.

---

## 12. SHA-256

**Type:** Cryptographic hash function in the SHA-2 family.

**Purpose:** Produces a 256-bit digest used for integrity checking and as part of digital-signature and authentication systems.

**Working:**
1. Pad the message and append its length.
2. Divide the padded message into 512-bit blocks.
3. Process each block through 64 rounds.
4. Update the internal hash state.
5. Output the 256-bit digest.

**Bit sizes:**
- **Message block size:** 512 bits.
- **Hash output:** 256 bits, usually shown as 64 hexadecimal characters.
- **Key size:** None in standard SHA-256.

**Viva points:**
- SHA-256 is part of SHA-2.
- A small change in the input should cause a substantially different digest.
- Hashing helps detect modification, but a plain hash alone does not prove who sent the message if an attacker can replace both the message and its hash.

---

## 13. RSA with SHA-256 Digital Signature

**Type:** Digital-signature scheme combining a hash function and RSA.

**Purpose:** Helps verify message integrity and the signer's identity.

**Working:**
1. The sender calculates the SHA-256 hash of the message.
2. The sender creates a digital signature using the RSA private key and a secure signature scheme.
3. The sender sends the message and signature.
4. The receiver calculates SHA-256 on the received message.
5. The receiver verifies the signature using the sender's public key.
6. If verification succeeds, the signature is valid for that message and public key.

**Bit/key sizes:**
- SHA-256 digest: **256 bits**.
- RSA key: commonly **2048 bits or more**.
- Signature length for RSA is generally the modulus length; for example, a 2048-bit RSA modulus gives a 256-byte signature.

**Viva points:**
- The private key is used to sign; the public key is used to verify.
- A digital signature is not the same as encrypting the message.
- The receiver must have a trusted way to associate the public key with the claimed sender.
- In practical systems, use a standard signature scheme such as RSA-PSS rather than manually implementing textbook RSA.

---

## 14. MAC and HMAC

**Type:** Message authentication code.

**Purpose:** Checks message integrity and authenticity using a shared secret key.

**Working:**
1. Sender and receiver share a secret key.
2. The sender calculates a MAC for the message.
3. The sender sends the message and MAC.
4. The receiver calculates the MAC again using the same key.
5. If the values match, the message passes the integrity/authenticity check.

**Bit/key sizes:**
- **Key size:** Depends on the MAC algorithm and configuration; there is no single fixed size for all MACs.
- **HMAC output:** Depends on the underlying hash function and any configured truncation. HMAC-SHA-256 normally produces a 256-bit output before truncation.

**Viva points:**
- HMAC combines a secret key with a hash function.
- Unlike a plain hash, a MAC requires a secret key.
- A MAC does not provide non-repudiation because both parties know the shared secret.
- A MAC is not encryption and does not hide the message.

---

## 15. Quick Bit-Size and Key-Size Table

| Algorithm | Type | Block Size | Key Size | Output / Main Detail |
|---|---|---:|---:|---|
| Caesar | Substitution | No fixed binary block | 26 possible shifts (about 5 bits to encode the shift) | Letter shift |
| Playfair | Digraph substitution | 2 letters at a time | Keyword; 5×5 matrix | I/J usually combined |
| Hill | Matrix substitution | Depends on matrix size | Invertible matrix modulo 26 | Requires modular inverse |
| Rail Fence | Transposition | No fixed binary block | Number of rails | Rearranges letters |
| DES | Symmetric block cipher | 64 bits | 56 effective bits; 64 bits including parity | 16 rounds |
| AES-128 | Symmetric block cipher | 128 bits | 128 bits | 10 rounds |
| AES-192 | Symmetric block cipher | 128 bits | 192 bits | 12 rounds |
| AES-256 | Symmetric block cipher | 128 bits | 256 bits | 14 rounds |
| RSA | Asymmetric | Depends on modulus/padding | Commonly 2048 or 3072 bits; 4096 also used | Uses prime numbers and GCD |
| Finite-field Diffie–Hellman | Key exchange | Not applicable | Depends on group; commonly 2048-bit or larger prime group | Establishes a shared secret |
| MD5 | Hash | 512-bit message block | No key | 128-bit digest |
| SHA-1 | Hash | 512-bit message block | No key | 160-bit digest |
| SHA-256 | Hash | 512-bit message block | No key | 256-bit digest |
| HMAC-SHA-256 | Authentication | Uses SHA-256 internally | Shared secret; configured by system | 256-bit output before truncation |
| RSA + SHA-256 signature | Digital signature | SHA-256 uses 512-bit message blocks | RSA commonly 2048 bits or more | SHA-256 digest is 256 bits |

**Important:** Block size, key size, and output/hash size are different concepts. For example, AES-256 has a 256-bit key but a 128-bit block size.

---

## 16. Fast Viva Questions and Answers

**1. What is cryptography?**  
Cryptography protects information using techniques such as encryption, hashing, and digital signatures.

**2. What is the difference between encryption and hashing?**  
Encryption can be reversed using the correct key. A hash is designed to be one-way and is not decrypted.

**3. What is a symmetric algorithm?**  
An algorithm in which the same secret key is used for encryption and decryption.

**4. What is an asymmetric algorithm?**  
An algorithm that uses a related public key and private key.

**5. Which algorithms use prime numbers and GCD in these experiments?**  
RSA uses prime numbers `p` and `q`, and chooses `e` so that `gcd(e, φ(n)) = 1`. Finite-field Diffie–Hellman uses a prime modulus and modular exponentiation. The Hill cipher uses a GCD condition to check whether its matrix is invertible modulo 26.

**6. Why is GCD important in RSA?**  
It ensures that the chosen public exponent has a modular inverse, which is needed to calculate the private exponent.

**7. Why does Hill cipher need a modular inverse?**  
Decryption needs the inverse of the key matrix modulo 26.

**8. What is the block size of DES?**  
64 bits.

**9. What is the effective key size of DES?**  
56 bits.

**10. What is the block size of AES?**  
128 bits for AES-128, AES-192, and AES-256.

**11. What are the AES key sizes and round counts?**  
128-bit key: 10 rounds; 192-bit key: 12 rounds; 256-bit key: 14 rounds.

**12. What is the output size of MD5?**  
128 bits, or 32 hexadecimal characters.

**13. What is the output size of SHA-1?**  
160 bits, or 40 hexadecimal characters.

**14. What is the output size of SHA-256?**  
256 bits, or 64 hexadecimal characters.

**15. Is Diffie–Hellman an encryption algorithm?**  
No. It is a key-exchange/key-agreement method used to establish a shared secret.

**16. What is a digital signature?**  
A cryptographic value created using the sender's private key and verified using the corresponding public key.

**17. What does a digital signature provide?**  
It supports integrity, authentication of the signer when the public key is trusted, and evidence that the signer approved the signed data.

**18. What is a MAC?**  
A value generated using a shared secret to check message integrity and authenticity.

**19. Why are MD5 and SHA-1 considered insecure?**  
They have known collision weaknesses, so they should not be used where collision resistance is required.

**20. Can a hash be decrypted?**  
No. A standard cryptographic hash is not designed to be decrypted.

**21. What is brute force?**  
Trying possible keys until the correct one is found.

**22. What is a substitution cipher?**  
A cipher that replaces letters or symbols with other letters or symbols.

**23. What is a transposition cipher?**  
A cipher that changes the positions of characters without replacing them.

**24. What is the difference between a hash and a MAC?**  
A plain hash does not use a secret key. A MAC uses a secret key.

**25. Why is AES preferred over DES?**  
AES supports larger keys and provides stronger modern security; DES's 56-bit effective key is too short.

---

## 17. Last-Minute Memory Sheet

Memorize these numbers:

- **DES:** 64-bit block, 56-bit effective key, 16 rounds.
- **AES:** 128-bit block; keys 128/192/256 bits; rounds 10/12/14.
- **RSA:** Common key sizes 2048/3072 bits; uses prime numbers and GCD.
- **Diffie–Hellman:** Prime group in finite-field DH; establishes a shared secret.
- **MD5:** 512-bit message block, 128-bit digest.
- **SHA-1:** 512-bit message block, 160-bit digest.
- **SHA-256:** 512-bit message block, 256-bit digest.
- **HMAC-SHA-256:** 256-bit output before truncation.
- **1 byte = 8 bits.**
- **Encryption hides data; hashing creates a digest; a digital signature verifies a signed message; a MAC checks integrity/authenticity using a shared secret.**

### Security reminder
DES, MD5, and SHA-1 are included for learning and legacy understanding, but should not be selected for new security-sensitive applications. For practical cryptographic systems, use vetted libraries and standard protocols rather than writing your own cryptography.
