a = 17
b = 11
e = 7

n = a*b
phi_n = (a-1)*(b-1)

d = pow(e,-1,phi_n)

print(f" Private Key {d},{n} \n Public Key {e},{n}")

m = 88

encrypt = pow(m,e,n)
decrypt = pow(encrypt,d,n)

print(f" Plain Text {m} \n Cipher Text {encrypt} \n decrypted Plain Text {decrypt}")