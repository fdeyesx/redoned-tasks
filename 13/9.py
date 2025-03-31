from ipaddress import ip_network
n = ip_network('235.86.56.0/255.255.248.0')
k = 0
for i in n:
    j = f'{i:b}'
    if j[-2:] == '11':
        k+=1
print(k)
