p = 23
q = 5

# Private key
a = 7
b = 13

# public Key
Alice_pub = (q**a)%p
Bob_pub = (q**b)%p

print(f" Alice public key {Alice_pub}")
print(f" Bob public key {Bob_pub}")

#Shared Secret Key
key1 = (Alice_pub**b)%p
key2 = (Bob_pub**a)%p

print(" Same Key to Alice and bob" if(key1==key2) else "Diff Key")