import socket
import ssl
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

HOST = "localhost"
PORT = 3000

# Shared AES Key (must be the same on client and server)
AES_KEY = b'1234567891011123' 

# Create a proper unverified SSL context for testing purposes
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
    # Wrap the socket with SSL
    with ssl_context.wrap_socket(soc, server_hostname=HOST) as secure_socket:
        try:
            # Connect to the server
            secure_socket.connect((HOST, PORT))
            print(f"Connected to server at {HOST}:{PORT}")
            
            # 1. Prepare and Encrypt the message
            message = "Hello World"
            cipher = AES.new(AES_KEY, AES.MODE_ECB)
            encrypted_message = cipher.encrypt(pad(message.encode('utf-8'), 16))
            
            # 2. Send the encrypted data
            secure_socket.sendall(encrypted_message)
            print(f"Sent encrypted packet: {encrypted_message.hex()}")
            
            # 3. Wait for server acknowledgment
            # This prevents the client from closing the socket too early
            response = secure_socket.recv(1024)
            if response:
                print(f"Server response: {response.decode('utf-8')}")
            
        except ConnectionRefusedError:
            print("Connection failed: Is the server running?")
        except Exception as e:
            print(f"An error occurred: {e}")
