from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

def completar_bloque(texto):
    if len(texto) % 16 != 0:
        texto += ' ' * (16 - len(texto) % 16)
    return texto
    
clave = 'abcdefghijklmnop'

aes = AES.new(clave.encode('utf-8'), AES.MODE_ECB)

mensaje = 'Hola mundo!'
mensaje = completar_bloque(mensaje)

cifrado = b2a_hex(aes.encrypt(mensaje.encode('utf-8')))
texto_claro = aes.decrypt(a2b_hex(cifrado)).decode('utf-8').rstrip(' ')

print("mensaje cifrado",cifrado)
print("mensaje claro",texto_claro)