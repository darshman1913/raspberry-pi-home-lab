# Explanation

These pages cover the why behind the lab. How the pieces work and why I set them up this way.

* [How DNS filtering actually works](how-dns-filtering-works.md)
* [Why Pi-hole took over DHCP](why-pihole-runs-dhcp.md)
* [Why the diagrams are code](why-diagrams-are-code.md)

## Security Notes

### 01 - Pi-hole DNS Sinkhole

This project is running inside my own home network for learning purposes.

I am not using this to monitor other people’s networks or bypass security controls. The purpose is to understand DNS, DHCP, and network filtering in a controlled lab environment.

### 02 - WireGuard VPN Server

Never share:

* Private keys
* Full WireGuard configs
* Public IP address
* Router login screenshots
* QR codes after deployment

Safe to share:

* Public keys
* Redacted configs
* Tunnel IPs
* Network diagrams

If a private key is exposed:

1. Generate a new keypair
2. Update peer configuration
3. Remove compromised key immediately
