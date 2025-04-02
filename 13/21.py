from ipaddress import ip_network
n = ip_network('192.168.156.235/255.255.255.240',0)
r = 0
for i in n:
    if str(i) == '192.168.156.235':
        print(f'{r}. {i}')
    r += 1
