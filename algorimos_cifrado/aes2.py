from Crypto.Cipher import AES
from Crypto import Random
from binascii import b2a_hex, a2b_hex

clave = 'abcdefghijklmnop'

mensaje = 'Hola mundo!'
iv = Random.new().read(AES.block_size)
cifrador_aes = AES.new(clave.encode('utf-8'), AES.MODE_CFB, iv)
cifrado = iv + cifrador_aes.encrypt(mensaje.encode('utf-8'))
descifrador_aes = AES.new(clave.encode('utf-8'), AES.MODE_CFB, cifrado[:AES.block_size])
texto_claro = descifrador_aes.decrypt(cifrado[AES.block_size:]).decode('utf-8').rstrip(' ')

print('clave', clave)
print("iv", b2a_hex(cifrado[:AES.block_size]).decode('utf-8'))
print("mensaje cifrado",b2a_hex(cifrado))
print("mensaje claro",texto_claro)