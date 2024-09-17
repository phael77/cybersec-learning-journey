#função criada para encriptar a mensagem
def caesar_cipher_encryption(message, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encoded = ""
   #loop criado para o avanço das letras no alfabeto de acordo com a chave informada pelo usuário
    for i in message:
        encoded_char_index = ((ord(i) - ord('a'))+key) % 26
        encoded += alphabet[encoded_char_index]
    #retornando a palavra codificada    
    return encoded
#função criada para desencriptar a mensagem
def caesar_cipher_decryption(crypto, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decrypted_message = ""
    #loop criado para o retorno das letras no alfabeto de acordo com a chave informada pelo usuário
    for i in crypto:
        decoded_char_index = ((ord(i) - ord('a'))-key) % 26
        decrypted_message += alphabet[decoded_char_index]
    #retornando a palavra decodificada
    return decrypted_message

message = input('Enter your message: ') #usuário informa a mensagem a ser encriptada
crypto_message = caesar_cipher_encryption(message, 11)
decrypted_message = caesar_cipher_decryption(crypto_message, 11) 
print('\nEncrypted message:', crypto_message) #saida da mensagem encriptada
print('\nDecrypted message:', decrypted_message) #saida da mensagem desencriptada