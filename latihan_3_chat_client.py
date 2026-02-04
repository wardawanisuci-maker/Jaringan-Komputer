import socket

# 1. Persiapan Socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Connect ke Server
client.connect(('localhost', 5000))
print("=== Terhubung ke Chat Server ===")

# 3. INTI CHAT: Loop komunikasi
while True:
    try:
        # 1. Kirim Pesan ke Server
        msg = input("Client (Anda) > ")
        client.send(msg.encode('utf-8'))

        # Cek jika client ingin keluar
        if msg.lower() == 'bye':
            print("[!] Anda mengakhiri sesi.")
            break

        # 2. Terima Balasan dari Server (BLOCKING)
        data = client.recv(1024).decode('utf-8')

        # Cek kondisi keluar
        if not data or data.lower() == 'bye':
            print("[!] Server mengakhiri sesi.")
            break

        print(f"Server > {data}")

    except Exception as e:
        print(f"Error Terjadi: {e}")
        break

# 4. Tutup koneksi
client.close()
print("=== Client Ditutup ===")
