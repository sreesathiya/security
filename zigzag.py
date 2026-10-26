text = input("Enter the text: ").upper().replace(" ", "")
rails = int(input("Enter the number of rails: "))

if rails < 2:
    print("Number of rails must be at least 2!")
    exit()

# Create matrix
matrix = [[' ' for _ in range(len(text))] for _ in range(rails)]

row = 0
direction = 1

# Arrange text in zigzag pattern
for col in range(len(text)):
    matrix[row][col] = text[col]

    if row == 0:
        direction = 1
    elif row == rails - 1:
        direction = -1

    row += direction

# Print zigzag matrix
print("\nZigzag Pattern:")
for i in range(rails):
    print("".join(matrix[i]))

# Read row by row to get ciphertext
cipher = ""
for i in range(rails):
    for j in range(len(text)):
        if matrix[i][j] != ' ':
            cipher += matrix[i][j]

print("\nCipher Text:", cipher)

# Decryption
matrix2 = [[' ' for _ in range(len(text))] for _ in range(rails)]

row = 0
direction = 1

# Mark zigzag positions
for col in range(len(text)):
    matrix2[row][col] = '*'

    if row == 0:
        direction = 1
    elif row == rails - 1:
        direction = -1

    row += direction

# Fill ciphertext row by row
k = 0
for i in range(rails):
    for j in range(len(text)):
        if matrix2[i][j] == '*':
            matrix2[i][j] = cipher[k]
            k += 1

# Read zigzag to recover plaintext
plain = ""
row = 0
direction = 1

for col in range(len(text)):
    plain += matrix2[row][col]

    if row == 0:
        direction = 1
    elif row == rails - 1:
        direction = -1

    row += direction

print("Recovered Text:", plain)