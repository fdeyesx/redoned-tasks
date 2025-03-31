for x in range(112_500_000,112_550_000 + 1):
    d = []
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            d.append(i)
            d.append(x//i)
    if len(d) >= 2:
        d = sorted(d)
        M = int(d[-1]) + int(d[-2])
        if str(M)[-4:] == '1214':
            print(x)
