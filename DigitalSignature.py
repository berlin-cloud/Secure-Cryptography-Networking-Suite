import hashlib

message = "Hello World"

p = 17
q = 11
e = 7

n = p*q
phi_n = (p-1)*(q-1)

d = pow(e,-1,phi_n)

hashed = int(hashlib.sha256(message.encode()).hexdigest(), 16)

signature = pow(hashed,d,n)

verification = pow(signature,e,n) == hashed%n

print(f" Plain Text {message} \n Cipher Text {hashed} \n", "Verification Successfull" if verification else "Verification failed")