def f(n):
    s = str(bin(n))[2:]
    if s.count('1')%2 == 0:
        s = s + '10'
    else:
        s = '11' + s
    return int(s,2)

a = []
for q in range(100,201):
    r = f(q)
    if r%2 == 0:
        a.append(r)
print(len(a))
