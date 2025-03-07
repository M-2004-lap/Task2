#Monoalphabetic Cipher
import itertools
import string

def encrypt(text, key_mapping):
    encrypted_text = "".join(key_mapping.get(c, c) for c in text)
    return encrypted_text

def decrypt(text, key_mapping):
    reversed_mapping = {v: k for k, v in key_mapping.items()}
    decrypted_text = "".join(reversed_mapping.get(c, c) for c in text)
    return decrypted_text

def generate_mappings():
    alphabet = string.ascii_uppercase
    for perm in itertools.permutations(alphabet):
        yield dict(zip(alphabet, perm))

def brute_force_attack(encrypted_text):
    possible_decryptions = []
    
    for key_mapping in generate_mappings():
        decrypted_text = decrypt(encrypted_text, key_mapping)
        possible_decryptions.append(decrypted_text)
    
    return possible_decryptions


choise = int(input("1.Encreption && 2.Decreption"))
if choise == 1:
    custom_key = dict(zip(string.ascii_uppercase, "QWERTYUIOPASDFGHJKLZXCVBNM"))
    original_text = input("Enter the original text: ").strip().upper()
    encrypted_message = encrypt(original_text, custom_key)
    print("Encrypted Text:", encrypted_message)
    
elif choise == 2:
    custom_key = dict(zip(string.ascii_uppercase, "QWERTYUIOPASDFGHJKLZXCVBNM"))
    encrypted_message = input("Enter the encrypted text: ").strip().upper()
    decrypted_message = decrypt(encrypted_message, custom_key)
    print("plain Text:", decrypted_message)