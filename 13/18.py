from ipaddress import ip_network
for x in range(0,33):
    n = ip_network(f'122.21.49.91/{x}',0)
    a = n.network_address
    if str(a) == '122.21.48.0':
        print(x)
