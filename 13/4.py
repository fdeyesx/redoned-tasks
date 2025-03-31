from ipaddress import ip_network
n = ip_network('192.168.32.48/255.255.255.192',0)
k = 0
for i in n:
    j = f'{i:b}'
    if j.count('1')%5 != 0:
        k+=1
print(k)
