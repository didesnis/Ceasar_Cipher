from ceasar_files import logo
from ceasar_files import alphabet
import random

print('Welcome to')
print(logo)
one_more_time = True

def encrypt(message, shift):
    cipher_text = ""
    for letter in message:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift)
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += letter
    return cipher_text
def decrypt(message, shift):
    encrypted_text = ""
    for letter in message:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position - shift)
            new_letter = alphabet[new_position]
            encrypted_text += new_letter
        else:
            encrypted_text += letter
    return encrypted_text

while one_more_time:
    what_to_do = input("Type 'Encode' to encode the message or type 'Decode' to decode the message:\n").lower()

    if what_to_do == 'encode':
        message = input('Write down your message:\n').lower()
        shift = int(input('Type the shift number:\n'))
        result = encrypt(message, shift)
        print(f"Encoded message: {result}")

    elif what_to_do == 'decode':
        message = input('Type your message here for decoding:\n').lower()
        shift = int(input('Type the shift number:\n'))
        result = decrypt(message, shift)
        print(f"Decoded message: {result}")

    else:
        print("Invalid input. Please type 'Encode' or 'Decode'.")

    one_more_time = input("Type 'Yes' if you wish to proceed one more time, or type 'No' if you wish to exit:\n").lower()
    if one_more_time == 'no':
        one_more_time = False
        print('Thank you for using our services')
    else:
        continue
