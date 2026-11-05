---
name: rideshare-research
description: Playbook for building rideshare/companies.csv, the list of US and Canadian ride-hailing companies that buy Ridebase Pay.
---

# Rideshare research playbook

## Order
1. Read rideshare/LEARNINGS.md and rideshare/YIELD.csv first.
2. Push after every 25 rows with `git push -u origin research/rideshare`. Update rideshare/STATUS.md.
3. Dedupe through tools/common.py add_rows (domain, then name and city, against payments/companies.csv).

## Best yield per minute
1. Socrata open data with a $group query. NYC TLC FHV active vehicles (8wbx-tsch) gave 447 base rows in 15 minutes with fleet counts. Always aggregate in the query; the raw table has driver names.
2. data.wa.gov ucdg-xgbj filtered to license_type Transportation Network Company: 13 rows with licence status and dates.
3. CPUC TNC permits-issued page: one HTML table, 19 names.
4. Web search for niche types (women-only, accessible, rural, teen, defunct). News articles give names, cities and closure dates.
5. State pages (NJ, MA, TX, PA): 2 to 6 names each, low yield.

## Reading a source
- Use the Socrata catalog API https://api.us.socrata.com/api/catalog/v1?q=<term> to find datasets.
- Check robots.txt before page reads. A 403 from a CDN means stop and log it.
- Probe a domain with tools/probe.py and compare the title to the company before using it.

## Judging a source
- Does each row name a company with a city or state?
- Does it give size (vehicles, drivers) or only a name?
- Is the licence for dispatching rides, or for owning vehicles?
- If two page reads add no new company, drop the source.

## Row rules
- Every row has a source_url. Size and pay claims start with Sourced, Calculated or No source yet.
- Status unknown unless a source says the company stopped; a terminated licence alone is unknown.
- Never store driver names. Never guess emails. No competitor names, no em dashes, no attribution lines in commits.
- Autonomous-vehicle operators with no contracted drivers are not buyers.
