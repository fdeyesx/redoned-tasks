from ipaddress import ip_network
n = ip_network('105.224.200.224/255.255.255.224')
k = 0
for i in n:
    j = f'{i:b}'
    if j.count('1')%4 == 0:
        k+=1
print(k)
