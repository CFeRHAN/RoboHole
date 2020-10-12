import openvpn_api.vpn

v = openvpn_api.VPN('localhost', 7505)

def Connect():
    
    try:
        v.connect()
        p = v.connect()
        s = v.state
        s.state_name
        return p
    except:
        pass

def Disconnect():
    
    v.disconnect
    print(v.state.state_name)