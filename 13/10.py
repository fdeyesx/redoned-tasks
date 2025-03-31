from ipaddress import ip_network
n = ip_network('165.44.96.0/255.255.248.0')
k = 0
for i in n:
    j = f'{i:b}'
    if '111' in j:
        k+=1
print(k)
