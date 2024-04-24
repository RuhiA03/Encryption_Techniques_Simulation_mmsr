import random
import string
import numpy as np


def caesar_cipher(text):
    key = random.randint(1, 25)  
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                shifted_char = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
            else:
                shifted_char = chr((ord(char) - ord('A') + key) % 26 + ord('A'))
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    print("Random Key:", key)
    return encrypted_text


def multiplicative_cipher(text):
    key = random.randint(1, 25)
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted_char = chr(((ord(char) - ord('a' if char.islower() else 'A')) * key) % 26 + ord('a' if char.islower() else 'A'))
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    print("Random Key:", key)
    return encrypted_text


def playfair_cipher(plaintext):
    key1 = [['M', 'O', 'N', 'A', 'R'],
            ['C', 'H', 'Y', 'B', 'D'],
            ['E', 'F', 'G', 'I', 'K'],
            ['L', 'P', 'Q', 'S', 'T'],
            ['U', 'V', 'W', 'X', 'Z']]
   
    key2 = [['Z', 'E', 'B', 'R', 'A'],
            ['C', 'D', 'F', 'G', 'H'],
            ['I', 'K', 'L', 'M', 'N'],
            ['O', 'P', 'Q', 'S', 'T'],
            ['U', 'V', 'W', 'X', 'Y']]
   
    print("Choose a key:")
    print("1. MONARCHY")
    print("2. ZEBRA")
    choice = int(input("Enter your choice (1/2): "))
    if choice == 1:
        key = key1
    elif choice == 2:
        key = key2
    else:
        print("Invalid choice!")
        return

    print("Key Matrix:")
    for row in key:
        print(row)

   
    plaintext_list = list(plaintext)
    l = len(plaintext_list)
    if l % 2 != 0:
        plaintext_list.append('Z')

   
    ciphertext = []
    i = 0
    while i < len(plaintext_list):
        char1 = plaintext_list[i]
        char2 = plaintext_list[i + 1]
        row1, col1 = None, None
        row2, col2 = None, None
        for row_idx, row in enumerate(key):
            if char1 in row:
                row1, col1 = row_idx, row.index(char1)
            if char2 in row:
                row2, col2 = row_idx, row.index(char2)

        if row1 == row2:  # Same row
            ciphertext.append(key[row1][(col1 - 1) % 5])
            ciphertext.append(key[row2][(col2 - 1) % 5])
        elif col1 == col2:  # Same column
            ciphertext.append(key[(row1 - 1) % 5][col1])
            ciphertext.append(key[(row2 - 1) % 5][col2])
        else:  # Different row and column
            ciphertext.append(key[row1][col2])
            ciphertext.append(key[row2][col1])

        i += 2

    return ''.join(ciphertext)



def vigenere_cipher(plaintext):
   
    vigenere_table = [['' for _ in range(26)] for _ in range(26)]
    for row_idx, char in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        for col_idx in range(26):
            vigenere_table[row_idx][col_idx] = chr((ord(char) - ord('A') + col_idx) % 26 + ord('A'))

   
    print("Vigenère Table:")
    print("  " + " ".join([chr(ord('A') + i) for i in range(26)]))
    for row_idx, row in enumerate(vigenere_table):
        print(chr(ord('A') + row_idx) + " " + " ".join(row))

   
    print("Choose a key:")
    print("1. VIT")
    print("2. DOLL")
    print("3. NET")
    choice = int(input("Enter your choice (1/2/3): "))
    if choice == 1:
        key = "VIT"
    elif choice == 2:
        key = "DOLL"
    elif choice == 3:
        key = "NET"
    else:
        print("Invalid choice!")
        return

   
    ciphertext = ""
    key_index = 0
    for char in plaintext.upper().replace(" ", ""):
        if char.isalpha():
            row_idx = ord(key[key_index % len(key)]) - ord('A')
            col_idx = ord(char) - ord('A')
            ciphertext += vigenere_table[row_idx][col_idx]
            key_index += 1
        else:
            ciphertext += char

    return ciphertext



def hill_cipher(plaintext):
    # Find the length of the plaintext
    l = len(plaintext)

    # Generate a random key sequence of size l*l
    key_sequence = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=l*l))
    print("Key=",key_sequence)

    # Convert plaintext and key sequence into numerical representation
    plaintext_numeric = [ord(char) - ord('A') for char in plaintext]
    key_sequence_numeric = [ord(char) - ord('A') for char in key_sequence]

    # Create a l*l matrix from the key sequence
    key_matrix = np.array(key_sequence_numeric[:l*l]).reshape((l, l))

    # Create a l*1 matrix from the plaintext numeric representation
    plaintext_matrix = np.array(plaintext_numeric[:l]).reshape((l, 1))

    # Perform matrix multiplication: key * plaintext
    result_matrix = np.matmul(key_matrix, plaintext_matrix)

    # Perform mod 26 on each element of the result matrix
    result_matrix = result_matrix % 26

    # Convert the result matrix back to letters
    cipher_text = ''.join([chr(int(result)) for result in result_matrix.flatten() + ord('A')])

    return cipher_text


plaintext = input("Enter the plaintext: ")

print("Choose an encryption technique:")
print("1. Caeser/Additive Cipher")
print("2. Multiplicative Cipher")
print("3. Playfair Cipher")
print("4. Vignere Cipher")
print("5. Hill Cipher")

choice = int(input("Enter your choice (1/2/3/4/5): "))

if choice == 1:
    ciphertext = caesar_cipher(plaintext)
elif choice == 2:
    ciphertext = multiplicative_cipher(plaintext)
    
elif choice == 3:
    ciphertext = playfair_cipher(plaintext)
elif choice == 4:
    ciphertext = vigenere_cipher(plaintext)
elif choice == 5:
    ciphertext = hill_cipher(plaintext)
else:
    print("Invalid choice!")
   
print("Ciphertext:", ciphertext)






