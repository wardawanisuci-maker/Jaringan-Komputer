import socket
import threading

def receive_messages(client):
    """Thread untuk menerima pesan dari server"""
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if not message:
                print("[!] Koneksi ke server terputus.")
                break
            print(message)
        except:
            print("[!] Terjadi error saat menerima pesan.")
            break

def start_client():
    # 1. Buat socket client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. Connect ke server (samakan port dengan server)
    client.connect(('localhost', 5555))
    print("=== Terhubung ke Chat Server ===")

    # 3. Jalankan thread penerima pesan
    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.daemon = True
    thread.start()

    # 4. Loop kirim pesan
    while True:
        try:
            msg = input()
            if msg.lower() == 'bye':
                client.send(msg.encode('utf-8'))
                print("[!] Anda keluar dari chat.")
                break
            client.send(msg.encode('utf-8'))
        except:
            break

    # 5. Tutup koneksi
    client.close()
    print("=== Client Ditutup ===")

if __name__ == "__main__":
    start_client()
