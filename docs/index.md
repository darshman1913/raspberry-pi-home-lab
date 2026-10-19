# Raspberry Pi Home Lab

This is my cybersecurity and networking home lab, built around a Raspberry Pi 5, my home network, and a Windows laptop. Every project here runs on real hardware on a real network, and the docs include the parts that broke.

The network is simple. Internet comes in through a Verizon CR1000A router. The Raspberry Pi 5 runs Pi-hole for DNS and DHCP, and every home device gets its settings from the Pi.

## Hardware

| Item                   | Use                                                     |
| ---------------------- | ------------------------------------------------------- |
| Raspberry Pi 5 (8GB)   | Main home lab server                                    |
| Verizon CR1000A Router | Home internet router                                    |
| Windows Laptop         | Management, testing, SSH, GitHub documentation          |
| Home Devices           | Real clients for testing DNS, DHCP, and network changes |

Full versions are in [Versions and hardware](reference/versions.md).

## Status

**Done**

* ✅ [01 - Pi-hole DNS Sinkhole](tutorials/01-pihole-dns-sinkhole.md). Network-wide DNS filtering, with Pi-hole running DHCP.
* ✅ [02 - WireGuard VPN Server](tutorials/02-wireguard-vpn-server.md). Encrypted remote access into the home network.
* ✅ [03 - Cowrie SSH Honeypot](tutorials/03-cowrie-honeypot.md). 48 hours of real attack traffic captured and analyzed.

**In progress**

* This docs site.

**Planned**

* 04 - IDS with Suricata
* 05 - Centralized SIEM with the ELK Stack
* 06 - Active Directory Lab
* 07 - Network Monitoring with Zeek

## How these docs are organized

The [tutorials](tutorials/index.md) are the full build writeups. The [how-to guides](how-to/index.md) cover one task each. [Reference](reference/index.md) has the IPs, versions, and commands. [Explanation](explanation/index.md) covers why things work the way they do, and the [decision log](decisions/index.md) records the big choices.

I am building this lab to learn cybersecurity by doing it, not just by watching videos or reading notes.
