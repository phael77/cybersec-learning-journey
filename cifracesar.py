def caesar_cipher_encryption(message, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encoded = ""
    
    for i in message:
        encoded_char_index = ((ord(i) - ord('a'))+key) % 26
        encoded += alphabet[encoded_char_index]
        
    return encoded

def caesar_cipher_decryption(crypto, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decrypted_message = ""
    
    for i in crypto:
        decoded_char_index = ((ord(i) - ord('a'))-key) % 26
        decrypted_message += alphabet[decoded_char_index]
        
    return decrypted_message

message = input('Enter your message: ')
crypto_message = caesar_cipher_encryption(message, 11)
decrypted_message = caesar_cipher_decryption(crypto_message, 11)
print('\nEncrypted message:', crypto_message)
print('\nDecrypted message:', decrypted_message)