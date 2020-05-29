def add_five(N):
    pos = True if N >= 0 else False
    N = list(str(N)) if pos else (list(str(-1*N)))

    if not pos:
        N.reverse()
    if int(N[0]) < 5 and pos:
        N.insert(0, '5')
    else:
        sep = None
        r = range(len(N)-1) if pos else range(len(N)-1, 0, -1)
        for i in range(len(N)-1):
            if int(N[i]) >= 5 and int(N[i+1]) < 5:
                sep = i
        if sep is None:
            N.append('5')
        else:
            N.insert(sep+1, '5')
    if not pos:
        N.reverse()
        N = -1*int(''.join(N))
    else:
        N = int(''.join(N))
    return N


if __name__ == '__main__':
    print(add_five(-7055))
    print(add_five(-7065))
    print(add_five(0))
    print(add_five(-1))
    print(add_five(670))
    print(add_five(-305))
    print(add_five(-500))
