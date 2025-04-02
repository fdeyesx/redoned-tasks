from ipaddress import ip_network
k = 0
for x in range(20,33):
    n = ip_network(f'175.122.80.0/{x}')
    if n.num_addresses >= 60:
        for i in n:
            if str(i) == '175.122.80.13':
                print(i)
                k+=1
        print(n, k)
print(k)
