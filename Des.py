from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

message = "Hello World" 

Des = DES.new(b'12345678', DES.MODE_ECB)

encrypt = Des.encrypt(pad(message.encode(), 8))

decrypt = unpad(Des.decrypt(encrypt), 8)

print(f" Plain Text : {message} \n Cipher Text : {encrypt} \n Decrypted Plain Text : {decrypt.decode()}")