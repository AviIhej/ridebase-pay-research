# Learnings

Each entry: what I tried, the symptom, what worked, the rule.

1. Colorado PUC transportation page. Tried: curl puc.colorado.gov/transportation. Symptom: HTTP 403 CloudFront "Request blocked". What worked: nothing; I did not bypass it. Rule: log and take Colorado names from search results and company pages.
2. Guessing company domains (arrorides.com, joinfare.com, ride.coop and others). Symptom: proxy returns 502 "Tunnel connection failed" for hosts that do not resolve. Rule: find the real domain by search first. Never batch-guess more than 10.
3. gokango.com. Symptom: page title is a backlink marketplace, not the Kango ride company. Rule: check the title of every probed domain; leave website blank when it does not match.
4. alto.com, fasten.com, safr.com. Symptom: unrelated or changed business at the guessed domain. Rule: a domain that loads is not proof it is the company.
5. State TNC lists (NJ MVC, MA DPU, TX TDLR, PA PUC). Symptom: pages name only Uber, Lyft and a few others, or give counts without names. Rule: state lists give 2 to 6 names each; spend at most 2 page reads on each.
6. WA DOL "For Hire" licence type (data.wa.gov ucdg-xgbj). Symptom: most rows are individuals. Rule: only the Transportation Network Company type is used. Never record personal names.
7. Chicago PPV licences (data.cityofchicago.org tfm3-3j95). Symptom: company_name is a licence or medallion holder, mostly limo and ambulance operators, not clearly ride-hail dispatchers. Rule: skipped.
8. NYC TLC FHV active dataset has one row per vehicle with driver names. Rule: aggregate by base in the query ($group) so no driver data is downloaded.

## Dead ends
- Colorado PUC site (403).
- Domain guessing without a search hit.
- Aggregator listicles (Ridester, rankred): thin, mostly global companies.
