def min_partitions(used, total):
    total_memory_used = sum(used)
    total.sort(reverse=True)
    n = 0
    i = 0
    while total_memory_used > 0 and i < len(used):
        total_memory_used -= total[i]
        i += 1
        n += 1
    return n


def min_partitions_alt(used, total):
    total_memory_used = sum(used)
    total.sort(reverse=True)
    n = 0
    for i in range(len(total)):
        total_memory_used -= total[i]
        if total_memory_used <= 0:
            return n+1
        n += 1


if __name__ == '__main__':
    print(min_partitions([3, 2, 1, 3, 1], [3, 5, 3, 5, 5]))
    print(min_partitions([1, 2, 3], [3, 3, 3]))
    print(min_partitions([3, 2, 5], [5, 5, 5]))
    print(min_partitions([1, 3, 5], [5, 5, 5]))
    print(min_partitions([1, 1, 3], [5, 5, 5]))
