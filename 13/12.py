from ipaddress import ip_network
for r in range(0,33):
    n = ip_network(f'130.140.241.137/{r}',0)
    a = str(n.network_address)
    if a == '130.140.240.0':
        r = n.netmask
        r = f'{int(r):b}'
        print(r.count('1'))
