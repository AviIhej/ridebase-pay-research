# Ridebase Pay buyer research: Canada pass

Run date: 2026-11-05. Canada was done first. The United States pass is started and thin. Every US row is a pre-sell target only: the product does not handle US payouts today.

## Not finished

- The United States pass is thin: it has only the rows listed in the counts. It covers New York, Chicago, a few ride-hail startups and a few taxi companies. Texas, Colorado, Massachusetts, Ohio and most large cities have no rows.
- Zero rows for the `logistics`, `shuttles` and `rideshare-companies` segments. Courier sites that I could read showed no driver pay terms, and the shuttle searches returned job boards.
- 55 of 79 rows have no fleet or driver count. Most taxi sites publish none.
- No row has a public complaint about pay errors. I did not find one on a company's own page, and I did not use review sites.
- No row has a job post that mentions payroll, bookkeeping or dispatch admin. The few careers pages I read list licence requirements only.
- 19 Canadian taxi and limousine sites could not be read or gave no usable text. They are listed in `sources.md` with the reason.
- Provincial coverage is thin outside British Columbia, Ontario and Alberta. The BC licensee list names many more companies than the BC rows cover. Newfoundland and Labrador, the Territories and most of Quebec have no rows.
- Part XX is only partly verified. See "Claims checked" below.

## What I searched

- City of Toronto business licence data (taxicab broker category), the City of Calgary taxi and limousine brokerage lists and the BC Passenger Transportation Board taxi licensee list, to find licensed companies.
- Web searches by city and province for taxi companies, ride-hailing startups, non-emergency medical transport, accessible transport, airport shuttles, limousine and courier operators.
- Each company's own pages: home, about, contact, careers and driver pages. A row exists only where I read the company's own page. Directory listings, review sites and job boards were not used as sources for rows.
- US lists: the NYC Taxi and Limousine Commission FHV base report, the City of Chicago public passenger vehicle licence data and the California Public Utilities Commission TNC permit list, to find companies and size.
- Primary sources for two claims: the Income Tax Act text on Justice Laws and a Payments Canada press release.

## What I skipped and why

- LinkedIn: not scraped, per the rules.
- Sites whose robots.txt disallowed my fetcher: skipped and listed in `sources.md`.
- The BC Passenger Transportation Board search page: it sits behind a Cloudflare challenge and I did not bypass it. The taxi licensee list page loads without one and was used.
- canada.ca: the connection reset on every attempt. I used the Act text on Justice Laws instead.
- Large national operators and the ride-hailing majors. The brief asks for regional operators.
- Named personal emails: several sites publish a person's address. I did not record those. Rows carry a role inbox or a form, or say that none was found.
- Free-mail addresses: two rows (Taxi Plus and Riders Cab) carry a Gmail address that the company itself publishes as its business contact. They are marked in `contact_role`.
- A taxi site in the UK template style (premiertaxi.ca, "DBS cleared" text) and a Moncton site whose pages contain unrelated casino spam (whitecabrocks.ca): left out because I could not confirm they are active Canadian operators.

## Sites that blocked or were spam in the US pass

- fare.coop returned 403 to automated fetches. No row. I did not work around it.
- denveryellowcab.com, metrotaxidenver.com, yellowcabhouston.com and flashcab.com serve unrelated spam. They are left out.
- Yellow Cab Sacramento and several others publish only a named person's email, so those rows were not written.

## Injected or odd page text

No page told me to do anything. Two pages carried unrelated spam text (casino promotion in Turkish on whitecabrocks.ca and a casino page at kabu.ca). I ignored both and left them out of the CSV.

## Counts (97 rows)

By country: Canada 80, United States 17.

By segment: taxi 71, tnc-startups 7, nemt 6, other 13, logistics 0, shuttles 0, rideshare-companies 0.

By province (Canada): Ontario 24, British Columbia 23, Alberta 14, Quebec 6, Saskatchewan 4, Nova Scotia 3, Manitoba 3, New Brunswick 2, Prince Edward Island 1.

