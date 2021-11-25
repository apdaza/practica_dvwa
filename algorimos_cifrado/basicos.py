import binascii
import base64

mensaje = "Hola mundo!"
cifrado = binascii.b2a_hex(mensaje.encode())
texto_claro = binascii.a2b_hex(cifrado).decode()

print("mensaje cifrado", cifrado)
print("mensaje claro", texto_claro)

cifrado2 = base64.encodebytes(mensaje.encode())
texto_claro2 = base64.decodebytes(cifrado2).decode()

print("mensaje cifrado", cifrado2)
print("mensaje claro", texto_claro2)