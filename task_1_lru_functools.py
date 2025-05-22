import random
import time
from functools import lru_cache

N = 100_000
Q = 50_000
K = 1000
global_array = [random.randint(1, 100) for _ in range(N)]


def range_sum_no_cache(global_array, L, R):
    return sum(global_array[L : R + 1])


def update_no_cache(global_array, index, value):
    global_array[index] = value


@lru_cache(maxsize=K)
def range_sum_with_cache(L, R):
    global global_array
    return sum(global_array[L : R + 1])


def update_with_cache(index, value):
    global global_array
    global_array[index] = value
    range_sum_with_cache.cache_clear()


queries = []
for _ in range(Q):
    if random.choice([True, False]):
        L, R = sorted(random.sample(range(N), 2))
        queries.append(("Range", L, R))
    else:
        index = random.randint(0, N - 1)
        value = random.randint(1, 100)
        queries.append(("Update", index, value))

start_time = time.time()
for query in queries:
    if query[0] == "Range":
        _, L, R = query
        range_sum_no_cache(global_array, L, R)
    elif query[0] == "Update":
        _, index, value = query
        update_no_cache(global_array, index, value)
no_cache_time = time.time() - start_time


start_time = time.time()
for query in queries:
    if query[0] == "Range":
        _, L, R = query
        range_sum_with_cache(L, R)
    elif query[0] == "Update":
        _, index, value = query
        update_with_cache(index, value)
cached_time = time.time() - start_time


print(f"Час виконання без кешування: {no_cache_time:.2f} секунд")
print(f"Час виконання з LRU-кешем: {cached_time:.2f} секунд")
