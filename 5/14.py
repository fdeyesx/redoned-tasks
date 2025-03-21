def k(n):
    s = ''
    while n!= 0:
        s = str(n%7) + s
        n //= 7
    return s

def f(n):
    s = k(n)
    if int(s[-1])%2 == 0:
        s = '6' + s
    else:
        s = '5' + s
    return int(s,7)

a = []
for q in range(343,2402):
    r = f(q)
    if r > 14500:
        a.append(r)
print(len(a))
