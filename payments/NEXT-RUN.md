# Next run

Written 2026-11-05. State at writing: 104 rows (81 Canada, 23 US), all pushed to develop and research/payments-ca.

## Best five sources to start with

1. BC Passenger Transportation Board taxi licensee list, https://www.ptboard.bc.ca/taxi-licensee-list. Best rate so far: 22 rows in 30 minutes. About two thirds of the names are still unread. Trade names to try next: Surrey and Langley companies, Prince George Taxi, Penticton and Salmon Arm taxis, Whistler Taxi.
2. NYC TLC FHV Base Aggregate Report, https://data.cityofnewyork.us/resource/2v9c-2k7f.json. Gives trips and vehicles per dispatch base. About 80 bases had over 3,000 trips in May 2026 and only six have rows. Probe domains from the base names.
3. City of Toronto licence data (TAXICAB BROKER and LIMOUSINE SERVICE COMPANY). Twenty active brokers, about nine unread because their sites are empty or unreadable. Try them through their app store pages or phone-listed sites.
4. California CPUC TNC permit list. Wingz, Daytrip, Prime Time Rideshare, Kango and Ridenroll are unread.
5. Searches built on settlement wording ("weekly settlements", "paid weekly") plus the word contractor. Worked for courier companies (five US rows). Run it by state and province.

## Gaps

- US: only 23 rows. No Texas, Colorado, Massachusetts or Ohio rows because their list pages were blocked. No large-city taxi companies beyond Chicago, Washington, Seattle and San Francisco.
- Canada: Quebec, Newfoundland and Labrador, Ottawa and Toronto are thin. 29 Calgary limousine brokerages have no row.
- Segments with no rows: shuttles and rideshare-companies. Logistics has six rows.
- 72 of 104 rows have no fleet or driver count.
- No public complaint about pay errors and no payroll job post found for any row.
- fare.coop and three state TNC pages blocked automated fetches, so their rows are missing.

## What I would change in the prompt

1. Give a row target per country and per segment. "Finish Canada" has no end because the long tail is endless.
2. Say whether a registry entry alone can make a row. I used only rows backed by the company's own page, which cut yield.
3. Say whether a business Gmail address that a company publishes as its contact is allowed. I allowed two and marked them.
4. Say which time zone the stop time uses. The second message said Eastern, the first did not.
5. Tell the run to verify a push with `git ls-remote origin refs/heads/<branch>`. A shallow clone has no local ref for a new branch.
6. Say whether the company website claims in the product brief may be softened in findings. The Part XX claim on the website is wider than the Act text.
