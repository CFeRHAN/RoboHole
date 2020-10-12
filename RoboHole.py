import time
import webbrowser
import os
from OpenHole import Connect
from OpenHole import Disconnect


browserExe = "iexplore.exe"
url = 'https://youtube.com'
testurl = 'https://httpbin.org/ip'

i = 0
p = 0

def OpenUrl():
    webbrowser.open_new(testurl)

while i <= 2000:
    if (Connect()== False):
        Connect()
    OpenUrl()
    i += 1
    time.sleep(6)
    if (i % 5 == 0):
        time.sleep(2)
        os.system("taskkill /f /im "+browserExe)
        Disconnect()