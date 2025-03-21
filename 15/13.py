for a in range(1,1000):
    d = set()
    for x in range(1,2000):
        for p in range(5,138):
            f = ((x%115 == 0) and (x%5 != 0)) or (((a%x == 0) <= (a%5 != 0)) and (a != p))
            d.add(f)
    if False and True in d:
        print(a)
        break
