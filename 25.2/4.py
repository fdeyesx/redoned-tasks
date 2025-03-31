for x in range(1000,10000):
    d = []
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            d.append(i)
            d.append(x//i)
    if len(d) != 0:
        d = sorted(d)
        sum1 = 0
        for j in d:
            sum1 += int(j)
        if sum1%100 == 23:
            print(x,sum1)
