for x in range(18782,18822):
    d = []
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d.append(i)
            d.append(x // i)
    if len(d) > 0:
        r = []
        for j in d:
            if int(j)%2 == 1:
                r.append(int(j))
        if len(r) == 3:
            r = sorted(r)
            print(r[0], r[1], r[2])
