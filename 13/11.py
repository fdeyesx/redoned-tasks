from ipaddress import ip_network
for r in range(0,33):
    n = ip_network(f'143.172.12.144/{r}',0)
    a = str(n.network_address)
    if a == '143.172.8.0':
        print(n.netmask)
