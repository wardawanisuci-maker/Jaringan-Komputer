import socket

# 1. Membuat soket (IPv4, TCP)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Connect ke server (alamat dan port HARUS sama dengan server)
client_socket.connect(('localhost', 12345))
print("Client: Berhasil terhubung ke server")

# 3. Kirim pesan ke server
client_socket.send("Halo Server, saya client!".encode('utf-8'))

# 4. Terima pesan dari server
msg = client_socket.recv(1024).decode('utf-8')
print(f"Client: Server membalas '{msg}'")

# 5. Tutup koneksi
client_socket.close()
print("Client: Koneksi ditutup")
