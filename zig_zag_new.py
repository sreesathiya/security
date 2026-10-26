def rail_fence(plaintext, rails):
    n = len(plaintext)
    grid = [[' ' for _ in range(n)] for _ in range(rails)]

    row = 0
    direction = 1

    # Construct zig-zag grid
    for col in range(n):
        grid[row][col] = plaintext[col]

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    print("\nZig-zag Grid:")
    for r in grid:
        print(' '.join(ch if ch != ' ' else '_' for ch in r))

    # Row-major ciphertext
    row_cipher = ''
    for r in range(rails):
        for c in range(n):
            if grid[r][c] != ' ':
                row_cipher += grid[r][c]

    # Column-major ciphertext
    col_cipher = ''
    for c in range(n):
        for r in range(rails):
            if grid[r][c] != ' ':
                col_cipher += grid[r][c]

    return row_cipher, col_cipher


def decrypt(ciphertext, rails, mode):
    n = len(ciphertext)
    grid = [[' ' for _ in range(n)] for _ in range(rails)]

    row = 0
    direction = 1

    # Mark zig-zag positions
    for col in range(n):
        grid[row][col] = '*'

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    index = 0

    # Fill grid using the selected encryption order
    if mode == 'row':
        for r in range(rails):
            for c in range(n):
                if grid[r][c] == '*':
                    grid[r][c] = ciphertext[index]
                    index += 1
    else:
        for c in range(n):
            for r in range(rails):
                if grid[r][c] == '*':
                    grid[r][c] = ciphertext[index]
                    index += 1

    # Read characters in zig-zag order
    plaintext = ''
    row = 0
    direction = 1

    for col in range(n):
        plaintext += grid[row][col]

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    return plaintext


# Main program
plaintext = input("Enter plaintext: ").replace(" ", "").upper()
rails = int(input("Enter number of rails: "))

if rails < 1:
    print("Number of rails must be at least 1.")
else:
    row_cipher, col_cipher = rail_fence(plaintext, rails)

    print("\nRow-major Ciphertext:", row_cipher)
    print("Column-major Ciphertext:", col_cipher)

    row_plain = decrypt(row_cipher, rails, 'row')
    col_plain = decrypt(col_cipher, rails, 'column')

    print("\nDecrypted Row-major:", row_plain)
    print("Decrypted Column-major:", col_plain)

    if row_cipher == col_cipher:
        print("\nBoth ciphertexts are the same.")
    else:
        print("\nBoth ciphertexts are different.")

    print("\nVerification:")
    print("Row-major decryption correct:", row_plain == plaintext)
    print("Column-major decryption correct:", col_plain == plaintext)
