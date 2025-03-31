from ipaddress import ip_network
n = ip_network('122.159.136.144/255.255.255.248')
k = 0
for i in n:
    j = f'{i:b}'
    if j.count('1')%4 != 0:
        k+=1
print(k)
