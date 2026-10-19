# How DNS Filtering Actually Works

Before a device can load anything, it asks a DNS server to turn a name like `doubleclick.net` into an IP address. Pi-hole sits in that spot for every device on my network.

When a request comes in, Pi-hole checks the domain against its blocklist. In my setup that list had 83,497 domains. If the domain is on it, Pi-hole answers with `0.0.0.0`. The device gets an address that goes nowhere, so the ad or tracker never loads. If the domain is allowed, Pi-hole forwards the request to Cloudflare at `1.1.1.1` with DNSSEC on and passes the answer back.

## How DNS Works in This Setup

```text
Home Device
   |
   | DNS request
   v
Pi-hole on Raspberry Pi 5
   |
   | If domain is blocked:
   | returns 0.0.0.0
   |
   | If domain is allowed:
   v
Cloudflare DNS 1.1.1.1
   |
   v
Internet
```

## What it does not do

Pi-hole only sees the names devices ask for. It does not see the web traffic itself, and it cannot block anything that is served from a domain that is allowed.

The blocking rate moved between 8% and 45% depending on which devices were active and what they were doing.

## The catch

This only works if devices actually send their DNS requests to the Pi. A device that uses a different DNS server skips the filter completely. That is the problem I hit with the Verizon CR1000A, and it is why Pi-hole ended up running DHCP. See [Why Pi-hole took over DHCP](why-pihole-runs-dhcp.md).

The quickest check from a client is:

```powershell
nslookup doubleclick.net
```

A blocked domain comes back as `Address: 0.0.0.0`.
