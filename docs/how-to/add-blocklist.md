# Add a Blocklist to Pi-hole

## When you need this

Use this when the default list is missing something you want gone, like a tracker that keeps showing up in the query log.

Adding more curated blocklists is still on the Pi-hole next steps list. I have not done it yet, so the lab is still running the default list with 83,497 domains. These steps are what I plan to follow.

## Steps

1. Find the list you want and copy its raw URL. It has to point at the plain text file of domains, not the web page that describes the list.

2. Open the Pi-hole dashboard and log in.

    ```text
    http://192.168.1.165/admin
    ```

3. Go to Lists. Paste the URL into the address field, add a comment so you remember where it came from, and add it as a blocklist.

4. Update gravity so Pi-hole downloads the new list. Over SSH:

    ```bash
    pihole -g
    ```

## Verify

The dashboard number for domains on the blocklist should go up from 83,497.

Then pick a domain that is on the new list and test it from Windows:

```powershell
nslookup <domain-from-the-new-list>
```

A blocked domain returns:

```text
Address: 0.0.0.0
```

## What can go wrong

* **Wrong URL.** If you paste the page URL instead of the raw file, gravity cannot read it and the domain count does not change. Read the `pihole -g` output for that list.
* **False positives.** A bigger list blocks more of the stuff you actually use. Watch `pihole -t` or the query log for a day after adding a list. If something breaks, allowlist that domain or remove the list.
* **The device still resolves the domain.** Windows may have the old answer cached. Run `ipconfig /flushdns` and test again. If it still resolves, run `ipconfig /all` and check that the DNS server is `192.168.1.165`.
