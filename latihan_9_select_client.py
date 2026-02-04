import socket

def run_chat_client():
    # 1. Buat socket client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. Hubungkan ke server
    client_socket.connect(('127.0.0.1', 9000))
    print("=== Terhubung ke Chat Server ===")
    print("Ketik pesan lalu ENTER (ketik 'bye' untuk keluar)")

    try:
        while True:
            # 3. Input dari user
            message = input("Anda > ")

            # 4. Kirim ke server
            client_socket.send(message.encode())

            if message.lower() == 'bye':
                print("[!] Anda keluar dari chat.")
                break

            # 5. Terima pesan broadcast dari server
            data = client_socket.recv(1024)
            if not data:
                print("[!] Server menutup koneksi.")
                break

            print(data.decode().strip())

    except KeyboardInterrupt:
        print("\nClient dihentikan.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()
        print("=== Client Ditutup ===")

if __name__ == "__main__":
    run_chat_client()
