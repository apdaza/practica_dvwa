from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

clave = 'abcdefghijklmnop'

def completar_bloque(texto):
    if len(texto) % 16 != 0:
        texto += ' ' * (16 - len(texto) % 16)
    return texto

def cifrar(texto):
    texto = completar_bloque(texto)
    obj = AES.new(clave.encode('utf-8'), AES.MODE_ECB)
    return b2a_hex(obj.encrypt(texto.encode('utf-8')))

def descifrar(texto):
    obj = AES.new(clave.encode('utf-8'), AES.MODE_ECB)
    print(texto)
    return obj.decrypt(a2b_hex(texto.strip())).decode('utf-8').rstrip(' ')
