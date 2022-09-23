#!/usr/bin/python3
"""
POST request to post email to the url.
URL and email are passed as parameters.
"""
if __name__ == "__main__":
    import urllib.parse as parse
    import urllib.request as request
    from sys import argv
    url = argv[1]
    vaues = {'email': argv[2]}
    data = parse.urlencode(vaues).encode('utf-8')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
