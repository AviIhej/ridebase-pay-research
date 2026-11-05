"""Aggregates the NYC TLC active FHV vehicle dataset (Socrata 8wbx-tsch) by base and writes one company row per base with 20+ vehicles. No driver names are kept."""
import json, re, sys, urllib.request, urllib.parse, datetime
sys.path.insert(0, __file__.rsplit('/',1)[0]); from common import *
q = "https://data.cityofnewyork.us/resource/8wbx-tsch.json?" + urllib.parse.urlencode({"$select":"base_number,base_name,base_type,base_address,base_telephone_number,website,count(*) as n","$group":"base_number,base_name,base_type,base_address,base_telephone_number,website","$order":"n DESC","$limit":"5000"})
data = json.load(urllib.request.urlopen(q, timeout=90))
SUFX = {'AVENUE','AVE','STREET','ST','ROAD','RD','BLVD','BOULEVARD','PLAZA','PARKWAY','HIGHWAY','DRIVE','DR','LANE','CONCOURSE','EXPRESSWAY','PLACE','WAY','COURT','BROADWAY','TURNPIKE','PKWY','PL','STREET.','FLOOR'}
def parse(a):
    t = a.split(); 
    if len(t) < 3: return '', ''
    st, zp = t[-2], t[-1]; rest = t[:-2]
    idx = max([i for i, w in enumerate(rest) if w.upper().strip('.,') in SUFX] or [-1])
    city = ' '.join(rest[idx+1:]) if idx >= 0 and idx+1 < len(rest) else ''
    city = {'LIC':'Long Island City','LONGISLAND CITY':'Long Island City'}.get(city.upper(), city.title())
    return city, st
# merge multiple base numbers of one operator name
agg = {}
for r in data:
    n = int(r['n']); 
    key = r['base_name'].strip().upper()
    if key in agg: agg[key]['n'] += n; agg[key]['bases'].append(r['base_number'])
    else: agg[key] = {**r, 'n': n, 'bases': [r['base_number']]}
rows = []
today = datetime.date.today().isoformat()
for key, r in agg.items():
    if r["n"] < int(sys.argv[1] if len(sys.argv)>1 else 20): continue
    city, st = parse(r.get('base_address',''))
    w = r.get('website','')
    web = '' if '@' in w or '.' not in w else w if w.startswith('http') else 'https://' + w.lower()
    big = r['n'] >= 100
    rows.append(dict(name=r['base_name'].title() if r['base_name'].isupper() else r['base_name'], website=web, country='US', province_or_state=st or 'NY', hq_city=city,
        markets_served='New York City', tier='regional platform' if big else 'taxi with an app', status='active', status_date=today,
        ride_types=f"For-hire vehicle base ({r['base_type'].lower()})", driver_count_or_fleet=f"{r['n']} active vehicles",
        size_basis=f"Sourced: count of active NYC TLC FHV vehicle licences affiliated with base(s) {', '.join(r['bases'])} in the TLC dataset on {today}",
        how_they_pay_drivers='Not stated in the registry', contact_role='Base dispatch office', 
        regulator_or_permit='NYC Taxi and Limousine Commission FHV base', permit_id=', '.join(r['bases']),
        evidence_summary=f"Active TLC-licensed FHV base with {r['n']} affiliated active vehicles. Registry shows address {r.get('base_address','').replace('  ',' ')} and phone {r.get('base_telephone_number','')}. App or driver pay terms not yet checked.",
        fit_score_1_to_5='3' if r['n']>=100 else '2', fit_reason='Calculated: fleet of 100 or more affiliated vehicles means many drivers to pay.' if big else 'Calculated: under 100 affiliated vehicles, pay terms unknown.',
        source_url='https://data.cityofnewyork.us/Transportation/For-Hire-Vehicles-FHV-Active/8wbx-tsch', source_type='regulator open data', found_on=today))
print(len(rows)); add_rows(rows)
