def f(n):
    r = []
    for j in n:
        k = []
        for i in range(2, int(x ** 0.5) + 1):
            if j % i == 0:
                r.append(i)
                r.append(j // i)
        if len(k) == 2:
            r.append(j)
    return r

for x in range(670_000,770_000):
    d = []
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            d.append(i)
            d.append(x//i)
    if len(d) != 0:
        sum1 = 0
        k =f(d)
        for j in k:
            sum1 += int(j)
        if sum1%10 == 5:
            print(x,sum1)
