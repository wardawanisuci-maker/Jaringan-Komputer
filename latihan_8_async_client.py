import asyncio

async def tcp_client():
    # 1. Koneksi ke server
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888
    )

    print("=== Terhubung ke Async Server ===")

    try:
        while True:
            # 2. Ambil input user (dibungkus agar tidak blok event loop)
            message = await asyncio.to_thread(input, "Client > ")

            if message.lower() == 'bye':
                print("[!] Client keluar.")
                break

            # 3. Kirim pesan ke server
            writer.write((message + "\n").encode())
            await writer.drain()

            # 4. Terima balasan server
            data = await reader.read(100)
            if not data:
                print("[!] Server menutup koneksi.")
                break

            print(f"Server > {data.decode().strip()}")

    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        # 5. Tutup koneksi
        writer.close()
        await writer.wait_closed()
        print("=== Client Ditutup ===")

if __name__ == "__main__":
    asyncio.run(tcp_client())
