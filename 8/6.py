from itertools import product, repeat
r = 0
for i in product('01234567',repeat=5):
    s = ''.join(i)
    if s[0] != '0':
        if s.count('1') == 0:
            if len(set(s)) == len(s):
                for j in '0246':
                    s = s.replace(j,'+')
                for k in '1357':
                    s = s.replace(k, '-')
                if '++' not in s or '--' not in s:
                    r+=1
print(r)
