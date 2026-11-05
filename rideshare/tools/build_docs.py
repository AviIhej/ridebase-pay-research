"""Builds the counts for README.md and the ranked list in top-targets.md from companies.csv."""
import sys, re, collections; sys.path.insert(0, __file__.rsplit('/',1)[0]); from common import *
rows = load(OUT)
def n(r):
    m = re.match(r'([\d,]+)', r['driver_count_or_fleet']); return int(m.group(1).replace(',','')) if m else 0
act = [r for r in rows if r['status']=='active']
act.sort(key=lambda r: (-int(r['fit_score_1_to_5'] or 0), -n(r)))
out = ["# Top 50 active targets (so far)\n", "Ranked by fit score, then fleet size. Fleet figures for NYC bases are Calculated from the TLC dataset (active vehicle licences per base), not driver counts. Evidence for weekly payouts is not yet found for most rows; the rows marked 'Not stated' need a company page read.\n", "| # | Company | State | Size | Score | Evidence | Source |", "|---|---|---|---|---|---|---|"]
for i, r in enumerate(act[:50], 1):
    ev = r['evidence_summary'][:160].replace('|','/')
    out.append(f"| {i} | {r['name']} | {r['province_or_state']} | {r['driver_count_or_fleet'] or 'No source yet'} | {r['fit_score_1_to_5']} | {ev} | {r['source_url']} |")
open(__file__.rsplit('/',2)[0] + '/top-targets.md', 'w').write('\n'.join(out) + '\n')
def tab(k): return '\n'.join(f"- {a or '(blank)'}: {b}" for a, b in collections.Counter(r[k] for r in rows).most_common())
print(len(rows)); 
for k in ('country','province_or_state','tier','status'): print('##',k); print(tab(k))
