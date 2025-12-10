import socket
import pickle
import zlib
import math
import sys
from colorama import Fore, init

init(autoreset=True)
sys.set_int_max_str_digits(1000000000)

HOST = '127.0.0.1'
PORT = 65432

def receive_task(sock):
    data = b""
    while True:
        part = sock.recv(4096)
        if not part:
            break
        data += part
        try:
            return pickle.loads(zlib.decompress(data))
        except:
            continue

def send_result(sock, result):
    serialized = pickle.dumps(result)
    compressed = zlib.compress(serialized)
    sock.sendall(compressed)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        print(Fore.CYAN + "[Клиент] Подключен к серверу.")

        while True:
            task = receive_task(sock)
            if not task or task[0] == 'done':
                break

            task_type, data = task
            if task_type == 'factorial':
                start, end = data
                print(Fore.YELLOW + f"[Клиент] Обработка от {start} до {end}...")
                result = math.prod(range(start, end + 1))
                send_result(sock, result)

if __name__ == "__main__":
    main()
