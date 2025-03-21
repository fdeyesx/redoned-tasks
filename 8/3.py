from itertools import product, repeat
k = 0
for i in product('0123456789abcde',repeat=5):
    s = ''.join(i)
    if s[0] != 0:
        if s.count('8') == 1:
            s = s.replace('b','a').replace('c','a').replace('d','a').replace('e','a')
            if s.count('a') > 1:
                k+=1
print(k)
