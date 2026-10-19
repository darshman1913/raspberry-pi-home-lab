# 0001 - DHCP Moves to Pi-hole

**Status:** Accepted

**Date:** 2026-10-18

## Context

The plan for project 01 was simple. The Verizon CR1000A keeps doing DHCP and tells every device to use Pi-hole at `192.168.1.165` for DNS.

That did not work. The router would not reliably advertise a custom DNS server to clients. Even after changing the settings, some devices kept using router or ISP DNS and skipped Pi-hole completely. DNS filtering only works if devices actually send their requests to the Pi, so this broke the whole point of the project.

## Decision

Pi-hole runs DHCP for the home network. DHCP on the Verizon CR1000A is disabled.

Pi-hole hands out `192.168.1.100` to `192.168.1.250`, sets the gateway to `192.168.1.1`, and gives itself as the DNS server. The Pi keeps a static IP of `192.168.1.165` in `dhcpcd.conf`.

## Consequences

* Every device gets Pi-hole as its DNS server automatically. All 5 active clients showed up in the dashboard.
* The Pi is now infrastructure. If it goes down, new devices cannot get an IP address and existing leases eventually run out.
* The static IP is not optional anymore. During the switchover the Pi lost network access until the static IP was in place.
* Only one DHCP server can be on at a time. Switching back has an order to it. See [Restore DHCP to the Verizon router](../how-to/restore-router-dhcp.md).
* Clients have to renew their leases after any change. See [Force clients to renew DHCP leases](../how-to/renew-client-leases.md).

## Alternatives considered

* **Set DNS by hand on every device.** Works for a laptop. Does not work well for phones, the TV, and anything else that does not expose a DNS setting. It also breaks the "network-wide" goal.
* **Buy a different router.** A router that advertises custom DNS properly would let the CR1000A setup stay as planned. It costs money and the lab has to stay free.
* **Pi-hole as DNS only.** Keep the router on DHCP and accept that some devices bypass filtering. That is the setup that was already failing.
