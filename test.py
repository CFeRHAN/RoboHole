import openvpn_api
v = openvpn_api.VPN('192.168.1.1', 7505)


def Connect():
    
    try:
        v.connect()
        
    except:
        print("Fuck YOU")

    s = v.state
    u = s.state_name
    print(u)
    return u
# Connect()
print(Connect())