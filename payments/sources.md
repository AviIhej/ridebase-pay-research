# Sources and how to repeat the search

Run date: 2026-11-05. Fetches used `curl` with the user agent `ridebase-research/1.0` and a robots.txt check before each company page.

## Registries and lists used

| Source | URL | What it covers |
|---|---|---|
| City of Toronto Open Data, Business licences and permits | https://open.toronto.ca/dataset/municipal-licensing-and-standards-business-licences-and-permits/ | Licence records including the category TAXICAB BROKER (113 records, 20 active with no cancel date on 2026-11-05) and LIMOUSINE SERVICE COMPANY (239 records, 13 active). Query the datastore API with the resource id 169e90ba-3ae0-43dd-8b2f-919e87002f50 and filter on Category. |
| City of Calgary, Taxi and limousine brokerages | https://www.calgary.ca/taxis-ride-share/brokers.html and https://www.calgary.ca/taxis-ride-share/licensed-operators.html | Four licensed taxi brokerages (list dated Nov. 20, 2023) and 33 limousine brokerages (list dated Sep. 6, 2024), with phone numbers. |
| BC Passenger Transportation Board, Taxi licensee list (updated September 2026) | https://www.ptboard.bc.ca/taxi-licensee-list | Legal name, trade name and regional district for every BC taxi licensee. Used to find company names, then each company's own site was read. |
| BC Employment Standards, ride-hail and delivery minimum wage | https://www2.gov.bc.ca/gov/content/employment-business/employment-standards-advice/employment-standards/forms-resources/igm/esr-part-4-section-18-2 | Minimum hourly wage for ride-hail workers applies to engaged time, and the platform must pay any shortfall in a pay period. |
| NYC Taxi and Limousine Commission, FHV Base Aggregate Report | https://data.cityofnewyork.us/resource/2v9c-2k7f.json | Monthly dispatched trips and vehicles for every New York for-hire dispatch base. Query with a where clause on year and month. May 2026 was the latest month used. |
| City of Chicago, Public Passenger Vehicle Licenses | https://data.cityofchicago.org/resource/tfm3-3j95.json | Active vehicles by company and vehicle type (livery, taxi, medicar). Group on company_name with status ACTIVE. Names only, no websites. |
| California Public Utilities Commission, TNC permits issued | https://www.cpuc.ca.gov/regulatory-services/licensing/transportation-licensing-and-analysis-branch/transportation-network-companies/tnc-permits-issued | Permitted ride-hail companies in California with dba names. |
| Massachusetts, Colorado and Ohio TNC lists | https://www.mass.gov/info-details/tnc-operating-permits ; https://puc.colorado.gov/transportation-network-companies-industry-info ; https://puco.ohio.gov/transportation/trucking/resources/transportation-network-companies | Found by search and not yet mined. Next run should read them. |
| Halifax Regional Municipality, taxi brokers | https://www.halifax.ca/business/licences/taxi-limousine-tncs/information-taxi-brokers-independent-brokers | Names five licensed brokers: Bob's Taxi, Casino Taxi, Satellite Taxi, Yellow Cab and Extra Care Accessible Service. |
| Wikipedia, Taxis of Canada | https://en.wikipedia.org/wiki/Taxis_of_Canada | Secondary source. Names the Ottawa licensed taxi companies and the BC licensed ride-hailing companies. Used only to find names. |
| Justice Laws, Income Tax Act, Part XX | https://laws-lois.justice.gc.ca/eng/acts/I-3.3/page-232.html and https://laws-lois.justice.gc.ca/eng/acts/I-3.3/page-233.html | Definitions of platform, platform operator, personal service, reporting platform operator, and the January 31 reporting date. |
| Payments Canada press release | https://payments.ca/online-platforms-and-mobile-apps-frustrate-canadian-gig-workers-when-it-comes-pay-day-reveals-new | Leger survey of 1,501 Canadians, February 27 to March 10, 2023. Interac e-Transfer 43% for how gig workers are paid and 48% for how they want to be paid. |

## Lists I tried and could not use

- BC Passenger Transportation Board search page (https://www.ptboard.bc.ca/licensee_list.htm): behind a Cloudflare challenge. Not bypassed. The taxi licensee list page above works.
- Search phrases such as "paid weekly" with taxi or ride-hail: returned job boards and guides, no company pages.
- Commission des transports du Québec list of intermédiaires en services de transport: covers heavy-vehicle transport, not taxis.
- City of Edmonton open data search for taxi: returned only Chicago data.
- canada.ca CRA Part XX guidance: connection reset on every attempt.
- fare.coop: 403 to every automated request. Not worked around.
- Canadian Public Transit Discussion Board taxi list: no company links on the page.

## Searches to repeat

Run these in a web search and keep only results on a company's own domain.

- `taxi company [city] fleet cabs become a driver` for each city
- `[city] taxi company official website` for Calgary, Edmonton, Winnipeg, Saskatoon, Regina, Halifax, Moncton, Saint John, Charlottetown, St. John's, Gatineau, Montreal, Quebec City
- `Canadian ride-sharing startup recruiting drivers` and `ride-hail company Lower Mainland drivers keep percent`
- `wheelchair accessible transportation company [city] our drivers`
- `non-emergency medical transportation company [province] contract drivers per trip`
- `airport shuttle company [city] fleet drivers`

## Company pages that could not be read

Robots.txt disallowed the fetch (not retried):
- https://checkercabs.ca/
- https://sooyellowcab.com/
- https://pacificcabs.com/
- http://www.surreymetrotaxi.com/
- https://www.protaxis.ca/
- https://taxidirectnord.ca/
- https://jiffycabs.ca/
- http://checkerstaxi.com/

Page text empty or loaded by script, or the only text was spam or a template:
- https://www.kelownacabs.com/
- https://www.calgaryunitedcabs.com/
- https://unitedtaxi.ca/
- https://www.toronto1taxi.com/
- https://www.crowntaxi.ca/
- https://www.taxiunion.com/
- https://www.taxicoop.com/
- https://www.taxiquebec.ca/
- https://www.94cabsreddeer.com/
- https://carecabs.ca/
- https://citywidetaxioshawa.com/ (the only emails on the page were on unrelated domains)

## Where each row's evidence lives

Every row in `companies.csv` has a `source_url` on the company's own domain. Rows that also cite a municipal list say so in `evidence_summary`.
