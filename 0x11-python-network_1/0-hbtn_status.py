#!/usr/bin/python3
"""
retrieve https://alx-intranet.hbtn.io/status
"""
if __name__ == "__main__":
    import urllib.request as req
    with req.urlopen('https://alx-intranet.hbtn.io/status') as ar:
        html = ar.read()
        print("Body response:$")
        print(f"\t- type: {type(html)}$")
        print(f"\t- content: {html}$")
        print(f"\t- utf8 content: {html.decode('utf-8')}$")
