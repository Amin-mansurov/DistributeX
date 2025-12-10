from tabulate import tabulate

def load_stats():
    rows = []
    with open("stats.txt", "r") as f:
        for line in f:
            mode, n, clients, ms = line.strip().split(";")
            rows.append([mode, n, clients, f"{ms} ms"])
    return rows

def main():
    data = load_stats()
    table = tabulate(data, headers=["Режим", "Факториал", "Работники", "Время"], tablefmt="fancy_grid")
    print("\n📊 Сравнение времени:")
    print(table)

if __name__ == "__main__":
    main()
