k = 0
for a in range(-500,500):
    d = set()
    for x in range(-1000,1000):
        for y in range(-1000,1000):
            f =  ((a < x) or (x**2 - 7*x + 10 > 0)) and ((a >= y) or (y**2 + 7*y + 12 >0))
            d.add(f)
    if False not in d:
        k+=1
print(k)
