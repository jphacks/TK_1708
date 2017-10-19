#! /usr/bin/env python3

import requests
import json

def ppost(d):
    h   = {'Content-Type': 'application/json'}
    tmp = requests.post("http://localhost:8545",
                        headers = h,
                        data    = json.dumps(d))
    resjson = json.loads(tmp.text)
    if "error" in resjson:
        print( "==error==" )
        print( resjson["error"] )
        raise
    else:
        return resjson["result"]

def eth_accounts():
    d = {"method":"eth_accounts","params":[],"id":1,"jsonrpc":"2.0"}
    return ppost(d)

def main ():
    print("accounts", eth_accounts())

main()
