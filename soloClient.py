import math
import time
import sys
from colorama import Fore, init
from tabulate import tabulate

init(autoreset=True)
sys.set_int_max_str_digits(1000000000)

def main():
    n = int(input("Введите число: "))
    print(Fore.CYAN + f"Вычисление {n}! в одиночку...")

    start_time = time.perf_counter()
    result = math.prod(range(1, n + 1))
    end_time = time.perf_counter()

    duration = (end_time - start_time) * 1000  # ms

    result_str = str(result)
    with open("solo_result.txt", "w") as f:
        f.write(result_str)

    print(Fore.LIGHTGREEN_EX + f"\nПервые 20 цифр: {result_str[:20]}")
    print(Fore.CYAN + f"Файл с полным результатом: solo_result.txt")
    print(Fore.LIGHTGREEN_EX + f"✅ Время одиночной обработки: {duration:.2f} мс")

    with open("stats.txt", "a") as f:
        f.write(f"Solo;{n};1;{duration:.2f}\n")

if __name__ == "__main__":
    main()
