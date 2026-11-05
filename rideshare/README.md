# Rideshare company list (US and Canada), first pass

## Not finished (read this first)
- This pass stopped at 494 rows. It is a start, not an exhaustive list.
- 421 rows are New York for-hire vehicle bases from one registry. The count is heavy on New York because that registry is the only one found that lists hundreds of operators with fleet size.
- Registry rows (NYC TLC, WA DOL) were not checked for an app, a website or pay terms. Their `tier` is provisional: 'taxi with an app' means a dispatch base with under 100 vehicles, 'regional platform' means 100 or more. Neither is confirmed.
- No driver pay terms were found for registry rows. Only Tripcarma has a sourced commission share (80 percent to the driver). No weekly-payout evidence yet for any row.
- Canada is thin here (2 rows). The Canada file `payments/companies.csv` has about 100 rows and is used only for de-duplication.
- Not yet searched: airport permit rosters, remaining state and city lists (FL, GA, AZ, NV, OR, MD, VA, NC, OH, MI, MN), Ontario and Alberta municipal lists, app store developer pages, funding directories, conference exhibitor lists, Product Hunt.
- Rows with status unknown include licences marked terminated by Washington. A terminated licence alone is not treated as defunct.

## What was searched
See `sources.md`. Scripts are in `tools/`, each with a one-line note. Process notes are in `LEARNINGS.md`, `YIELD.csv` and `.claude/skills/rideshare-research/SKILL.md`.

## What was skipped and why
- Colorado PUC site: HTTP 403 from the CDN. Not bypassed.
- Chicago public passenger vehicle licences: licence holders are mostly limo and ambulance owners, not clearly ride-hail dispatchers.
- Washington "For Hire" licence type: mostly individuals. Personal names are not recorded.
- GitHub search for open datasets of ride-hail companies: only generic awesome-lists came back, none with company rows.
- Autonomous-vehicle operators (Waymo, Zoox, May Mobility): no contracted drivers to pay.
- Concierge services that book Uber or Lyft for customers (GoGoGrandparent) and companion-care firms: they do not dispatch their own drivers.
- No page asked for anything unusual; no instruction-like page text was found.

## Counts (494 rows)
- Country: US 492, CA 2.
- Status: active 479, unknown 11, defunct 4.
- Tier: taxi with an app 404, regional platform 54, niche 15, startup 15, white-label operator 4, national platform 2.
- State or province: NY 421, CA 22, NJ 20, WA 7, blank 7 (companies with no stated HQ), CT 3, MA 3, MN 2, one each IA, GA, NC, NM, PE, ON, CO, DC, TX.

## Known data issues
- NYC base rows use the dispatcher address on the TLC record; some are out of state (CA, NJ, CT) because the base is registered there. The `markets_served` field says New York City.
- The `hq_city` for NYC rows is parsed from the address by a rule and can be wrong.
- Contact fields are empty for registry rows. Registry email fields held personal addresses, so none were copied.
