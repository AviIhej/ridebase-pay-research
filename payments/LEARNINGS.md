# Learnings

Minutes in YIELD.csv are approximate, read from the session clock.

## Entries

1. Page fetch blocked at start. Tried curl and the fetch agent. Symptom: CONNECT tunnel failed 403 and getaddrinfo ENOTFOUND. Fix: the owner set network access to full internet. Rule: test one fetch before planning, and ask for network access at once.
2. canada.ca refused every request. Symptom: curl 92 HTTP/2 INTERNAL_ERROR and curl 52 empty reply. Tried HTTP/1.1 and a plain user agent. Fix: read the Income Tax Act text on laws-lois.justice.gc.ca pages 232 and 233. Rule: use Justice Laws for legislation.
3. BC Passenger Transportation Board search page showed a Cloudflare challenge. Not bypassed. Rule: do not retry; use company sites.
4. Search summaries are not sources. WebSearch returns summaries of directories and job boards. Fix: use the result URLs only to find a company's own domain, then read that domain. Rule: block directory domains in the query.
5. Guessing domains in bulk worked. A small probe script that fetches the home page title for 30 guesses found about a third. Rule: probe name variants with .ca and .com before searching.
6. Toronto open data has a datastore API. Query the licence resource with Category=TAXICAB BROKER and drop rows with a cancel date. Rule: check CKAN-style portals for a datastore_search endpoint first.
7. Many small taxi sites show no fleet size or pay terms. Rule: do not spend more than two page reads on a site that shows none.
8. Many sites publish a person's email. Rule: record only role inboxes or forms.
9. Spam pages. whitecabrocks.ca and kabu.ca carry unrelated casino text. Rule: skip the site and note it in the README.
10. Courier carrier sites load text by script and the plain fetch returned nothing. Rule: do not retry; use job posts on the company's own domain if present.
11. robots.txt disallowed some sites. Rule: skip and list in sources.md.

## Dead ends

- canada.ca (twice)
- ptboard.bc.ca search page
- Quebec CTQ "intermédiaires en services de transport" list (heavy vehicles, not taxis)
- Edmonton open data keyword search for taxi (returns Chicago data)
- cptdb.ca taxi wiki page (no company links)
- Courier and airport shuttle searches with a pay phrase (return job boards and trucking carriers)
