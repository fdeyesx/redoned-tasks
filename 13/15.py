from ipaddress import ip_network
n = ip_network(f'140.37.235.224/255.255.240.0',0)
print(n.network_address)
