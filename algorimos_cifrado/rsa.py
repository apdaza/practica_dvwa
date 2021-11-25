from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

keyPair = RSA.generate(3072)

pubkey = keyPair.publickey()
print(f"Public key : (n='{hex(pubkey.n)}, e={hex(pubkey.e)})")
pubKeyPEM = pubkey.exportKey()
print(pubKeyPEM.decode('ascii'))

print(f"Private key : (n='{hex(keyPair.n)}, e={hex(keyPair.e)}, d={hex(keyPair.d)})")
privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))

mensaje = "Hola mundo!"
msg = bytes(mensaje, 'utf-8')
cifrador = PKCS1_OAEP.new(pubkey)
cifrado = cifrador.encrypt(msg)
descifrador = PKCS1_OAEP.new(keyPair)
descifrado = descifrador.decrypt(cifrado)

print("mensaje cifrado", binascii.hexlify(cifrado))
print("mensaje claro", descifrado.decode('utf-8'))
