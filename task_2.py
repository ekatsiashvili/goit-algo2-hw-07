from functools import lru_cache
from timeit import timeit
import matplotlib.pyplot as plt
from tabulate import tabulate
from splay_tree import SplayTree


@lru_cache(maxsize=128)
def fibonacci_lru(n):
    if n < 2:
        return n
    return fibonacci_lru(n - 1) + fibonacci_lru(n - 2)


def fibonacci_splay(n, tree):
    cached_value = tree.find(n)
    if cached_value is not None:
        return cached_value

    if n <= 1:
        value = n
    else:
        value = fibonacci_splay(n - 1, tree) + fibonacci_splay(n - 2, tree)

    tree.insert(n)
    return value


if __name__ == "__main__":
    results = []
    test_values = list(range(0, 951, 50))

    for n in test_values:
        lru_time = timeit(lambda: fibonacci_lru(n), number=10)

        splay_tree = SplayTree()
        splay_time = timeit(lambda: fibonacci_splay(n, splay_tree), number=10)

        results.append([n, lru_time, splay_time])

    headers = ["n", "LRU Cache (сек.)", "Splay Tree (сек.)"]
    print(tabulate(results, headers=headers, tablefmt="grid"))

    n_values = [row[0] for row in results]
    lru_times = [row[1] for row in results]
    splay_times = [row[2] for row in results]

    plt.plot(n_values, lru_times, label="LRU Cache")
    plt.plot(n_values, splay_times, label="Splay Tree")
    plt.xlabel("n")
    plt.ylabel("Час виконання (сек.)")
    plt.title("Порівняння часу виконання для обчислення чисел Фібоначчі")
    plt.legend()
    plt.grid()
    plt.show()
