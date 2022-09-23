#!/usr/bin/python3
"""
https://alx-intranet.hbtn.io/status
"""
if __name__ == "__main__":
    import urllib.request

    alx_req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(alx_req) as ar:
        html = ar.read()
        print("Body response:$")
        print(f"\t- type: {type(html)}$")
        print(f"\t- content: {html}$")
        print(f"\t- utf8 content: {html.decode('utf-8')}$")
