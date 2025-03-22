from itertools import product, repeat
r = 0
for i in product('01234567',repeat=7):
    s = ''.join(i)
    if s[0] != '0':
        for j in '02468':
            s = s.replace(j,'+')
        if s.count('+') == 2:
            for k in '135':
                s = s.replace(k,'-')
            if '-7' not in s and '7-' not in s:
                r+=1
print(r)
