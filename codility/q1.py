def sum_to_zero(N):
    half = int(N/2)
    result = []
    for i in range(1, half+1):
        result.append(i)
        result.append(-i)
    if N % 2 != 0:
        result.append(0)
    return result


if __name__ == '__main__':
    print(sum_to_zero(100))
