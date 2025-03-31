from ipaddress import ip_network
n = ip_network('101.157.240.0/255.255.252.0')
k = 0
for i in n:
    j = f'{i:b}'
    if j[:16].count('1') > j[16:].count('1'):
        k+=1
print(k)
