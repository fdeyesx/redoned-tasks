for x in range(770_000,0,-1):
    d = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    if len(d) != 0:
        d = sorted(d)
        sum1 = sum(d)//len(d)
        if sum1%100 == 12:
            print(x,sum1)
