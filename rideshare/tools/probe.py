"""Probes candidate domains (args) and prints HTTP status, final URL and page title so a company site can be confirmed before it goes in a row."""
import sys, re, urllib.request, ssl
from concurrent.futures import ThreadPoolExecutor
def p(d):
    for u in ([d] if d.startswith('http') else ['https://'+d, 'https://www.'+d]):
        try:
            r = urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent':'Mozilla/5.0 (research; contact via repo owner)'}), timeout=15)
            t = r.read(60000).decode('utf-8','ignore'); m = re.search(r'<title[^>]*>(.*?)</title>', t, re.S|re.I)
            return f"{d} {r.status} {r.geturl()} | {re.sub(chr(10)+'|'+chr(13)+'|  +',' ',m.group(1)).strip()[:90] if m else ''}"
        except Exception as e: err = str(e)[:50]
    return f"{d} FAIL {err}"
if __name__ == '__main__':
    with ThreadPoolExecutor(12) as ex:
        for l in ex.map(p, sys.argv[1:]): print(l)
