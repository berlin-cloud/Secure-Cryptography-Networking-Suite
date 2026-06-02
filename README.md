# Secure Cryptography & Networking Suite

A comprehensive Python-based security suite implementing standard cryptographic algorithms and secure network communication protocols. This project demonstrates foundational concepts in data encryption, integrity, and secure client-server architectures.

## 🚀 Key Features

### 🔐 Cryptographic Implementations
*   **Symmetric Encryption:** Implementation of **AES (Advanced Encryption Standard)** and **DES (Data Encryption Standard)** for secure data at rest.
*   **Asymmetric Encryption:** **RSA** implementation for secure key management and data transmission.
*   **Key Exchange:** **Diffie-Hellman** protocol implementation to simulate secure shared secret establishment over insecure channels.
*   **Digital Signatures:** Mechanism for ensuring data authenticity and non-repudiation.

### 🌐 Secure Networking
*   **Encrypted Socket Communication:** A custom-built client-server architecture using Python `sockets`.
*   **SSL/TLS Integration:** Implementation of secure wrappers (`ssl`) using PEM certificates (`cert.pem`, `key.pem`) to ensure end-to-end encrypted data transmission (E2EE).
*   **Packet Handling:** Structured data transmission using custom packet definitions.

## 🛠 Tech Stack
*   **Language:** Python 3.x
*   **Libraries:** `PyCryptodome`, `ssl`, `socket`
*   **Security:** SSL/TLS, AES, RSA, DES, SHA

## 📂 Project Structure
```text
├── Aes.py               # AES Encryption logic
├── Des.py               # DES Encryption logic
├── Rsa.py               # RSA Encryption logic
├── DeffiHellMan.py      # Diffie-Hellman Key Exchange
├── DigitalSignature.py  # Data Integrity & Verification
├── packet_server.py     # SSL-wrapped Secure Server
├── packet_client.py     # Secure Client Implementation
├── Packets.py           # Data structure definitions
├── cert.pem / key.pem   # SSL Certificates
└── requirements.txt     # Dependency list
```

## ⚙️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/berlin-cloud/SECURE-CRYPTOGRAPHY-NETWORKING-SUITE.git
   cd SECURE-CRYPTOGRAPHY-NETWORKING-SUITE
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Secure Server:**
   ```bash
   python packet_server.py
   ```

4. **Run the Client:**
   ```bash
   python packet_client.py
   ```

## 🛡 Security Disclaimer
This project is intended for **educational and research purposes only**. It demonstrates the mechanics of cryptographic protocols. For production environments, always use verified industry-standard libraries and managed security services.

---
Developed by [Berlin Samvel Pandian S](https://linkedin.com/in/s-berlin-samvel-pandian007)
