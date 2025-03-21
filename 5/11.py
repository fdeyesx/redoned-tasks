def k(n):
    s = ''
    while n!= 0:
        s = str(n%8) + s
        n //= 8
    return s

def f(n):
    s = k(n)
    s_c = s
    for i in '02468':
        s_c = s_c.replace(i,'+')
    for j in '13579':
        s_c = s_c.replace(j,'-')
    if s_c.count('+')%2 == 1:
        if len(s) >= 3:
            s = s[-3:] + '46'
        else:
            s = s + '46'
    else:
        l = k(n%8)
        s = l + s
    return int(s,8)

a = []
for q in range(80,1000):
    r = f(q)
    a.append(r)
print(min(a))
