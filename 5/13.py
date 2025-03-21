def k(n):
    s = ''
    while n!= 0:
        s = str(n%6) + s
        n //= 6
    return s

def f(n):
    s = k(n)
    if n%3 == 0:
        s = s + s[:2]
    else:
        s = s + k((n%3)*10)
    return int(s,6)

a = []
for q in range(1,1000):
    r = f(q)
    if r > 680:
        a.append(r)
print(min(a))
