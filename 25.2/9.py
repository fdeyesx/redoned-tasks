k = 0
for x in range(6638225,6638322):
    k+=1
    d = set()
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    if len(d) == 2:
        print(k,x)