By state (United States): NY 8, CA 3, IL 2, DC 1, Multiple states 1, Not stated on pages read 1, WA 1. Rows with several states or none stated are counted under their entry in the CSV.

By size band (Calculated from the sourced vehicle or fleet counts in `driver_count_or_fleet`; the bands are my grouping): 500 or more 6, 200 to 499 12, 50 to 199 10, under 50 4, not published 65. Shareholder counts and trip counts were not used for bands, except Yellow Cab Vancouver, which uses its 325 owner-operator shareholders as the count. Richmond Taxi uses its 130 cabs, not the 1,000 drivers its about page claims. For New York black car bases the band uses the vehicles dispatched in May 2026 from the NYC TLC data, or the company's own fleet claim where one exists.

By fit score (Plan number: my own 1 to 5 score, see below): 5 has 4, 4 has 29, 3 has 34, 2 has 30.

## How rows were scored

- 5: the company states a commission share or a regular pay cycle in public.
- 4: a published fleet or driver count of 100 or more, a high published trip volume, a transit or health contract that implies per-trip settlement, account-billed accessible service, or a cooperative with member drivers.
- 3: a licensed operator with a published business contact where size or pay is not stated.
- 2: a small operator or one with no size evidence.

`how_they_pay_drivers` says "Not stated on pages read" unless the company's own page says how drivers are paid. R-Hero, Apt Rides and Checkmate Cabs state a payout schedule.

## Claims checked

Part XX (company claim: every platform that dispatches contract drivers owes a CRA return by 31 January, and owes each driver a copy).

- Sourced: the Income Tax Act, Part XX, requires a reporting platform operator to report to the Minister, and to give the information to the seller, no later than January 31 of the year after the seller is identified as a reportable seller. Source: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/page-233.html
- Sourced: the Act defines a platform operator as an entity that contracts with sellers to make a platform available, and a platform as software that connects sellers to users. A personal service excludes work done under an employment relationship. Source: https://laws-lois.justice.gc.ca/eng/acts/I-3.3/page-232.html
- No source yet: that every taxi dispatcher or fleet that has contract drivers meets the platform definition. A small cab company with phone dispatch and no software that connects sellers to users may fall outside it. The website wording is wider than the Act text I read. I did not reach the CRA guidance pages.

Interac share (company claim: Interac e-Transfer is how Canadian gig workers are most often paid, 43%, and how they most want to be paid, 48%).

- Sourced: Payments Canada press release says "Interac e-Transfer is the leading method used for gig workers to get paid (43%)" and that 48% want to be paid by it. The survey was run by Leger from February 27 to March 10, 2023, with 1,501 Canadians, margin of error 2.5%. Source: https://payments.ca/online-platforms-and-mobile-apps-frustrate-canadian-gig-workers-when-it-comes-pay-day-reveals-new
- Calculated: none. The figures cover gig workers in general. They do not cover taxi or ride-hailing drivers alone.

## Gaps for the next run

1. The rest of the United States pass: the Massachusetts, Colorado and Ohio ride-hail permit lists, the Texas licence list, and city taxi commission lists.
2. Courier and delivery fleets that pay owner-operators by the run. Most carrier sites load their text by script and gave me nothing to read.
3. Fleet counts for the 65 rows without one. Municipal plate counts by brokerage would fill most of them.
4. Job posts that mention payroll or dispatch admin, and public complaints about pay errors.
5. Prairie cabs that share a street address: Prairie Cabs and Yellow Cabs GP list the same Grande Prairie address and may be one operation.
6. Quebec, Newfoundland and Labrador and the Territories.
7. The remaining Toronto taxi brokers from the city licence list: Toronto 1 Taxi, Prestige Taxi Services, Checker Taxi, Imperial Taxi, Able Atlantic and Beeline Taxi, Unlimited Taxi and Limo Group, A-1 GTA Cab. Their own pages were empty or unreadable. Maple Leaf Taxi has a readable site but no fleet figure or email, so it has no row. Co-op Cabs and Royal Taxi share one licence address and phone line on the city list, so they are likely one operation.
8. The 29 Calgary limousine brokerages on the city list that have no row. The list names 33 and four have rows.
