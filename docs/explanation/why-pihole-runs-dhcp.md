# Why Pi-hole Is Also Running DHCP

Originally, I wanted the Verizon CR1000A router to keep handling DHCP while simply pointing all devices to Pi-hole for DNS.

That did not work properly.

The router did not give me reliable control over custom DNS settings for client devices. Even after changing settings, devices were still not consistently using Pi-hole for DNS.

The workaround was to:

1. Enable DHCP inside Pi-hole
2. Disable DHCP on the Verizon CR1000A router
3. Let Pi-hole hand out IP addresses and DNS settings

This solved the problem because every device now receives the Raspberry Pi as its DNS server automatically.

The full record of this decision, with the alternatives I considered, is in [0001 - DHCP moves to Pi-hole](../decisions/0001-dhcp-on-pihole.md). To undo it, see [Restore DHCP to the Verizon router](../how-to/restore-router-dhcp.md).
