from ipaddress import ip_network
for a in range(0,255+1):
    n = ip_network(f'183.192.{a}.0/255.255.252.0',0)
    k = 0
    r = 0
    for i in n:
        r += 1
        j = f'{i:b}'
        if j[15:].count('1') > 3:
            k+=1
    if k == r:
        print(a)
        break
