from json import load

try:
    from urllib2 import urlopen, URLError, HTTPError  # Python 2.7
except ImportError:
    from urllib.request import urlopen, URLError, HTTPError   # Python 3.5


def get_public_ip():
    public_sites = [
        'http://jsonip.com',
        'http://httpbin.org/ip'
    ]

    for url in public_sites:
        ip = ''
        for key in ['origin', 'ip']:
            try:
                j = load(urlopen(url))
                if key in j.keys():
                    ip = j[key]
            except (HTTPError, URLError):
                pass
        if ip:
            return ip
    return ''
