#Playfair Cipher
def key_matrix(key):
    key = key.replace("J", "I")
    key = "".join(dict.fromkeys(key + "ABCDEFGHIKLMNOPQRSTUVWXYZ"))
    return [list(key[i:i+5]) for i in range(0, 25, 5)]
    
def find_position(matrix,letter):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row , col 
    return None

def encrypt_digraph(matrix, digraph):
    a, b = digraph[0], digraph[1]
    row_a, col_a = find_position(matrix, a)
    row_b, col_b = find_position(matrix, b)
    
    if row_a == row_b:  
        return matrix[row_a][(col_a + 1) % 5] + matrix[row_b][(col_b + 1) % 5]
    elif col_a == col_b: 
        return matrix[(row_a + 1) % 5][col_a] + matrix[(row_b + 1) % 5][col_b]
    else: 
        return matrix[row_a][col_b] + matrix[row_b][col_a]
    
def decrypt_digraph(matrix, digraph):
    a, b = digraph[0], digraph[1]
    row_a, col_a = find_position(matrix, a)
    row_b, col_b = find_position(matrix, b)
    
    if row_a == row_b:
        return matrix[row_a][(col_a - 1) % 5] + matrix[row_b][(col_b - 1) % 5]
    elif col_a == col_b:
        return matrix[(row_a - 1) % 5][col_a] + matrix[(row_b - 1) % 5][col_b]
    else:
        return matrix[row_a][col_b] + matrix[row_b][col_a]
    
def prepare_text(plaintext):
    plaintext = plaintext.upper().replace("J", "I")
    prepared = ""
    i = 0
    while i < len(plaintext):
        a = plaintext[i]
        b = "X" if i + 1 == len(plaintext) or plaintext[i] == plaintext[i + 1] else plaintext[i + 1]
        prepared += a + b
        i += 1 if a == b else 2
    return prepared

def playfair_encrypt(plaintext, key):
    matrix = key_matrix(key)
    plaintext = prepare_text(plaintext)
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        ciphertext += encrypt_digraph(matrix, plaintext[i:i+2])
    return ciphertext

def playfair_decrypt(ciphertext, key):
    matrix = key_matrix(key)
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        plaintext += decrypt_digraph(matrix, ciphertext[i:i+2])
    return plaintext



choise = int(input("1.Encreption && 2.Decreption"))
if choise == 1:
    key = input("Enter the key: ").strip().upper()
    plaintext = input("Enter plain text: ").strip().upper()
    ciphertext = playfair_encrypt(plaintext, key)
    print("Ciphertext:", ciphertext)
    
    
elif choise == 2:
    key = input("Enter the key: ").strip().upper()
    ciphertext = input("Enter the ciphertext: ").strip().upper()
    decrypted_text = playfair_decrypt(ciphertext, key)
    print("plain Text:", decrypted_text)
    