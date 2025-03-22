def f(n):
    s = str(bin(n))[2:]
    if s.count('1')%2 == 0:
        s = '10' + s[2:] +'0'
    else:
        s = '11' + s[2:] + '1'
    return int(s,2)
a = []
for i in range(28,100):
    r = f(i)
    a.append(r)
print(min(a))
