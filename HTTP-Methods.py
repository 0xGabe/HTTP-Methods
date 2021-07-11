import requests
import sys

def prRed(skk): print("\033[91m{}\033[00m" .format(skk))

if len(sys.argv) != 2:
    prRed("[-] How to use -> python 10.10.10.10")
else:
    method_http = ['GET','POST','PUT','DELETE','OPTIONS','TRACE',]
    for method in method_http:
        req = requests.request(method, "http://"+sys.argv[1])
        print(method, req.status_code, req.reason) 
