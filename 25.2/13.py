k = 0
for x in range(800_000,10**20):
    d = []
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d.append(i)
            d.append(x // i)
    if len(d) > 0:
        m = min(d) + max(d)
        if m%138 == 0:
            print(x,m)
            k += 1
            if k == 5:
                break
