from itertools import product, repeat
k = 0
for i in product('берск',repeat=5):
    s = ''.join(i)
    k+=1
for i in product('берск',repeat=6):
    s = ''.join(i)
    k+=1
for i in product('берск',repeat=7):
    s = ''.join(i)
    k+=1
print(k)
