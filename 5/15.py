def f(n):
    s = str(bin(n))[2:]
    n1 = 0
    while n1 < 2:
        if len(list(s))%2 == 0:
            s = s + '10'
        else:
            s = '11' + s
        n1+=1
    return int(s,2)

a = []
k = 0
for q in range(100,201):
    r = f(q)
    if r%2 == 0:
        a.append(r)
        k+=1
print(len(a),k)
