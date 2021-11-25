from Crypto.Cipher import DES

def completar(texto):
    if len(texto) % 8 != 0:
        texto += ' ' * (8 - len(texto) % 8)
    return texto

clave = b'abcdefgh'

des = DES.new(clave, DES.MODE_ECB)
mensaje = 'Hola mundo!'
mensaje = completar(mensaje)
cifrado = des.encrypt(mensaje.encode('utf-8'))
texto_claro = des.decrypt(cifrado).decode('utf-8').rstrip(' ')

print("mensaje cifrado",cifrado)
print("mensaje claro",texto_claro)