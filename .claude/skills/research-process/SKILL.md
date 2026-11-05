---
name: research-process
description: Playbook for finding Canadian and US driver-pay buyers for Ridebase Pay and writing payments/companies.csv rows.
---

# Research process

## Order of work
1. Read payments/LEARNINGS.md and payments/YIELD.csv first.
2. Canada first, then the US. Never say a US company can buy the product today.
3. Push to develop and research/payments-ca every 25 rows. Update payments/STATUS.md each time.

## Sources that gave rows fastest
1. Municipal licence lists. City of Toronto open data (datastore API, Category TAXICAB BROKER, no cancel date) and City of Calgary broker pages. They give names and phones. Then find each company's own site.
2. Web search by city with directory domains blocked (yelp, yp, bbb, facebook, indeed, linkedin, wikipedia). Keep only results on a company's own domain.
3. Bulk domain probing. Try name.ca and name.com for 30 names and keep sites whose title matches.
4. Searches for ride-hail startups and accessible transport companies. These pages state pay terms more often than taxi pages.

## How to read a company site
- Fetch home, about, contact, careers or driver pages. Check robots.txt first.
- Pull: fleet or driver count, city, how drivers are paid, a role inbox or form.
- Skip personal emails, free-mail addresses unless the company publishes them as its contact, and guessed addresses.
- A row needs its own source URL on the company domain.

## Checklist for a source
- Does it name companies with a city? 
- Can I reach each company's own page?
- Does it show size or pay terms for at least one in five?
- If two page reads show neither, drop the site.

## Row rules
- size_basis starts with Sourced or No source yet.
- how_they_pay_drivers says Not stated on pages read unless the page says it.
- Scores: 5 stated commission plus regular payout; 4 published size of 100 or more, contract work or member drivers; 3 licensed with a contact; 2 small or unknown.
- No em dashes, no competitor names, no attribution lines in commits.

## Verified claims
- Part XX: Income Tax Act pages 232 and 233 on laws-lois.justice.gc.ca. The Act covers platform operators, not every dispatcher.
- Interac: Payments Canada press release, 43% paid and 48% preferred among gig workers, Leger 2023.

## Do not retry
See Dead ends in payments/LEARNINGS.md.
