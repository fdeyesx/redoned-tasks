from ipaddress import ip_network
n = ip_network('112.208.0.0/255.255.128.0')
k = 0
for i in n:
    j = f'{i:b}'
    if j.count('1')%11 == 0:
        k+=1
print(k)
