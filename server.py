import socket
import threading
import pickle
import zlib
import time
import math
import sys
from colorama import init, Fore, Style
from tabulate import tabulate

init(autoreset=True)
sys.set_int_max_str_digits(1000000000)

HOST = '127.0.0.1'
PORT = 65432


def send_compressed(conn, data):
    serialized = pickle.dumps(data)
    compressed = zlib.compress(serialized)
    conn.sendall(compressed)


def receive_compressed(conn):
    data = b""
    while True:
        part = conn.recv(4096)
        if not part:
            break
        data += part
        try:
            return pickle.loads(zlib.decompress(data))
        except:
            continue


def split_ranges(n, parts):
    step = n // parts
    ranges = []
    for i in range(parts):
        start = i * step + 1
        end = (i + 1) * step if i != parts - 1 else n
        ranges.append((start, end))
    return ranges


def main():
    n = int(input("Введите N (например, 10000): "))
    client_count = int(input("Введите количество клиентов: "))

    print(Fore.CYAN + f"\n[Сервер] Ожидаем {client_count} клиента...\n")

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(client_count)

    clients = []
    for _ in range(client_count):
        conn, addr = server.accept()
        print(Fore.GREEN + f"[Сервер] Подключился клиент: {addr}")
        clients.append(conn)

    ranges = split_ranges(n, client_count)

    print(Fore.MAGENTA + "\n[Сервер] Распределяем задачи...\n")
    time_start = time.perf_counter()

    for conn, task_range in zip(clients, ranges):
        send_compressed(conn, ('factorial', task_range))

    partial_results = []
    for i, conn in enumerate(clients):
        part = receive_compressed(conn)
        partial_results.append(part)
        print(Fore.YELLOW + f"[Сервер] Результат от клиента {i + 1} получен.")

    result = math.prod(partial_results)
    time_end = time.perf_counter()
    duration = (time_end - time_start) * 1000  # ms

    result_str = str(result)
    with open("distributed_result.txt", "w") as f:
        f.write(result_str)

    print(Fore.CYAN + f"\nПервые 20 цифр факториала: {result_str[:20]}")
    print(Fore.CYAN + f"Файл с полным результатом: distributed_result.txt")

    print(Fore.LIGHTGREEN_EX + f"\n✅ Время распределённой обработки: {duration:.2f} мс")

    for conn in clients:
        send_compressed(conn, ('done', None))
        conn.close()

    with open("stats.txt", "a") as f:
        f.write(f"Distributed;{n};{client_count};{duration:.2f}\n")


if __name__ == "__main__":
    main()
