from ipaddress import ip_network
for a in range(0,255+1):
    n = ip_network(f'223.167.{a}.167/255.255.255.192',0)
    k = 0
    r = 0
    for i in n:
        r += 1
        j = f'{i:b}'
        if j[16:].count('1') >= j[:16].count('1'):
            k+=1
    if k == r:
        print(a)
