import random
import time
from lru import LRUCache


def range_sum_no_cache(array, L, R):
    return sum(array[L : R + 1])


def update_no_cache(array, index, value):
    array[index] = value


lru_cache = LRUCache(1000)


def range_sum_with_cache(array, L, R):
    cache_key = (L, R)
    cached_sum = lru_cache.get(cache_key)
    if cached_sum != -1:
        return cached_sum

    result = sum(array[L : R + 1])
    lru_cache.put(cache_key, result)
    return result


def update_with_cache(array, index, value):
    array[index] = value

    invalid_keys = [key for key in lru_cache.cache if key[0] <= index <= key[1]]
    for key in invalid_keys:
        del lru_cache.cache[key]


N = 100000
Q = 50000
array = [random.randint(1, 100) for _ in range(N)]
queries = []
for _ in range(Q):
    query_type = random.choice(["Range", "Update"])
    if query_type == "Range":
        L = random.randint(0, N - 1)
        R = random.randint(L, N - 1)
        queries.append((query_type, L, R))
    elif query_type == "Update":
        index = random.randint(0, N - 1)
        value = random.randint(1, 100)
        queries.append((query_type, index, value))


start_time = time.time()
for query in queries:
    if query[0] == "Range":
        _, L, R = query
        range_sum_no_cache(array, L, R)
    elif query[0] == "Update":
        _, index, value = query
        update_no_cache(array, index, value)
no_cache_time = time.time() - start_time


start_time = time.time()
for query in queries:
    if query[0] == "Range":
        _, L, R = query
        range_sum_with_cache(array, L, R)
    elif query[0] == "Update":
        _, index, value = query
        update_with_cache(array, index, value)
cached_time = time.time() - start_time

print(f"Час виконання без кешування: {no_cache_time:.2f} секунд")
print(f"Час виконання з LRU-кешем: {cached_time:.2f} секунд")
