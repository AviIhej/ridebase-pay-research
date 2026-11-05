"""Shared helper: add_rows() appends rows to rideshare/companies.csv after de-duplicating by domain, then name+city, against itself and payments/companies.csv."""
import csv, re, os, sys
from urllib.parse import urlparse
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
OUT = os.path.join(ROOT, 'rideshare', 'companies.csv')
PAY = os.path.join(ROOT, 'payments', 'companies.csv')
COLS = ["name","parent_company","website","country","province_or_state","hq_city","markets_served","tier","status","status_date","ride_types","app_store_url","play_store_url","year_founded","driver_count_or_fleet","size_basis","how_they_pay_drivers","contact_role","published_business_email_or_form","regulator_or_permit","permit_id","evidence_summary","fit_score_1_to_5","fit_reason","source_url","source_type","found_on"]
FREE = {'facebook.com','linkedin.com','gmail.com','yelp.com','instagram.com','wikipedia.org'}
def domain(u):
    if not u: return ''
    u = u.strip().lower()
    if '@' in u and '/' not in u: return ''
    if not u.startswith('http'): u = 'http://' + u
    h = urlparse(u).netloc.replace('www.', '')
    return '' if h in FREE else h
SUF = re.compile(r'\b(llc|l l c|inc|incorporated|corp|corporation|ltd|limited|co|company|the|dba)\b|[^a-z0-9 ]')
def nname(n): return re.sub(r'\s+', ' ', SUF.sub(' ', n.lower())).strip()
def load(path):
    if not os.path.exists(path): return []
    with open(path, newline='', encoding='utf-8') as f: return list(csv.DictReader(f))
def keys():
    doms, nc, names = set(), set(), set()
    for p in (OUT, PAY):
        for r in load(p):
            d = domain(r.get('website','')); 
            if d: doms.add(d)
            city = (r.get('hq_city') or r.get('city') or '').lower()
            nc.add((nname(r['name']), city)); names.add(nname(r['name']))
    return doms, nc, names
def add_rows(rows, name_only=False):
    doms, nc, names = keys()
    new = []
    for r in rows:
        d = domain(r.get('website',''))
        k = (nname(r['name']), r.get('hq_city','').lower())
        if (d and d in doms) or k in nc or (name_only and k[0] in names):
            continue
        if d: doms.add(d)
        nc.add(k); names.add(k[0]); new.append(r)
    exists = os.path.exists(OUT)
    with open(OUT, 'a', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=COLS, quoting=csv.QUOTE_ALL, extrasaction='ignore')
        if not exists: w.writeheader()
        for r in new: w.writerow({c: r.get(c, '') for c in COLS})
    print(f"added {len(new)} of {len(rows)}; total {len(load(OUT))}")
    return len(new)
