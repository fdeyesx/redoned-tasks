from ipaddress import ip_network
n = ip_network('156.132.15.138/255.255.252.0',0)
r = 0
for i in n:
    if str(i) == '156.132.15.138':
        print(f'{r}. {i}')
    r += 1
