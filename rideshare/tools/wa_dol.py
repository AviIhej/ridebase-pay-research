"""Pulls Washington DOL business licences of type Transportation Network Company (data.wa.gov ucdg-xgbj). Skips individuals and one shipping agency."""
import sys, json, urllib.request, urllib.parse; sys.path.insert(0, __file__.rsplit('/',1)[0]); from common import *
q = "https://data.wa.gov/resource/ucdg-xgbj.json?" + urllib.parse.urlencode({"license_type":"Transportation Network Company","$limit":"500"})
SKIP = {'SHELBY L MCCAIN','NORTON LILLY INTERNATIONAL, INC.'}
rows = []
for r in json.load(urllib.request.urlopen(q, timeout=60)):
    n = r['business_name']
    if n in SKIP: continue
    act = r['license_status'] == 'Active'
    exp = r['expiration_date'][:10]
    rows.append(mk(n.title().replace(', Inc.', ', Inc.'), 'regional platform' if 'TAXI' not in n and 'CAB' not in n else 'taxi with an app', 'US', r['business_state'] or 'WA', r['business_city'].title(),
        ride='Ride-hail (WA TNC licence)', reg='Washington State Department of Licensing, Transportation Network Company licence', pid=r['license_number'], mk_='Washington',
        status='active' if act else 'unknown', sdate=(r['first_issue_date'][:10] if act else exp),
        ev=f"WA DOL record: licence {r['license_number']} status {r['license_status']}, first issued {r['first_issue_date'][:10]}, expires {exp}. " + ('' if act else 'Licence terminated; whether the company stopped operating is not confirmed.'),
        src='https://data.wa.gov/Business-Licensing/Department-of-Licensing-s-Business-Licenses-Related-/ucdg-xgbj', stype='regulator open data'))
add_rows(rows)
