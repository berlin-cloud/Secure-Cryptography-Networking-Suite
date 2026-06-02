import socket
import ssl
import sys
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

HOST = "localhost"
PORT = 3000

# Shared AES Key (must be the same on client and server)
AES_KEY = b'1234567891011123' 

# Get the absolute path to the directory this script is in
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Create the SSL context for the server
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
try:
    ssl_context.load_cert_chain(certfile=os.path.join(BASE_DIR, "cert.pem"), 
                                keyfile=os.path.join(BASE_DIR, "key.pem"))
except Exception as e:
    print(f"Error loading SSL certificates: {e}")
    print("Ensure 'cert.pem' and 'key.pem' are in the project folder.")
    sys.exit(1)

print(f"Server starting on {HOST}:{PORT}...")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    
    print("Waiting for connections (Press Ctrl+C to stop)...")
    
    while True:
        try:
            # Accept incoming connection
            conn, addr = server_socket.accept()
            
            # Wrap the connection with SSL
            with ssl_context.wrap_socket(conn, server_side=True) as secure_conn:
                with secure_conn:
                    print(f"\n[+] Connection from {addr}")
                    
                    # 1. Receive encrypted data
                    data = secure_conn.recv(1024)
                    if not data:
                        continue
                    
                    print(f"    Received (Ciphertext): {data.hex()}")
                    
                    # 2. Decrypt the data using AES (ECB mode as per your Aes.py example)
                    try:
                        cipher = AES.new(AES_KEY, AES.MODE_ECB)
                        decrypted_data = unpad(cipher.decrypt(data), 16)
                        message = decrypted_data.decode('utf-8')
                        print(f"    Decrypted Message: {message}")
                        
                        # 3. Send acknowledgment to the client
                        secure_conn.sendall(f"Server received: {message}".encode('utf-8'))
                    except Exception as decrypt_error:
                        print(f"    Decryption Error: {decrypt_error}")
                        secure_conn.sendall(b"Error: Decryption failed")
                        
        except KeyboardInterrupt:
            print("\nServer stopping...")
            break
        except Exception as e:
            print(f"Connection error occurred: {e}")
