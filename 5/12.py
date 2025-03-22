def k(n):
    s = ''
    while n!= 0:
        s = str(n%3) + s
        n //= 3
    return s

def f(n):
    s = k(n)
    sum1 = 0
    for i in s:
        sum1 += int(i)
    if sum1%4 == 0:
        s = '1' + s[:-2]
    else:
        s = s + k((sum1%4)*3)
    return int(s,3)

a = []
for q in range(0,100000):
    r = f(q)
    if r > 353:
        a.append(r)
print(min(a))
