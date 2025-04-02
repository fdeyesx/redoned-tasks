from ipaddress import ip_network
n = ip_network('192.168.32.160/255.255.255.240')
k = 0
for i in n:
    j = f'{i:b}'
    if j.count('1')%2 == 0:
        k+=1
print(k)
