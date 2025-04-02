from ipaddress import ip_network
for r in range(0,33):
    n1 = ip_network(f'118.187.59.255/{r}',0)
    n2 = ip_network(f'118.187.65.115/{r}',0)
    a1 = n1.network_address
    a2 = n2.network_address
    r1 = n1.broadcast_address
    r2 = n2.broadcast_address
    if a1 != a2:
        if str(r1) != '118.187.59.255':
            if str(r2) != '118.187.65.115':
                print(r)
