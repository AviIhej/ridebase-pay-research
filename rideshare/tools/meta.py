"""Prints title, meta description and the first 300 chars of visible text for each URL argument, so evidence for a row comes from the company's own page."""
import sys, re, html, urllib.request
for u in sys.argv[1:]:
    try:
        t = urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent':'Mozilla/5.0 (research)'}), timeout=20).read(200000).decode('utf-8','ignore')
        d = re.search(r'<meta[^>]+(?:name|property)=["\'](?:og:)?description["\'][^>]+content=["\'](.*?)["\']', t, re.S|re.I)
        b = re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',re.sub(r'(?s)<(script|style).*?</\1>',' ',t))))
        print(u, '|', html.unescape(d.group(1))[:250] if d else '', '|', b[:300], '\n')
    except Exception as e: print(u, 'FAIL', str(e)[:60], '\n')
