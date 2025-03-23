f = open('17.txt')
a = []
b = []
k = 0
for i in f:
    a.append(int(i))
for i in a:
    if i % 9 != 0 and i % 11 != 0:
        if i % 10 == 5 or i % 10 == 7:
            k += 1
            b.append(i)

sum1 = min(b) + max(b)
print(k, sum1)
