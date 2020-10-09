import time
import webbrowser
import os
import openvpn_api

proxy = "20speed487631:546449@127.0.0.1"
proxies = [
    "20speed487631:546449@127.0.0.2"
    "20speed487631:546449@127.0.0.3"
    "20speed487631:546449@127.0.0.4"
]
v = openvpn_api.VPN(proxy, 7505)
browserExe = "iexplore.exe" 
url = 'gestyy.com/ee27TQ'
i = 0
p = 0
#j= 2 * i
def OpenUrl():
    webbrowser.open_new(url)


while i <= 5:
    v.connect()
    OpenUrl()
    i += 1
    time.sleep(7)
    if (i % 5 == 0):
        time.sleep(2)
        os.system("taskkill /f /im "+browserExe)
        v.disconnect()
        proxy = proxies[p]
        p += 1
        break