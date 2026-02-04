import socket
import json
import time
import random
import psutil

SERVER_IP = "127.0.0.1"
SERVER_PORT = 9999

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = {
        "device_id": "agent-001",
        "cpu_usage": psutil.cpu_percent(),
        "temperature": random.randint(30, 60),
        "timestamp": time.time()
    }

    message = json.dumps(data)
    sock.sendto(message.encode(), (SERVER_IP, SERVER_PORT))

    print("Data terkirim:", data)
    time.sleep(2)
