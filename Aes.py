from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = b'1234567891011123'

message = "hello World"

print(f" plain text : {message}")

AES_Algo = AES.new(key, AES.MODE_ECB)

encrypt = AES_Algo.encrypt(pad(message.encode(), 16))

print(f" Cipher Text : {encrypt}")

decrypt = unpad(AES_Algo.decrypt(encrypt), 16)

print(f" Decrypted Plain Text: {decrypt.decode()}")