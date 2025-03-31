from ipaddress import ip_network
n = ip_network('185.8.0.0/255.255.128.0')
k = []
for i in n:
    j = f'{i:b}'
    k.append(j.count('1'))
print(max(k))
